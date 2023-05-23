
import requests
import os
import json
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from constants import USERNAME, PASSWORD

# TODO: Store credentials in environment variable


disable_warnings(InsecureRequestWarning)

baseURL = "https://dashboard.viriciti.com/api/" 
companyID = "60819a6e720b0a5d366a68e7"
# "https://api.viriciti.com/api/v1/sessions/my"
tz = "America%2FToronto" 

def keys_reader(fname,keys):
    """
    Function to read in values stored in json file
    """
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    fp = os.path.join(fileDir, fname)
    keys_dict={}
    with open(fp,'r') as file:
        file_data =json.load(file)
        for key in keys:
            keys_dict[key] = file_data[key]
    return keys_dict

def getSessionCookies():
    """
    Function gets session cookies
    """

    global USERNAME; PASSWORD
    # USERNAME =urllib.parse.quote_plus('Melissa.Luc@metrolinx.com')
    #  PASSWORD = urllib.parse.quote_plus('CUgB4t9017ibkH^!')
    URL = "https://dashboard.viriciti.com/dashboard"
    # credentials= keys_reader("config.json",["USERNAME","PASSWORD"])
    # USERNAME = credentials["USERNAME"]
    # PASSWORD = credentials["PASSWORD"]

    payload = {"username": f"{USERNAME}",
        "password": f"{PASSWORD}",
        "submit":"",
        "header": {
            "Content-Type":"application/json"
        }

        }    

    with requests.Session() as session:
        post = session.post("https://accounts.viriciti.com/login", json=payload, verify=False)
        # r_login = session.get("https://accounts.viriciti.com/login", verify=False)
        r_dashboard = session.get(URL, verify=False)
        session_cookies_dict = session.cookies.get_dict()
        session_cookies_dict_new = {f'{key}=': v for key, v in session_cookies_dict.items()}
        session_cookie = ';'.join(key + value for key, value in session_cookies_dict_new.items())
        return session_cookie
        #TODO: confirm log in success 
        # print(r_dashboard.text)
    
   
cookies = getSessionCookies()
print(cookies)

def getRequest(URL_list):
    """
    Return get response as JSON
    """
    global cookies

    data_header = {
            "Cookie": cookies,
            "Content-Type": "application/json; charset=utf-8"
    }
    # TODO: update URL List to params dict
    URL = "".join(URL_list)
    response = requests.get(URL, headers= data_header ,verify=False)
    if response.status_code == 200:
        res_json = response.json()
        return res_json
    else:
        print("Could not retrieve data")
    
def postRequest(URL, payload):

    global cookies

    data_header = {
            "Cookie": cookies,
            "Content-Type": "application/json"
    }



    response = requests.post(URL, headers=data_header,json=payload ,verify=False)
    if response.status_code == 200:
        res_json = response.json()
        return res_json
    else:
        print("Could not retieve data")


def getReportsAPI(  vid = "adl_005",
                    analysis_name = "analyses.energy_charged",
                    start_dt =1672549200000,
                    end_dt = 1683863999999,
                    period_int = 1,
                    period = "day",
                    t_res = "hour",
                ):
    """
    Function that gets data from :
    https://dashboard.viriciti.com/reports
    Returns listObj

    https://dashboard.viriciti.com/api/v1/time/adl_004
    ?page=1
    &time%5Bstart%5D=1683777600000
    &time%5Bend%5D=1683864000000
    &time%5Bstep%5D%5B0%5D=30
    &time%5Bstep%5D%5B1%5D=seconds
    &time%5Btype%5D=first
    &label=ccvs1.wheel_based_vehicle_speed
    """
    global cookies; baseURL; tz


    URL_list  = [
        f"{baseURL}v1/report/{vid}?",
        f"labels%5B0%5D={analysis_name}",
        f"&time%5Bstart%5D={start_dt}",
        f"&time%5Bend%5D={end_dt}",
        f"&time%5Bperiod%5D%5B0%5D={period_int}",
        f"&time%5Bperiod%5D%5B1%5D={period}",
        f"&time%5Bresolution%5D={t_res}",
        f"&time%5Btimezone%5D={tz}",
        ]
    
    req = getRequest(URL_list)
    return req

