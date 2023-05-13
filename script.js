import "whatwg-fetch"

_                = require "underscore"
async            = require "async"
fp               = require "lodash/fp"
i18n             = require("i18next").default
momentTZ         = require "moment-timezone"
{ Settings }     = require "luxon"
React            = require "react"
ReactDOM         = require "react-dom"
request          = require "request"
Sentry           = require "@sentry/browser"
storage          = require "local-storage-fallback"

highchartsLocales            = require "./locales/highcharts"
momentLocales                = require "./locales/moment"
ProgressBar                  = require "components/progressbar.cjsx"
PROGRESS_BAR_SEGMENT = 11.11

# Gets you every time
# Webpack documentation does a terrible job at explaining this
# coffeelint: disable
window.STATICS_PATH          = STATICS_PATH
window.GATEWAY_HTTP_OVERRIDE = GATEWAY_HTTP_OVERRIDE # may be undefined
window.GATEWAY_WS_OVERRIDE   = GATEWAY_WS_OVERRIDE # may be undefined
# coffeelint: enable

# stupid hash routing breaks normal window.location.search
# Anyway, it's nice to have prepared searchParams available on the window
search = window.location.href.split('?')[1]
window.searchParams = new URLSearchParams search or ''

# Needed for Hot Module Replacement
module.hot.accept() if typeof(module.hot) isnt "undefined"

# addEventListener doesn't play nice with HRM
window.onunhandledrejection = (event) ->
	console.error "Unhandled rejection #{event.reason}"

# underscore
window._ = _

# Shim window.localStorage
# Fallback for when no localStorage
window.localStorage = storage if not ('localStorage' of window)

# jquery
window.$      = require "jquery"
window.jQuery = window.$
window.setMomentLocale = () ->
	return unless window.locale

	if momentLocales[window.locale]
		moment.locale window.locale, momentLocales[window.locale]
	else
		moment.locale window.locale

	moment.updateLocale window.locale, week:
		dow: 1
		doy: 4

	momentTZ.tz.setDefault window.timezone
	# Set defaults for luxon
	Settings.defaultLocale = window.locale
	Settings.defaultZoneName = window.timezone

# Twitter Typeahead
require "../vendor/typeahead.bundle.min.js"

# datetimepicker
require "../vendor/datetimepicker/jquery.datetimepicker.js"

# jcanvas
require "../vendor/jcanvas/jcanvas.min.js"

# form validation
require "../vendor/jquery.validate/jquery.validate.js"

# polyfills
require("react-app-polyfill/ie11")
require("react-app-polyfill/stable")

# socket.io
io = require "socket.io-client"

# backbone
Backbone   = require "backbone"
ViewMaster = require "viewmaster"
require "backbone.paginator"

window.Backbone            = Backbone
window.Backbone.$          = window.$
window.Backbone.ViewMaster = ViewMaster

# Polyfills
require('custom-event-polyfill')

# Backgrid
window.Backgrid = require "../vendor/backgrid/backgrid.min.js"
require "../vendor/backgrid/backgrid-paginator.js"

# socket binding
require "backbone.iobind/dist/backbone.iobind.js"
require "backbone.iobind/dist/backbone.iosync.js"

# Bootstrap
require "../vendor/bootstrap/bootstrap.min.js"
require "../vendor/bootstrap/bootstrap-tagsinput.min.js"
require "../vendor/datepicker/bootstrap-datepicker.js"

# Highcharts
window.Highcharts = require "../vendor/highcharts/highstock.js"
(require "../vendor/highcharts/highcharts-more.js")(window.Highcharts)
(require "../vendor/highcharts/no-data-to-display-custom.js")(window.Highcharts)
(require "../vendor/highcharts/exporting.js")(window.Highcharts)
require "../vendor/highcharts/highcharts-flag-overlap.js"
require "../vendor/highcharts/export-csv.js"

# PouchDB
PouchDB = require("pouchdb").default
window.PouchDB or= PouchDB

