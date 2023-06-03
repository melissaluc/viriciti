# Starter code

import helpers
from helpers import tz
import urllib.parse
import math
import pandas as pd
import os
import logging


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

                if isinstance(resp,list):
                    page_num+=1
                else:
                    break

            except Exception as e:
                page_num = None
                break
            
            else:
                data_df = pd.DataFrame(resp)
                data_df["fleet"] = vtype
                data_df["vehID"] =v

                if ('gps' in label) and (len(data_df)>0):
                    data_df[['lat','lon']] = data_df['value'].str.split('|',expand=True)

                    
                data_df= data_df.astype({
                    "fleet":str, 
                    "vehID":int,
                    })
                
                time_data_list.append(data_df)
                # print(len(time_data_list))
  

    
    try:
        tz_convert = urllib.parse.unquote(tz)
        time_df = pd.concat(time_data_list)
        time_df["time"] = time_df["time"]/1000
        time_df["time"] = pd.to_datetime(time_df["time"]
                                        .apply(lambda x: math.trunc(x)), unit='s').map(lambda t: t.tz_localize(tz_convert))
        # print(time_df)
        
        return time_df


    except Exception as e:
        print(e)
        return []

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

        expand_cols_list = ([i for i in df_.columns if isinstance(df_[i][0],dict)])
  

        # print(expand_cols_list)
    
        for col in expand_cols_list:
            df = pd.concat([df, df[col]
                            .apply(pd.Series)
                            .add_prefix(f'{col}_')], axis=1).drop(col, axis='columns')
  

        # print(df)
        return df

#  Main ==========================

def main(start_dt, end_dt, vtype, period_int, period, t_res,output=None):

    """
    output = 1 ==> return time data
    output = 2 ==> return reports data
    output = 3 ===> return current fleet status
    output = None ===> return all data
    """
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


    # #  ==== REPORT ANALYSES =======
    # analysis_keys = [
    #     "Performance", 
    #     "Energy", 
    #     "State of Charge", 
    #     "Time", 
    #     "Fuel Performance", 
    #     "Fuel"
    #     ]

    # analysis_dict = helpers.keys_reader("report_analyses.json",analysis_keys)

    # report_df_dict = {}
    # for vid1, vid2 in vid_dict.items():
    #     for key1 in analysis_dict:
    #         # print(f"||  {key1}  ||")
    #         for key2 in analysis_dict[key1]:
    #             analysis_name = analysis_dict[key1][key2]
    #             # print(f"--------{key2}--------")
            
    #             report_df = getReportAPI_df(vid2, vid_name_dict, analysis_name, start_dt, end_dt,period_int,period, t_res)
    #             report_df_dict[key2] =  report_df

    #  ==== TIME ANALYSES =======
    time_analysis_dict = helpers.keys_reader("time_analyses.json")

    time_analyses_df_dict = {}
    for key, label in time_analysis_dict.items():
        # print(key)
        time_analyses_df_dict[key] = TimeAnalysisData_df (label, vid_dict, start_dt, end_dt, vtype)
        # print("=========")

    # Get the current status of all vehicles real-time
    # time | energetic_state | gps_filter | soc_filtered |  fuel_level
    # fleetStatus = helpers.getFleetStatus()

    return {"time_analysis":time_analyses_df_dict}


if __name__ == "__main__":
    main()
    """
    Return dict of df
    """
