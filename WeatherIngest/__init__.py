import helpers
from datetime import datetime
import pandas as pd
from helpers import tz
import urllib.parse

def main(start_dt, end_dt):
    start_dt_str=datetime.utcfromtimestamp(start_dt/1000).strftime("%Y-%m-%d")
    end_dt_str=datetime.utcfromtimestamp(end_dt/1000).strftime("%Y-%m-%d")

    URL_list = [f"https://archive-api.open-meteo.com/v1/archive?",
    f"latitude=43.70&longitude=-79.42",
    f"&start_date={start_dt_str}",
    f"&end_date={end_dt_str}",
    f"&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,apparent_temperature_max,apparent_temperature_min,apparent_temperature_mean,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant",
    f"&timezone=America%2FNew_York",
    f"&timeformat=unixtime"]

    tz_convert = urllib.parse.unquote(tz)
    resp_json = helpers.getRequest(URL_list)
    data_dict = resp_json['daily']
    data_df = pd.DataFrame(data_dict)
    data_df ['time'] = pd.to_datetime(data_df["time"],unit='s').map(lambda t: t.tz_localize(tz_convert))
    


    return data_df




if __name__ == "__main__":
    main()
    """
    Return dict of df
    """