# set window events
require "./lib/DOMOperations"

# moment.js plugins
window.moment = moment = require "moment"
require "moment-duration-format"

# toastr
toastr = require "toastr"
toastr.options =
	positionClass: "toast-bottom-right"

window.toastr = toastr
alert = require "./lib/alert"

# Triggers "chart.reflow" when tab is active
# coffeelint: disable
$(window).on "shown.bs.tab", -> $(window).trigger "resize"
# coffeelint: enable
Router       = require "./Router"
NoAccessView = require "./views/NoAccess"

if process.env.NODE_ENV is "production"
	try
		Sentry.init
			# dsn: 'https://a9209d6219114caeaecd63cc7a41d243@sentry.cloud1.viriciti.com/2' # Old DSN
			dsn: "https://5de8a5a12b45460e8ae1cb148f1ce3ef@o1261169.ingest.sentry.io/6478848"
			integrations: (integrations) ->
				# integrations will be all default integrations
				integrations.filter (integration) ->
					integration.name isnt 'Breadcrumbs'
			beforeSend: (event) ->
				return event unless event.exception and event.exception.values

				_.map event.exception.values, (exception) ->
					console.error exception

				return event
	catch err
		console.error "Sentry error", err

localisation = null

renderProgressBar = (progress) ->
	status += progress

	progressBarElement = window.document.getElementsByClassName("startup-progress-bar")[0]
	ReactDOM.render <ProgressBar progress={status}/>, progressBarElement if progressBarElement

getSocket = (skipWebsocket, cb) ->
	try
		renderProgressBar(PROGRESS_BAR_SEGMENT)
		return cb() if skipWebsocket

		nows = switch window.location.hostname
			when "nows.viriciti.com" then true
			when "nows.localhost" then true
			else false

		### NO WS ###
		getNowsOptions = ->
			# ? This window.apiKey stuff is never used right?
			path = "/api/v1/monitoring/nowebsocket-livedata" + if window.apiKey then "?apiKey=" + window.apiKey + "&end=true" else ""

			"reconnect":          true
			"reconnection delay": 2000
			transports:           ["polling"]
			path: path

		getNowsOptionsLive = ->
			# ? This window.apiKey stuff is never used right?
			path = "/api/v1/live/io-nows" + if window.apiKey then "?apiKey=" + window.apiKey + "&end=true" else ""

			"reconnect":          true
			"reconnection delay": 2000
			transports:           ["polling"]
			path: path

		### WS ###
		getWsOptions = ->
			# ? This window.apiKey stuff is never used right?
			path = "/api/v1/monitoring/livedata" + if window.apiKey then "?apiKey=" + window.apiKey + "&end=true" else ""

			"reconnect":          true
			"reconnection delay": 2000
			transports:           ["websocket"]
			path: path

		getWsOptionsLive = ->
			# ? This window.apiKey stuff is never used right?
			path =                 "/api/v1/live/io" + if window.apiKey then "?apiKey=" + window.apiKey + "&end=true" else ""

			"reconnect":          true
			"reconnection delay": 2000
			transports:           ["websocket"]
			path: path

		socket = io.connect window.gatewayWS, if nows then getNowsOptions() else  getWsOptions()
		live   = io.connect window.gatewayWS, if nows then getNowsOptionsLive() else getWsOptionsLive()

		live.on "reconnect", ->

			connection = (require "lib/Connection").singleton()
			connection.resendLiverequest()

			if window.track
				name = "browser:socket-reconnect"
				details =
					reason: "Live socket reconnected"

				window.track.event { name, details }

		live.on "disconnect", ->
			if window.track
				name = "browser:socket-disconnect"
				details =
					reason: "Live socket disconnected"

				window.track.event { name, details }


		socket.on "reconnect", ->
			if window.track
				name = "browser:socket-reconnect"
				details =
					reason: "Monitoring server socket reconnected"

				window.track.event { name, details }

		socket.on "disconnect", ->
			if window.track
				name = "browser:socket-disconnect"
				details =
					reason: "Monitoring server socket disconnected"

				window.track.event { name, details }

		# server messages
		socket.on "client:message", (message) ->
			return unless message.type and message.data
			alert type: message.type, message: message.data, options: message.options

		async.parallel [
			(cb) -> socket.once "ready", cb
			(cb) -> live.once "ready",   cb
		], ->
			renderProgressBar(PROGRESS_BAR_SEGMENT)
			cb null, { socket, live }

	catch cb