def getTimeAnalysis(
                        vid,
                        start_dt,
                        end_dt,
                        page,
                        t_step = 30,
                        t_step_units = "seconds",
                        label = "analyses.gps_filter",
                    ):
    """
    Function that gets data from :
    https://dashboard.viriciti.com/api/v1/time/adl_004?
    page=1&
    time%5Bstart%5D=1683777600000&
    time%5Bend%5D=1683864000000&
    time%5Bstep%5D%5B0%5D=30&
    time%5Bstep%5D%5B1%5D=seconds&
    time%5Btype%5D=first&
    label=analyses.gps_filter

    https://dashboard.viriciti.com/api/v1/time/adl_005
    ?page=2
    &time%5Bstart%5D=1672549200000
    &time%5Bend%5D=1684123200000
    &time%5Bstep%5D%5B0%5D=6
    &time%5Bstep%5D%5B1%5D=hours
    &time%5Btype%5D=first
    &label=analyses.soc_used
    """
    global cookies; baseURL



    URL_list  = [
        f"{baseURL}v1/time/{vid}?",
        f"page={page}",
        f"&time%5Bstart%5D={start_dt}",
        f"&time%5Bend%5D={end_dt}",
        f"&time%5Bstep%5D%5B0%5D={t_step}",
        f"&time%5Bstep%5D%5B1%5D={t_step_units}",
        f"&time%5Btype%5D=first",
        f"&label={label}",
    ]

    req = getRequest(URL_list)
    return req

def getAssets():
    """
    Function that gets data from :
    https://portal.viriciti.com/api/v2/assets?
    sort=name
    &where%5Bcompany%5D=60819a6e720b0a5d366a68e7
    &fields%5B0%5D=name
    &fields%5B1%5D=name
    &fields%5B2%5D=vid

    sort: name
    where[company]: 60819a6e720b0a5d366a68e7
    fields[0]: name
    fields[1]: name
    fields[2]: vid
    """
    global cookies; companyID
    baseURL = "https://portal.viriciti.com/api/"
    URL_list  = [
        f"{baseURL}v2/assets?",
        f"sort=name",
        f"&where%5Bcompany%5D={companyID}",
        f"&fields%5B0%5D=name",
        f"&fields%5B1%5D=name",
        f"&fields%5B2%5D=vid",
    ]

    
    req = getRequest(URL_list)
    return req

def getAllFleet():
    """
    https://portal.viriciti.com/api/v2/fleets?
    fields%5B0%5D=name
    &fields%5B1%5D=company
    &search=&searchBy%5B0%5D=name
    &populate%5B0%5D%5Bpath%5D=company
    &populate%5B0%5D%5Bselect%5D%5B0%5D=title
    &limit=20&sort%5Blabel%5D=name
    &sort%5Bdirection%5D=asc
    """
    global cookies
    baseURL = "https://portal.viriciti.com/api/"
    limit = 20

    URL_list  = [
        f"{baseURL}v2/fleets?",
        f"fields%5B0%5D=name",
        f"&fields%5B1%5D=company",
        f"&search=&searchBy%5B0%5D=name",
        f"&populate%5B0%5D%5Bpath%5D=company",
        f"&populate%5B0%5D%5Bselect%5D%5B0%5D=title",
        f"&limit={limit}&sort%5Blabel%5D=name",
        f"&sort%5Bdirection%5D=asc"
    ]
    req = getRequest(URL_list)
    return req

def getActiveFleet(fleetType=None):
    """
    Function that gets data from :
    https://dashboard.viriciti.com/api/v2/portal/fleets?
    fields=_id%20name%20assets&
    populate%5Bpath%5D=vios&
    populate%5Bselect%5D=type%20name%20vid%20group%20vin%20active%20assetType%20type_old&
    filtered=true

    fields: _id name assets
    populate[path]: vios
    populate[select]: type name vid group vin active assetType type_old
    filtered: true   
    """
    global cookies; baseURL

    fleet_ids = getAllFleet()

    fleet_ids_dict ={}
    for f in fleet_ids:
        fleet_ids_dict[f"{f['name']}"] = f["_id"]



    if fleetType == "Electric":
        # fleetType = "/60de2e4b5550a1d51ce1b1d1"
        fleetType = "/" + fleet_ids_dict["Metrolinx ADL Electric 45'"]
    elif fleetType == "Diesel":
        # fleetType = "/60954e02608e434c39754aeb"
        fleetType = "/" + fleet_ids_dict["Metrolinx ADL Diesel 45'"]
    else:
        fleetType ="/" 

    URL_list  = [
        f"{baseURL}v2/portal/fleets",
        f"{fleetType}",
        f"?fields=_id%20name%20assets",
        f"&populate%5Bpath%5D=vios",
        f"&populate%5Bselect%5D=type%20name=Metrolinx+ADL+Electric+45%20vid%20group%20vin%20active%20assetType%20type_old",
        f"&filtered=true"
    ]

    
    req = getRequest(URL_list)
    return req
