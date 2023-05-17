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




# Set up params to pass
currentTIME = datetime.now().strftime("%H:%M:%S")
currentHOUR = datetime.now().strftime("%H")
currentDATE = date.today().strftime("%d/%m/%Y")

period_int = 1
period = "day" 
t_res = "seconds"
start_dt = 1672635600000
end_dt = 1683777600000

# =========== DYNAMIC datetime used to generate weekly reporting ========
# dt_start = 10
# dt_end = 1
# start_dt = int((datetime.now()-timedelta(days=dt_start)).timestamp())*(1000)
# end_dt = int((datetime.now()-timedelta(days=dt_end)).timestamp())*(1000)



# ============GET fleet info =========================
# Fleet info is taken from api endpoint
# TODO: handle vtype Diesel & Electric
vtype = "Electric"
fleet = helpers.getActiveFleet(vtype)["vios"]
assets = helpers.getAssets()


vid_dict ={}
vid_name_dict = {}
for asset in assets:
    for f in fleet:
        if asset["vid"] == f.get("vid",None):
            vid_dict[asset["name"]] = asset["vid"]
            vid_name_dict[asset["vid"]] = asset["name"]


# ============GET alert data =========================

# ============GET report analyses per vehicle =========================
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


# # ============GET | GPS | Speed | Energy In-serivce | SOC Used | per vehicle =========================
# # GET gps location for each vehicle in the fleet
# # TODO: conisder parallelism or map func vid_dict["Electric"], vid_dict["Diesel"]

time_analysis_dict =  {
    "soc_used":"analyses.soc_used",
    "energy_inservice":"analyses.energy_inservice",
    "gps":"analyses.gps_filter",
    "speed":"ccvs1.wheel_based_vehicle_speed",
}


time_data_list = []
for v in vid_dict:
    page_num = 1
    while page_num != None:
        try: 
            resp = helpers.getTimeAnalysis(
                            vid_dict[v],
                            start_dt,
                            end_dt,
                            page = page_num,
                            label="analyses.energy_inservice"
                        )
            if len(resp)>0:
                page_num+=1
                data_df = pd.DataFrame(resp)
                data_df["fleet"] = vtype
                data_df["vehID"] =v
                # data_df[['lat','lon']] = data_df['value'].str.split('|',expand=True)
                # data_df.drop(columns = ['value'], inplace=True)
                time_data_list.append(data_df)
            else:
                page_num = None
                break
        except Exception as e:
            break

            # TODO: Testing
            # print(data,"\n================\n")
            # with open('gps_data_dump.txt', 'a', encoding='utf-8') as f:
            #     f.write(f"{str(data)}\n")

time_df = pd.concat(time_data_list,ignore_index=True)
time_df["time"] = pd.to_datetime(time_df["time"]/1000, unit='s')
print(time_df)

print(helpers.getFleetStatus())