getChargers = (cb) ->
	# NOTE
	# request js timeout does not seem to always work, maybe because the server
	# has responded but then hangs? We force a timeout using async.race for
	# good measure.
	async.race [
		(cb) ->
			fields = [ "name", "identity", "connectors", "alive", "chargerModel" ]

			request.get
				uri: "api/v1/chargestations/chargestations"
				qs:
					filtered: true
					select:   fields.join ","
					populate: JSON.stringify
						path: "chargerModel"
						select: "brand name variationName"
					query:
						JSON.stringify active: true
				json: true
				timeout: 5000
			, (error, response, body) ->
				if error or response.statusCode >= 500
					return cb new Error "Failed to retrieve charging stations [#{response.statusCode}]"

				cb null, body

		(cb) ->
			timeout = setTimeout ->
				cb new Error "Failed to retrieve charging stations [timeout]"
			, 5000
	], (error, body) ->
		if error
			console.error error.message
			toastr.error error.message
			return cb null, []

		cb null, body

getAssets = (cb) ->
	request.get
		uri: "api/v2/portal/assets"
		qs:
			filtered: true
			fields: "_id name vid vehicleModel type type_old icon operator viface assetType timezone active mac"

	, (error, response, body) ->
		if error
			console.error "Error fetching chargers", error
			toastr.error "Failed to retrieve assets"
			return cb error
		cb null, body

getUser = (userId, skipViewaccess, cb) ->
	async.parallel
		viewaccess: (cb) ->
			# If chargerCount is above 0, there are no asets. See bottom of this file
			return cb null, {} if skipViewaccess

			request.get
				uri: "api/v2/portal/users/#{userId}/viewaccess"
			, (error, res, viewaccess) ->
				return cb error if error

				renderProgressBar(PROGRESS_BAR_SEGMENT)
				# This will not likely happen, we already returned on top of this function if no assets
				return cb null, viewaccess unless res.statusCode is 403 or not viewaccess

				console.error "No viewaccess found"
				window.location.href = "/#noaccess"
				return cb new Error "No viewaccess found"

		user: (cb) ->
			request.get
				uri: "api/v2/portal/users/#{userId}"
				headers:
					"Cache": false
				qs:
					# ! missing field selection
					populate:
						path:   "company"
						select: "title type theme emissionSettings "
			, (error, res, user) ->
				return cb error if error
				return cb new Error "No user found #{res?.statusCode}" unless user

				renderProgressBar(PROGRESS_BAR_SEGMENT)

				user.unit_system = user.unitSystem
				window.unitSystem = user.unitSystem

				cb null, user

		acl: (cb) ->
			request.get
				uri: "api/v2/portal/acl"
				qs:
					userId: userId
			, (error, response, body) ->
				return cb error if error
				cb null, Object.keys body
	, cb

setWindowUser = ({ userId, timezone, language, companyId, email, theme, locale }) ->
	window.userId       = userId
	window.timezone     = timezone
	window.locale       = locale
	window.userLanguage = language
	window.companyId    = companyId
	window.email        = email
	window.theme        = theme
	window.localStorage.setItem("theme", theme)

# Awful...
loadStyle = (theme) ->
	createAttachLink = (url) ->
		linkElement = document.createElement('link')
		linkElement.setAttribute('rel', 'stylesheet')
		linkElement.setAttribute('href', url)
		document.getElementsByTagName('head')[0].appendChild linkElement

	theme = "default" if not theme

	createAttachLink "https://cdn.viriciti.com/styles/8.6.2/default.bundle.css"

	if theme isnt "default"
		createAttachLink "https://cdn.viriciti.com/styles/8.6.2/#{theme}.bundle.css"

	createAttachLink "https://atomic-components.viriciti.com/themes/#{theme}.bundle.css"

