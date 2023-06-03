import pandas as pd
import geopandas as gpd
import ChargePointIngest as CP_ingest
from datetime import date, datetime, timedelta
import logging
import CADAVL
import GTFSIngest
import logging

from functools import reduce   

logging.basicConfig(
    filename="output.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
    datefmt="%Y-%m-%d %I:%M:%S%p",
)


# Set up params to pass
currentTIME = datetime.now().strftime("%H:%M:%S")
currentHOUR = datetime.now().strftime("%H")
currentDATE = date.today().strftime("%d/%m/%Y")


# Params
period_int = 1
period = "day" 
t_res = "seconds"

# TODO: Test
# start_dt = 1672549200000
# end_dt = 1686542400000


# =========== DYNAMIC datetime used to generate weekly reporting ========
dt_start = 50
dt_end = 0
# str date for querying
start_dt = int((datetime.now()-timedelta(days=dt_start)).timestamp())*(1000)
if dt_end > 0:
    end_dt = int((datetime.now()-timedelta(days=dt_end)).timestamp())*(1000)
else:
    end_dt = int((datetime.now()).timestamp())*(1000)

print(end_dt)


# Get EV trip data

# block_data_df = CADAVL.main(start_dt,end_dt)

gtfs_df = GTFSIngest.main()


# ============GET fleet info =========================
# Fleet info is taken from api endpoint
# TODO: handle vtype Diesel & Electric
vtype = "Electric"
cp_df_dict = CP_ingest.main(start_dt, end_dt, vtype, period_int, period, t_res)
gps_df = cp_df_dict.get('time_analysis').get('gps')

gps_gdf = gpd.GeoDataFrame(gps_df, geometry=gpd.points_from_xy(x=gps_df.lon, y=gps_df.lat))
gps_gdf.astype({'time':str}).to_file('point_location.shp')

time_analyses_df_dict = cp_df_dict.get('time_analysis')


time_analyses_df_list = []
for key, value in time_analyses_df_dict.items():
    # print(f"the key is: {key}\n{value}")
    if len(value)>0:
        time_df=value.rename(columns={'value':f'{str(key).replace(" ", "_")}'}).set_index(keys=['time','vehID'])
        time_analyses_df_list.append(time_df)
        print(time_df)

data_merge_time_analysis = reduce(lambda left, right: pd.merge(left , right, on = ["time","vehID","fleet"],how = "outer"),time_analyses_df_list)
# data_merge_time_analysis .to_csv('check_df.csv')