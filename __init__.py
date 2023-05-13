# Starter code

import helpers
import pandas as pd
import urllib.parse
import os
import logging
import re
import json
from datetime import date, datetime, timedelta
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)



# Get current time
currentTIME = datetime.now().strftime("%H:%M:%S")
currentHOUR = datetime.now().strftime("%H")
currentDATE = date.today().strftime("%d/%m/%Y")

# now = int((datetime.now()-timedelta(days=5)).timestamp())*(1000)


period_int = 1
period = "week" 
t_res = "hour"
start_dt = 1672635600000
end_dt = 1683777600000
# end_dt = int((datetime.now()-timedelta(days=5)).timestamp())*(1000)

# TODO: get the fleet data from endpoint
vid_dict = helpers.getActiveFleet()
print(vid_dict)
# vid_dict = {
#         "Electric":{
#                 4001:"adl_005",
#                 4000:"adl_006"
#             },
#         "Diesel":{
#                 8503:"adl_003",
#                 8507:"adl_004"
#             }
#         }

analysis_keys = [
    "Performance", 
    "Energy", 
    "State of Charge", 
    "Time", 
    "Fuel Performance", 
    "Fuel"
    ]

# analysis_dict = helpers.keys_reader("analyses.json",analysis_keys)
# analysis_name = analysis_dict["Energy"]["Energy charged"]
# vid = vid_dict["Electric"][4001]

# for key1 in analysis_dict:
#     print(f"||  {key1}  ||")
#     for key2 in analysis_dict[key1]:
#         analysis_name = analysis_dict[key1][key2]
#         print(f"--------{key2}--------")
#         resp_data = helpers.getReportsAPI(  
#                             vid,
#                             analysis_name,
#                             start_dt,
#                             end_dt,
#                             period_int,
#                             period,
#                             t_res
#                         )
#         analyses_data_list = []
#         if len(resp_data)>1:
#             data = pd.DataFrame(resp_data)
#             data["vehID"] = vid 
#             # data[['lat','lon']] = data['value'].str.split('|',expand=True)
#             # data.drop(columns = ['value'], inplace=True)

#             # TODO: Testing
#             # print(data,"\n================\n")
#             # with open('analyses_data_dump.txt', 'a', encoding='utf-8') as f:
#             #     f.write(f"{str(data)}\n")
#             analyses_data_list.append(data)
#     analyses_data = pd.concat(analyses_data_list)
#     print(analyses_data)



# GET gps location for each vehicle in the fleet
# TODO: conisder parallelism or map func vid_dict["Electric"], vid_dict["Diesel"]


def getGPSdata ():
    # Iterate for one vehicle
    gps_data_list = []
    page_num = 1
    while page_num != None:
        try: 
            resp_data = helpers.getGPSLocation(
                            vid_dict[vtype][vid],
                            start_dt,
                            end_dt = 1683777600000,
                            page_num=page_num
                        )
            # print(resp_data)
            if len(resp_data)>1:
                data = pd.DataFrame(resp_data)
                data["Fleet"] = vtype
                data["vehID"] = vid 
                data[['lat','lon']] = data['value'].str.split('|',expand=True)
                data.drop(columns = ['value'], inplace=True)
                gps_data_list.append(data)
                page_num+=1
            else:
                page_num = None
                break
        except Exception as e:
            break



for vtype in vid_dict:

    gps_data_list = []
    for vid in vid_dict[vtype]:
        page_num = 1
        while page_num != None:
            try: 
                resp_data = helpers.getGPSLocation(
                                vid_dict[vtype][vid],
                                start_dt,
                                end_dt = 1683777600000,
                                page_num=page_num
                            )
                # print(resp_data)
                if len(resp_data)>1:
                    data = pd.DataFrame(resp_data)
                    data["Fleet"] = vtype
                    data["vehID"] = vid 
                    data[['lat','lon']] = data['value'].str.split('|',expand=True)
                    data.drop(columns = ['value'], inplace=True)
                    gps_data_list.append(data)
                    page_num+=1
                else:
                    page_num = None
                    break
            except Exception as e:
                break

                # TODO: Testing
                # print(data,"\n================\n")
                # with open('gps_data_dump.txt', 'a', encoding='utf-8') as f:
                #     f.write(f"{str(data)}\n")

gps_df = pd.concat(gps_data_list)    
print(gps_df)

# helpers.getRouteLog (
#         baseURL,
#         start_dt=1672549200000,
#         end_dt=1683863999999,
#         vid,
#         analysis,
#         time_res=6,
#         time_res_unit="hours"
#         )