# ---------------------------------
def getDM1():
    """"
    https://dashboard.viriciti.com/api/v1/messages/diagnostic-message
    ?vids%5B0%5D=adl_004
    &query=%7B%22onGoing%22%3Atrue%7D

    https://dashboard.viriciti.com/api/v1/messages/diagnostic-message
    ?query=%7B%22onGoing%22%3Atrue%7D
    """
    return

def getIncidents():
    """
    https://dashboard.viriciti.com/api/v1/incidents
    ?limit=20
    &skip=0
    &sort%5Bstart.time%5D=-1
    &query=%7B%22start.time%22%3A%7B%22%24gte%22%3A1 672549200000 %2C%22%24lt%22%3A 1682913600000 %7D%7D
    """
    return

# ---------------------------------
# TODO: automate payload: filter for single veh and fleet (i.e. diesel or electric)
def getFleetStatus():
    global cookies

    # TODO: build payload: get all fleet or specific fleet
    # --- List of labels: labels_list
    # ---- Buid dict of vid: labels_list
    payload = {"adl_003":
                    ["gps_filter","soc_filtered","fuel_level","energetic_state","alive"],
                "adl_004":
                    ["gps_filter","soc_filtered","fuel_level","energetic_state","alive"],
                "adl_005":
                    ["gps_filter","soc_filtered","fuel_level","energetic_state","alive"],
                "adl_006":["gps_filter","soc_filtered","fuel_level","energetic_state","alive"]
                }
    URL = "https://dashboard.viriciti.com/api/v1/viostate"
    resp = postRequest(URL, payload)
    return resp



def getRouteLog (
        start_dt=1672549200000,
        end_dt=1683863999999,
        vid= "adl_005",
        time_res=6,
        time_res_unit="hours"
        ):
    """ 
    GET request at viriciti endpoint to get "Route Info"
    Time in service	01:36 h   ["time_inservice"]["delta"]
    Time driving	00:49 h ["time_driven"]["delta"]
    Battery used	11.5 %["soc_used"["delta"]]
    Distance	19.2 km ["odo_reference"]["delta"]
    Energy used in service	51.83 kWh ["energy_inservice"]["delta"]
    Energy regenerated	8.23 kWh["energy_recovered"]["delta"]
    
    Function that gets data from :
    https://dashboard.viriciti.com/vio/adl_006/route_log
    
    """
    global baseURL

    # increment
        # route info 
    URL_list = [
                    f"{baseURL}v2/delta/multilabel/{vid}?",
                    f"labels=time_inservice&",
                    f"labels=energy_inservice&",
                    f"labels=soc_used&",
                    f"labels=odo_reference&",
                    f"labels=energy_recovered&",
                    f"labels=time_driven&",
                    f"labels=fuel_used_inservice&",
                    f"labels=hydrogen_used_inservice&",
                    f"start={start_dt}&",
                    f"end={end_dt}"
                ]

    req = getRequest(URL_list)
    return req
    

def getRouteLogGraphs(
            vid,
            start_dt,
            end_dt,
            t_step,
            t_step_unit,
            time_type="first",
            analysis = "ccvs1.wheel_based_vehicle_speed"
                    ):
    """
    Analysis - soc - SOC used
    Analysis - energy - Energy used in service
    Vehicle - Wheel Based Vehicle Speed

    """
    global baseURL

    URL_list = [
                f"{baseURL}v1/time/{vid}",
                f"?page=1&time%5Bstart%5D={start_dt}",
                f"&time%5Bend%5D={end_dt}",
                f"&time%5Bstep%5D%5B0%5D={t_step}",
                f"&time%5Bstep%5D%5B1%5D={t_step_unit}",
                f"&time%5Btype%5D={time_type}",
                f"&label={analysis}"
                ]
    
    req = getRequest(URL_list)
    return req