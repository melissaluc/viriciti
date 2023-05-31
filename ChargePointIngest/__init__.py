# Starter code

import helpers
import math
import pandas as pd
import os
import logging
import re
import json

from datetime import date, datetime, timedelta
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)

#  Functions ==========================
def TimeAnalysisData_df (label, vid_dict, start_dt, end_dt, vtype):
    """
    Construct df from 
    """

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
                                label=label
                            )
                if len(resp)>0:
                    page_num+=1
                    data_df = pd.DataFrame(resp)
                    data_df["fleet"] = vtype
                    data_df["vehID"] =v
                    # if 'speed' not in label:
                    #     data_df.drop(data_df[data_df['value'] == 0].index, inplace = True)
                    if 'gps' in label:
                        data_df[['lat','lon']] = data_df['value'].str.split('|',expand=True)
                        data_df.drop(columns = ['value'], inplace=True)
                    data_df.astype({
                        "fleet":str, 
                        "value":"float64",
                        "vehID":int,
                        })
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
    try:
        time_df = pd.concat(time_data_list,ignore_index=True)
        time_df["time"] = time_df["time"]/1000
        time_df["time"] = pd.to_datetime(time_df["time"]
                                        .apply(lambda x: math.trunc(x)), unit='s')
        print(time_df)
        
    except Exception as e:
        print(e)

   


# ============GET report analyses per vehicle =========================
def getReportAPI_df(vid, vid_name_dict, analysis_name, start_dt, end_dt,period_int,period, t_res):
    resp_data = helpers.getReportsAPI(  
                        vid,
                        analysis_name,
                        start_dt,
                        end_dt,
                        period_int,
                        period,
                        t_res
                    )
    analyses_data_list = []
    if len(resp_data)>1:
        data = pd.DataFrame(resp_data)
        data["vehID"] = vid_name_dict[vid] 
        analyses_data_list.append(data)
        df = pd.concat(analyses_data_list)
        
        df_ = df.mask(df == " ").dropna().head().reset_index()
        # print(df_[0])
 
        # if analysis_name == 'analyses.calculated_odo':
        #     df_.to_csv("test.csv")
        expand_cols_list = ([i for i in df_.columns if isinstance(df_[i][0],dict)])
  

        print(expand_cols_list)
    
        for col in expand_cols_list:
            df = pd.concat([df, df[col]
                            .apply(pd.Series)
                            .add_prefix(f'{col}_')], axis=1).drop(col, axis='columns')
  

        print(df)
        return df

#  Main ==========================

def main(start_dt, end_dt, vtype, period_int, period, t_res):


    # ============GET fleet info =========================
    # Fleet info is taken from api endpoint
    # TODO: handle vtype Diesel & Electric

    fleet = helpers.getActiveFleet(vtype)["vios"]
    assets = helpers.getAssets()


    vid_dict ={}
    vid_name_dict = {}
    for asset in assets:
        for f in fleet:
            if asset["vid"] == f.get("vid",None):
                vid_dict[asset["name"]] = asset["vid"]
                vid_name_dict[asset["vid"]] = asset["name"]

    #  ==== REPORT ANALYSES =======
    analysis_keys = [
        "Performance", 
        "Energy", 
        "State of Charge", 
        "Time", 
        "Fuel Performance", 
        "Fuel"
        ]

    analysis_dict = helpers.keys_reader("report_analyses.json",analysis_keys)
    # vid = vid_dict.get('4001')
    for vid1, vid2 in vid_dict.items():
        for key1 in analysis_dict:
            print(f"||  {key1}  ||")
            for key2 in analysis_dict[key1]:
                analysis_name = analysis_dict[key1][key2]
                print(f"--------{key2}--------")
            
                getReportAPI_df(vid2, vid_name_dict, analysis_name, start_dt, end_dt,period_int,period, t_res)


    #  ==== TIME ANALYSES =======
    time_analysis_dict = helpers.keys_reader("time_analyses.json")

    time_analyses_df_dict = {}
    for key, label in time_analysis_dict.items():
        print(key)
        time_analyses_df_dict[key] = TimeAnalysisData_df (label, vid_dict, start_dt, end_dt, vtype)
        print("=========")

    # Get the current status of all vehicles real-time
    # time | energetic_state | gps_filter | soc_filtered |  fuel_level
    # print(helpers.getFleetStatus())


if __name__ == "__main__":
    main()
    """
    Return dict of df
    """