initUser = ({ userId, skipViewaccess, impersonating = {}, skipUber = false, skipTrack = false, session }, cb) ->
	getUser userId, skipViewaccess, (error, userInfo) ->
		return cb error if error

		userInfo.user?.portalAddress = window.portalAddress # ! Whaat

		user = require("models/User").singleton userInfo
		user.setHasOnlyChargers() if skipViewaccess # If this is true, the user has charging stations

		unless skipUber
			user.setIsUber if impersonating?.active is true then impersonating.withUber else user.get("company")?.type is 'uber'

		if user.get("company").theme isnt window.localStorage.getItem("theme")
			loadStyle user.get("company").theme

		setWindowUser {
			userId,
			timezone  : user.get "timezone"
			language  : session?.language or user.get "language"
			locale    : session?.locale or user.get "locale"
			email     : user.get "email"
			companyId : (user.get "company")._id
			theme     : (user.get "company").theme
		}

		window.document.documentElement.setAttribute "dir", "rtl" if window.userLanguage is "he"

		window.Highcharts.setOptions
			global:
				timezone: window.timezone
			lang: highchartsLocales[window.userLanguage] if highchartsLocales[window.userLanguage]

		# TODO: Fix the scope or remove it altogether
		# Sentry.configureScope (scope) ->
		# 	name = user.get("name")
		# 	scope.setUser
		# 		username: "#{user.name?.first} #{user.name?.last}"
		# 		company:  (user.get "company")
		# 		userId:   userId

		cb()

setUserAndSession = (skipViewaccess, cb) ->
	# ! Who does this!? Auto Reports does
	serviceName = window.searchParams.get "serviceName"
	userId      = window.searchParams.get "userId"
	window.isService             = Boolean serviceName

	unless window.isService
		request.get
			uri:             "api/v1/sessions/my"
			withCredentials: true
			json:            true
		, (error, response, body) ->
			return cb error if error
			return cb new Error "Error retrieving session information from the gateway." unless response.statusCode is 200
			return cb new Error "Empty body from the gateway." unless body?.user

			require("models/Session") body
			userId  = body.impersonating?.user?._id or body.user?._id

			initUser {
				userId
				skipViewaccess
				impersonating: body.impersonating
				session: body
			}, cb

	else
		console.warn "🚨   Running as service for #{serviceName} for user #{userId}!   🚨"

		# ? Empty user, whY?
		require("models/Session") { user: { name: {} } }

		initUser {
			userId: userId # * Auto Reports sets this too
			skipViewaccess
			skipTrack: true
			skipUber: true # ! Odd
		}, cb

