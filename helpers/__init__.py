
import requests
import os
import json
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
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
    # USERNAME =urllib.parse.quote_plus('Melissa.Luc@metrolinx.com')
    #  PASSWORD = urllib.parse.quote_plus('CUgB4t9017ibkH^!')
    URL = "https://dashboard.viriciti.com/dashboard"
    credentials= keys_reader("config.json",["USERNAME","PASSWORD"])
    USERNAME = credentials["USERNAME"]
    PASSWORD = credentials["PASSWORD"]

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

def getRequest(URL):
    """
    Return get response as JSON
    """
    global cookies

    data_header = {
            "Cookie": cookies,
            "Content-Type": "application/json; charset=utf-8"
    }

    response = requests.get(URL, headers= data_header ,verify=False)
    if response.status_code == 200:
        res_json = response.json()
        return res_json
    



def getRouteLog (
        baseURL,
        start_dt=1672549200000,
        end_dt=1683863999999,
        vid= "adl_005",
        time_res=6,
        time_res_unit="hours"
        ):
    """ 
    GET request at viriciti endpoint to get "Route Info" and "Graphs" data\n
    baseURL : endpoint base URL\n
    start_dt:\n
    end_dt:\n
    vehID:\n
    analysis:\n
    time_res: default=6\n
    time_res_unit: default=hours\n

    Function that gets data from :
    https://dashboard.viriciti.com/vio/adl_006/route_log
    
    """
    global cookies; baseURL; 

    # increment
        # route info 
    route_info_URL_list = [
                    f"{baseURL}v2/delta/multilabel/{vehID}?",
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

    route_URL = "".join(route_info_URL_list)
    route_data = getRequest(route_URL)
    
    page = 1
    analysis = ""
    while page is not None:

        # Graph Data 
        graph_URL_list = [
                    f"{baseURL}v1/time/{vid}",
                    f"?page={page}",
                    f"&time%5Bstart%5D={start_dt}",
                    f"&time%5Bend%5D={end_dt}",
                    f"&time%5Bstep%5D%5B0%5D={time_res}",
                    f"&time%5Bstep%5D%5B1%5D={time_res_unit}",
                    f"&time%5Btype%5D=first&label={analysis}"
                    ]
        try:
            page+=1
            graph_URL = "".join(graph_URL_list)
            getRequest(graph_URL)
        except Exception as e:
            page = None
        
        return route_data 

def getAlerts ():
    """
    Function that gets data from :
    https://dashboard.viriciti.com/api/v1/messages/diagnostic-message?
    query=%7B%22onGoing%22%3Atrue%7D
    """



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
    
    URL = "".join(URL_list)
    print(URL)
    data_header = {
            "Cookie": cookies,
            "Content-Type": "application/json; charset=utf-8"
                }
    
    response = requests.get(URL, headers= data_header ,verify=False)
    if response.status_code == 200:
        res_json = response.json()
        return res_json
    else:
        return print("Could not retreive data")


def getGPSLocation(
                        vid,
                        start_dt,
                        end_dt,
                        page_num=1
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
    """
    global cookies; baseURL



    URL_list  = [
        f"{baseURL}v1/time/{vid}?",
        f"page={page_num}",
        f"&time%5Bstart%5D={start_dt}",
        f"&time%5Bend%5D={end_dt}",
        f"&time%5Bstep%5D%5B0%5D=30",
        f"&time%5Bstep%5D%5B1%5D=seconds",
        f"&time%5Btype%5D=first",
        f"&label=analyses.gps_filter",
    ]
    
    URL = "".join(URL_list)
    print(URL)
    data_header = {
            "Cookie": cookies,
            "Content-Type": "application/json; charset=utf-8"
                }
    
    response = requests.get(URL, headers= data_header,verify=False)
    if response.status_code == 200:
        res_json = response.json()
        return res_json
    else:
        return print("Could not retrieve data")



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

    
    URL = "".join(URL_list)
    print(URL)
    data_header = {
            "Cookie": cookies,
            "Content-Type": "application/json; charset=utf-8"
                }
    
    response = requests.get(URL, headers= data_header,verify=False)
    if response.status_code == 200:
        res_json = response.json()
        return res_json
    else:
        return print("Could not retrieve data")

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

    URL = "".join(URL_list)
    print(URL)

    data_header = {
        "Cookie": cookies,
        "Content-Type": "application/json; charset=utf-8"
            }
    
    response = requests.get(URL, headers= data_header,verify=False)
    if response.status_code == 200:
        res_json = response.json()
        return res_json
    else:
        return print("Could not retrieve data")

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

    
    URL = "".join(URL_list)
    print(URL)
    data_header = {
            "Cookie": cookies,
            "Content-Type": "application/json; charset=utf-8"
                }
    
    response = requests.get(URL, headers= data_header,verify=False)
    if response.status_code == 200:
        res_json = response.json()
        return res_json
    else:
        return print("Could not retrieve data")


def epochConvertTime():
    """
    Convert epochtime to normal
    """

def getTimeAPI(
                        vid,
                        start_dt,
                        end_dt,
                        page=1,
                        label = "analyses.soc_used"
                    ):
    """
    Function that gets data from :
    https://dashboard.viriciti.com/api/v1/time/adl_005
    ?page=2
    &time%5Bstart%5D=1672549200000
    &time%5Bend%5D=1684123200000
    &time%5Bstep%5D%5B0%5D=6
    &time%5Bstep%5D%5B1%5D=hours
    &time%5Btype%5D=first
    &label=analyses.soc_used
    """
    global cookies

    baseURL = "https://dashboard.viriciti.com/api/"

    URL_list  = [
        f"{baseURL}v1/time/{vid}?",
        f"page={page}",
        f"&time%5Bstart%5D={start_dt}",
        f"&time%5Bend%5D={end_dt}",
        f"&time%5Bstep%5D%5B0%5D=6",
        f"&time%5Bstep%5D%5B1%5D=hours",
        f"&time%5Btype%5D=first",
        f"&label={label}",
    ]
    
    URL = "".join(URL_list)
    print(URL)
    data_header = {
            "Cookie": cookies,
            "Content-Type": "application/json; charset=utf-8"
                }
    
    response = requests.get(URL, headers= data_header,verify=False)
    if response.status_code == 200:
        res_json = response.json()
        return res_json
    else:
        return print("Could not retrieve data")