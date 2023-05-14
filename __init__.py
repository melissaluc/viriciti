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

period_int = 1
period = "day" 
t_res = "seconds"
start_dt = 1672635600000
end_dt = 1683777600000

# DYNAMIC dt
# start_dt = int((datetime.now()-timedelta(days=10)).timestamp())*(1000)
# end_dt = int((datetime.now()-timedelta(days=5)).timestamp())*(1000)



# ============GET fleet vehicle =========================
# TODO: get the fleet data from endpoint
vtype = "Electric"
fleet = helpers.getActiveFleet(vtype)["vios"]
print("fleet ---->",fleet)
assets = helpers.getAssets()
print("assets--->",assets)
print("allfleet--->",helpers.getAllFleet())

vid_dict ={}
vid_name_dict = {}
for asset in assets:
    for f in fleet:
        if asset["vid"] == f.get("vid",None):
            vid_dict[asset["name"]] = asset["vid"]
            vid_name_dict[asset["vid"]] = asset["name"]

# print(type(fleet[0].get('vios')))

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


# ============GET analyses per vehicle =========================
analysis_keys = [
    "Performance", 
    "Energy", 
    "State of Charge", 
    "Time", 
    "Fuel Performance", 
    "Fuel"
    ]

analysis_dict = helpers.keys_reader("analyses.json",analysis_keys)
# vid = vid_dict.get('4001')

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
#             data["vehID"] = vid_name_dict[vid] 
#             # data[['lat','lon']] = data['value'].str.split('|',expand=True)
#             # data.drop(columns = ['value'], inplace=True)

#             # TODO: Testing
#             # print(data,"\n================\n")
#             # with open('analyses_data_dump.txt', 'a', encoding='utf-8') as f:
#             #     f.write(f"{str(data)}\n")
#             analyses_data_list.append(data)
#     analyses_data = pd.concat(analyses_data_list)
#     print(analyses_data)


# # ============GET GPS per vehicle =========================
# # GET gps location for each vehicle in the fleet
# # TODO: conisder parallelism or map func vid_dict["Electric"], vid_dict["Diesel"]

# def getGPSdata ():
#     # Iterate for one vehicle
#     gps_data_list = []
#     page_num = 1
#     while page_num != None:
#         try: 
#             resp_data = helpers.getGPSLocation(
#                             vid_dict[vtype][vid],
#                             start_dt,
#                             end_dt = 1683777600000,
#                             page_num=page_num
#                         )
#             # print(resp_data)
#             if len(resp_data)>1:
#                 data = pd.DataFrame(resp_data)
#                 data["Fleet"] = vtype
#                 data["vehID"] = vid 
#                 data[['lat','lon']] = data['value'].str.split('|',expand=True)
#                 data.drop(columns = ['value'], inplace=True)
#                 gps_data_list.append(data)
#                 page_num+=1
#             else:
#                 page_num = None
#                 break
#         except Exception as e:
#             break

 


gps_data_list = []
for v in vid_dict:
    print(v,"\n",vid_dict)
    page_num = 1
    while page_num != None:
        try: 
            print(vid_dict[v])
            resp_data = helpers.getGPSLocation(
                            vid_dict[v],
                            start_dt,
                            end_dt,
                            page_num
                        )
            
            if len(resp_data)>0:
                data = pd.DataFrame(resp_data)
                data["fleet"] = vtype
                data["vehID"] = vid_name_dict[v] 
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
gps_df["time"] = pd.to_datetime(gps_df["time"]/1000, unit='s')
print(gps_df)

# time_data_list = []
# for v in vid_dict:
#     page_num = 1
#     while page_num != None:
#         try: 
#             resp_data =  helpers.getTimeAPI(  
#                                     vid_dict[v],
#                                     start_dt =1672549200000,
#                                     end_dt = 1683863999999,
#                                     page = page_num
#                                 )

#             if len(resp_data)>0:
#                 print("enter the if")
#                 data = pd.DataFrame(resp_data)
#                 data["fleet"] = vtype
#                 data["vehID"] = vid_name_dict[v] 
#                 time_data_list.append(data)
#                 page_num+=1
#                 print(len(time_data_list))
#             else:
#                 page_num = None
#                 break
#         except Exception as e:
#             break

# time_data = pd.concat(time_data_list)
# print(time_data)