getConfig = ->
	if window.GATEWAY_HTTP_OVERRIDE or window.GATEWAY_WS_OVERRIDE
		# * Only webpack define plugin can be used only to override the gateway URL infer from location
		# localhost is a special case and needs an override value
		gatewayHTTP = window.GATEWAY_HTTP_OVERRIDE
		gatewayWS   = window.GATEWAY_WS_OVERRIDE
		console.info "Gateway URL override from webpack define plugin #{gatewayHTTP} & #{gatewayWS}"

	else
		gatewayHTTP = window.location.origin
		protocol    = if window.location.protocol is "http:" then "ws://" else "wss://"
		gatewayWS   = protocol + window.location.origin.split("://")[1]
		console.info "Gateway URL based on current location #{gatewayHTTP} & #{gatewayWS}"

	window.gatewayHTTP = gatewayHTTP.replace /\/+$/, "" # trailing slash
	window.gatewayWS   = gatewayWS.replace /\/+$/, "" # trailing slash

	request = request.defaults
		baseUrl:         window.gatewayHTTP
		withCredentials: true
		json:            true

	url = "#{window.gatewayHTTP}/api/v1/config?keys=dashboard"
	result = await fetch url, {
		credentials: 'include',
		method: 'GET'
	}

	unless result.status in [ 200, 304 ]
		message = "Could not retrieve configuration. "
		alert { type: "error", message }
		throw new Error message

	if not result.ok or result.status is 401
		message = "Session has expired. Redirecting..."
		alert { type: "error", message }
		setTimeout ->
			window.location.href = "/logout"
		, 3000
		throw new Error message

	config = await result.json()
	{ env, mapBox, whiteLabel, portalAddress, localisation } = config.dashboard

	portalMap =
		'proterra-server.viriciti.com':    'https://proterra.viriciti.com'
		'prems-dashboard.tevva.com':       'https://prems.tevva.com'
		'customerportal.vayongroup.com':   'https://login.vayongroup.com'
		'dashboard.motivps.com':           'https://portal.motivps.com'
		'dashboard.phoenixmotorcars.com':  'https://portal.phoenixmotorcars.com'
		'navineo.viriciti.com':            'https://navineo-portal.viriciti.com'
		'vdl-chargestations.viriciti.com': 'https://vdl-portal.viriciti.com'
		'monitoring.livetech-systems.com': 'https://portal.livetech-systems.com'

	window.portalAddress      = whiteLabel?.addresses?.portal or portalMap[window.location.host] or portalAddress
	window.supportedLanguages = localisation.supportedLanguages
	window.osmAddress         = mapBox.address
	window.mapBoxAPIKey       = mapBox.APIKey
	window.NODE_ENV           = env

# ! Start !
# progressBar
loadStyle(window.localStorage.getItem("theme"))
status = 0
renderProgressBar 0

