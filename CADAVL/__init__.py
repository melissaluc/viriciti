import urllib
import datetime
from datetime import datetime
import pandas as pd
import sqlalchemy as sqlal
from sqlalchemy import create_engine
import logging
from helpers.constants import ORACLE_DB_HOSTNAME, ORACLE_DB_PASSWORD, ORACLE_DB_USERNAME,ORACLE_DB_PORTNUM,ORACLE_DB_SERVICENAME



def main(start_dt=None, end_dt=None):
    start_dt_str=datetime.utcfromtimestamp(start_dt/1000).strftime("%d-%b-%Y")
    end_dt_str=datetime.utcfromtimestamp(end_dt/1000).strftime("%d-%b-%Y")

    if start_dt==None and end_dt==None:
        date_filter =""
    else:
        date_filter = f"""
        AND OPD_DATE BETWEEN '{start_dt_str}' and '{end_dt_str}'
        """

    engine = create_engine(f"oracle+cx_oracle://{ORACLE_DB_USERNAME}:{ORACLE_DB_PASSWORD}@{ORACLE_DB_HOSTNAME}:{ORACLE_DB_PORTNUM}/?service_name={ORACLE_DB_SERVICENAME}")

    EV_Trips_df = pd.read_sql_query(
        f"""
          SELECT *
        FROM
        (SELECT 
            vtrip.OPD_DATE,
            vtrip.VEHICLE_ID,
            vtrip.METERS,
            vtrip.ACT_DEP_TIME,
            vtrip.NOM_DEP_TIME,
            vtrip.NOM_END_TIME,
            vtrip.ACT_END_TIME,
            vtrip.LINE_ID,
            vtrip.TRIP_ID,
            vtrip.PATTERN_ID,
            vtrip.PATTERN_DIRECTION,
            vtrip.TRIP_TYPE,
            vtrip.PATTERN_QUALITY,
            vtrip.APC_QUALITY,
            vtrip.BLOCK_ID,
            vtrip.PASSENGER_DATA,
            vtrip.TIME_GRP_ID,
            vtrip.TRIP_CODE,
            vtrip.IS_ADDITIONAL_TRIP,
            vtrip.TRIP_ROLE,
            vtrip.TRIP_SUBROLE,
            vtrip.TRIP_PURPOSE,
            block.LONG_NAME,
            patt.NAME_SUFFIX
        FROM MX_REPORTS.VEH_TRIP vtrip
        LEFT JOIN MX_REPORTS.NOM_BLOCK block
        ON block.BLOCK_ID = vtrip.BLOCK_ID
        LEFT JOIN MX_REPORTS.NOM_PATTERN patt
        ON patt.PATTERN_ID = vtrip.PATTERN_ID AND patt.LINE_ID = vtrip.LINE_ID)
        WHERE VEHICLE_ID IN ('4000','4001'){date_filter}

        """
        , engine).reset_index()
    

    EV_Trips_df= EV_Trips_df.astype({'long_name':str,'line_id':str})

    # print(EV_Trips_df)
    return EV_Trips_df



if __name__ == "__main__":
    main()
    """
    Return dict of df
    """
