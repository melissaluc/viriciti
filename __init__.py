import ChargePointIngest as CP_ingest
from datetime import date, datetime, timedelta
import logging
import CADAVL



# Set up params to pass
currentTIME = datetime.now().strftime("%H:%M:%S")
currentHOUR = datetime.now().strftime("%H")
currentDATE = date.today().strftime("%d/%m/%Y")

# Params
period_int = 1
period = "day" 
t_res = "seconds"
start_dt = 1672635600000
# end_dt = 1683777600000


# =========== DYNAMIC datetime used to generate weekly reporting ========
# dt_start = 10
dt_end = 0
# start_dt = int((datetime.now()-timedelta(days=dt_start)).timestamp())*(1000)
end_dt = int((datetime.now()-timedelta(days=dt_end)).timestamp())*(1000)


# Get EV trip data

block_data_df = CADAVL.main()

# ============GET fleet info =========================
# Fleet info is taken from api endpoint
# TODO: handle vtype Diesel & Electric
vtype = "Electric"
# CP_ingest.main(start_dt, end_dt, vtype, period_int, period, t_res)