getConfig().then ->
	setUp = (assets, chargers) ->
		require("collections/Chargers").singleton chargers

		# Some of this stuff could be parallelized, but we're seeing user's laptops blow up, the assumption is that
		# doing this in series reduces spreads out the load a bit
		async.series [
			(cb) ->
				skipViewaccess = chargers.length and not assets.length

				setUserAndSession skipViewaccess, (error) ->
					return cb error if error

					companyId = require("models/User").singleton().toJSON().company._id

					request.get
						uri: "api/v2/portal/facilities"
						qs:
							where:
								company: companyId

					, (error, res, facilities) ->
						if error
							console.error(error.message)
							toastr.error "[Facilities]: #{error.message}"
							return cb error

						require("collections/Facilities").singleton facilities
						renderProgressBar(PROGRESS_BAR_SEGMENT)

						cb()
			(cb) ->
				require("./i18n") localisation, (err) ->
					throw err if err
					cb()
			(cb) ->
				unless chargers.length or assets.length
					new NoAccessView().render()
					return cb new Error "No assets and no chargers found"

				cb()

			(cb) ->
				return cb() if not assets.length

				request.get
					uri: "api/v1/vehicle-model"
					qs:
						select: 'brand,model,energyType'
				, (error, res, vehicleModels) ->
					return cb error if error

					renderProgressBar(PROGRESS_BAR_SEGMENT)

					assets = _.map assets, (asset) ->
						vehicleModel       = _.find(vehicleModels, { _id: asset.vehicleModel }) or {}
						asset.energyType   = vehicleModel.energyType or ""
						asset.title        = asset.name
						asset.typeID       = asset.type
						asset.type         = asset.type_old
						asset._id          = asset.vid
						asset.actual_id    = asset._id
						asset.icon         = vehicleModel.icon or vehicleModel.vehicleType?.toLowerCase() or asset.icon
						asset.model        = vehicleModel.model or ""
						asset.manufacturer = vehicleModel.brand or ""
						asset.fleets       = [] #default
						asset

					require("collections/Vios").singleton assets

					cb()
			(cb) ->
				return cb() unless assets.length

				typeIds = _.compact _.uniq _.pluck require("collections/Vios").singleton().toJSON(), "typeID"

				translate = (toTranslate) ->
					return toTranslate unless toTranslate.category or toTranslate.title

					category = if toTranslate.category
						i18n.t "categories:#{fp.camelCase(toTranslate.category)}", defaultValue: toTranslate.category
					else
						toTranslate.category

					{
						...toTranslate,
						category,
						title:    i18n.t "parameters:#{fp.camelCase(toTranslate.title)}", defaultValue: toTranslate.title
					}

				progressBarSegment = PROGRESS_BAR_SEGMENT / typeIds.length

				fields = ['_id', 'vid', 'parameters', 'params', 'analyses', 'reports', 'messages', 'map', 'title', 'vcm']

				async.mapLimit typeIds, 3, (typeId, cb) ->
					request.get
						uri: "api/v2/portal/types/#{typeId}"
						qs: { filtered: true, fields }
					, (error, res, type) ->
						return cb error if error

						result = {
							...type
							_id:        type.vid
							new_id:     type._id
							portal_id:  type._id
							parameters: fp.map translate, type.parameters
							analyses:   fp.map translate, type.analyses
							params:     fp.map translate, type.params
							reports:    fp.map translate, type.reports
							messages:   fp.map translate, type.messages
						}

						renderProgressBar progressBarSegment

						cb null, result
				, (error, types) ->
					return cb error if error

					unless types.length
						new NoAccessView().render()
						return cb new Error "No types found"

					require("collections/Types").singleton types
					cb()
			(cb) ->
				return cb() unless assets.length

				request.get
					uri: "api/v2/portal/fleets"
					qs:
						fields: "_id name assets"
						populate:
							path: "vios"
							select: "type name vid group vin active assetType type_old"
						filtered: true

				, (error, response, fleets) ->
					return cb error if error

					require("collections/Fleets").singleton fleets
					renderProgressBar PROGRESS_BAR_SEGMENT
					cb()

			(cb) ->
				skipWebsocket = assets.length is 0

				getSocket skipWebsocket, (error, { socket, live } = {}) ->
					return cb error if error
					return cb()     unless socket and live

					(require "lib/Connection").singleton socket, live
					renderProgressBar(PROGRESS_BAR_SEGMENT)

					cb()
		], (error) ->
			if error
				Sentry.captureException error
				console.error error
				throw error

			types  = require("collections/Types").singleton()
			fleets = require("collections/Fleets").singleton()
			user   = require("models/User").singleton()

			# We need type_old on fleet vios aswell.. Very hard to apply in the backend, so unfortunately this lives here. Only needed here too so..
			if fleets.length
				fleets = fleets.toJSON()
				fleets = _.map fleets, (fleet) ->
					fleet.vios = _.compact _.map fleet.vios, (vio) ->
						foundType = types.find (type) -> type.get("new_id") is vio.type
						return console.error "No type found for vio with vid #{vio.vid}" unless foundType

						vio.type_old = foundType.get "vid"
						vio.title    = vio.name
						vio._id      = vio.vid

						vio

					fleet

				require("collections/Fleets").singleton fleets

			window.getVios  = (page) -> require("collections/Vios").for page
			if not window.location.href.includes("ocpp_chargestations") and user.get "hasOnlyChargers"
				window.location = "/#ocpp_chargestations"

			progressBarElement = window.document.getElementsByClassName("startup-progress-bar")[0]
			ReactDOM.unmountComponentAtNode progressBarElement if progressBarElement

			new Router

			if Backbone.History.started
				route = Backbone.history.fragment or ""
				Backbone.history.loadUrl route
			else
				Backbone.history.start pushState: true

			require "./zenDesk.js" unless window.isService

	async.parallel [
		(cb) -> getAssets cb
		(cb) -> getChargers cb
	], (error, [ assets, chargers ]) ->
		return console.error "Failed to fetch assets or chargers: #{error.message}" if error

		setUp assets, chargers
