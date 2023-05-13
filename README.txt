|| ViriCiti ||

Manage Account
https://portal.viriciti.com/

Documentation
https://viricitihelp.zendesk.com/hc/en-us'

Monitor Fleet
https://dashboard.viriciti.com/



Get list of assets:
Fleets 
https://dashboard.viriciti.com/api/v1/report/adl_003?
labels%5B0%5D=energy_used&
labels%5B1%5D=odo_reference&
time%5Bstart%5D=1683777600000&
time%5Bend%5D=1683863999999&
time%5Bperiod%5D%5B0%5D=1&
time%5Bperiod%5D%5B1%5D=day&
time%5Bresolution%5D=hour&
time%5Btimezone%5D=America%2FToronto

https://dashboard.viriciti.com/api/v1/report/adl_003?
labels=efficiency_cur_day&
time%5Bstart%5D=1682568000000&
time%5Bend%5D=1683777600000&
time%5Bperiod%5D%5B0%5D=1&
time%5Bperiod%5D%5B1%5D=day&
time%5Bresolution%5D=hour&
time%5Btimezone%5D=America%2FToronto


https://dashboard.viriciti.com/api/v1/report/adl_006?
labels=odo_reference&
time%5Bstart%5D=1682568000000&
time%5Bend%5D=1683777600000&
time%5Bperiod%5D%5B0%5D=1&
time%5Bperiod%5D%5B1%5D=day&
time%5Bresolution%5D=hour&
time%5Btimezone%5D=America%2FToronto

ALL VEH ALERTS
https://dashboard.viriciti.com/api/v1/messages/diagnostic-message?
query=%7B%22onGoing%22%3Atrue%7D

QUERY ALERT FOR VEH
https://dashboard.viriciti.com/api/v1/messages/diagnostic-message?
vids%5B0%5D=adl_005&vids%5B1%5D=adl_006&query=%7B%22onGoing%22%3Atrue%7D



POST GET GPS LOCATION?
"https://dashboard.viriciti.com/api/v1/viostate", 
payload = {
            {
            "adl_005":["gps_filter","soc_filtered","fuel_level","energetic_state","alive"],
            "adl_006":["gps_filter","soc_filtered","fuel_level","energetic_state","alive"]
            },
            "headers": {
                         "content-type": "application/json",
            }
}


{"adl_005":["gps_filter","soc_filtered","fuel_level","energetic_state","alive"],
"adl_006":["gps_filter","soc_filtered","fuel_level","energetic_state","alive"]}



GET for Report
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.charge_cycles&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.average_inservice_speed&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.average_speed&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.efficiency_cur_day&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.efficiency_cur_day_driving&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.efficiency_cur_day_inservice&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.calculated_odo&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.recuperation_rate_cur_day&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.rel_time_in_area&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.rel_distance_in_area&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.fuel_used_per_km_cur_day&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.fuel_used_inservice_per_km_cur_day&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=vdhr.total_vehicle_distance&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.energy_charged&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.energy_consumed&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.energy_driven&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.energy_idled&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.energy_inservice&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.energy_not_inservice&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.energy_recovered&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.energy_used&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.odo_reference&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.soc_charged&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.charging_counter&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.soc_used&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.soc_used_driving&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.soc_used_idling&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.soc_used_inservice&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.soc_used_not_inservice&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.time_charged&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.time_consumed&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.time_driven&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.time_idled&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.time_inservice&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.time_not_inservice&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.time_in_area&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.time_driving&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.distance_in_area&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.fuel_used&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.time_used&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.fuel_used_driving&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.fuel_used_idling&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.fuel_used_inservice&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto
https://dashboard.viriciti.com/api/v1/report/adl_006?labels%5B0%5D=analyses.fuel_used_not_inservice&time%5Bstart%5D=1672549200000&time%5Bend%5D=1683863999999&time%5Bperiod%5D%5B0%5D=1&time%5Bperiod%5D%5B1%5D=week&time%5Bresolution%5D=hour&time%5Btimezone%5D=America%2FToronto



|| Performance ||
Average Speed
Average Speed in service
Calculated ODO
Charge Cycles
Consumption driving
Consumption in service
Consumption overall
Distance driven
Distance driven in area
Number of charging sessions
ODO
Regeneration rate
Relative distance driven in area


|| Energy ||
Energy charged
Energy consumed driving
Energy driven
Energy idled
Energy regenerated driving
Energy used
Energy used in service
Energy used not in service


|| State of Charge ||
SOC charged
SOC used
SOC used driving
SOC used idling
SOC used in service
SOC used not in service


|| Time ||
Relative time in area
Time charging
Time driving
Time driving consuming
Time idling
Time in area
Time in service
Time not in service
Time using
Time driven ***

|| Fuel Performance ||
Fuel used in service per km/mi current day
Fuel used per km/mi current day


|| Fuel ||
Fuel used
Fuel used driving
Fuel used idling
Fuel used in service
Fuel used not in service




Diagnostic Message
https://dashboard.viriciti.com/api/v1/messages/diagnostic-message?vids%5B0%5D=adl_004&query=%7B%22onGoing%22%3Atrue%7D
[{"vid":"adl_004","messages":[{"_id":"645e216b3025b86f8f97eca8","message":{"spn":"520229","occurence":126,"fmi":"5","description":"Unknown proprietary message","priority":"Low"},"source":49,"firstOccurence":1683890538826,"lastOccurence":1683907631832,"onGoing":true,"vid":"adl_004","partName":"Cab Controller - Primary"},{"_id":"645e64243025b86f8f97ed07","message":{"spn":"520209","fmi":"5","occurence":126,"description":"Unknown proprietary message","priority":"Low"},"source":49,"firstOccurence":1683907619958,"lastOccurence":1683907631832,"onGoing":true,"vid":"adl_004","partName":"Cab Controller - Primary"},{"_id":"645e642c3025b86f8f97ed09","message":{"spn":"929","occurence":127,"fmi":"12","description":"Tire Location - Failure","priority":"High"},"source":51,"firstOccurence":1683907627981,"lastOccurence":1683907627981,"onGoing":true,"vid":"adl_004","partName":"Tire Pressure Controller"}]}]


ccvs1.wheel_based_vehicle_speed
page: 1
time[start]: 1683777600000
time[end]: 1683864000000
time[step][0]: 30
time[step][1]: seconds
time[type]: first
label: ccvs1.wheel_based_vehicle_speed
https://dashboard.viriciti.com/api/v1/time/adl_004?page=1&time%5Bstart%5D=1683777600000&time%5Bend%5D=1683864000000&time%5Bstep%5D%5B0%5D=30&time%5Bstep%5D%5B1%5D=seconds&time%5Btype%5D=first&label=ccvs1.wheel_based_vehicle_speed


analyses.gps_filter
page: 1
time[start]: 1683777600000
time[end]: 1683864000000
time[step][0]: 30
time[step][1]: seconds
time[type]: first
label: analyses.gps_filter
https://dashboard.viriciti.com/api/v1/time/adl_004?page=1&time%5Bstart%5D=1683777600000&time%5Bend%5D=1683864000000&time%5Bstep%5D%5B0%5D=30&time%5Bstep%5D%5B1%5D=seconds&time%5Btype%5D=first&label=analyses.gps_filter


https://dashboard.viriciti.com/api/v2/delta/multilabel/adl_004?labels=time_inservice&labels=energy_inservice&labels=soc_used&labels=odo_reference&labels=energy_recovered&labels=time_driven&labels=fuel_used_inservice&labels=hydrogen_used_inservice&start=1683777600000&end=1683864000000
labels: time_inservice
labels: energy_inservice
labels: soc_used
labels: odo_reference
labels: energy_recovered
labels: time_driven
labels: fuel_used_inservice
labels: hydrogen_used_inservice
start: 1683777600000
end: 1683864000000
{"time_inservice":{"start_point":{"time"drogen_used_inservice":{}:"2023-05-11T09:16:21.097000+00:00","value":14147860255},"end_point":{"time":"2023-05-12T02:50:09.240000+00:00","value":14194907012},"delta":47046757,"interval_coverage":0.7318072106481481},"energy_inservice":{},"soc_used":{},"odo_reference":{"start_point":{"time":"2023-05-11T09:16:25.873000+00:00","value":187086.055},"end_point":{"time":"2023-05-12T02:48:52.410000+00:00","value":187644.635},"delta":558.5800000000163,"interval_coverage":0.7308626967592593},"energy_recovered":{},"time_driven":{},"fuel_used_inservice":{"start_point":{"time":"2023-05-11T09:16:21.097000+00:00","value":78497.843054},"end_point":{"time":"2023-05-12T02:49:10.236000+00:00","value":78744.792447},"delta":246.9493930000026,"interval_coverage":0.7311242939814815},"hydrogen.."}


https://dashboard.viriciti.com/api/v1/viostate
{"adl_004":{"analyses.fuel_used_inservice_per_km_cur_day":{"time":1683910578366,"value":0.400656},"analyses.fuel_used_per_day":{"time":1683910578366,"value":152.688585},"analyses.odo_reference_per_day":{"time":1683910577842,"value":379.555},"at1_t1_i1.aftrtrtmnt1_dsl_exhst_fld_tank_level":{"time":1683910574906,"value":100},"ccvs1.wheel_based_vehicle_speed":{"time":1683910578422,"value":44.78125},"dd1.fuel_level1":{"time":1683910577468,"value":86.4},"dd1.washer_fluid_level":null,"eec1.engine_speed":{"time":1683910578368,"value":1574.375},"efl_p1.engine_coolant_level1":{"time":1683910578207,"value":100},"efl_p1.engine_oil_level":null,"energetic_state":{"time":1683910578422,"value":3},"etc2.transmission_current_gear":{"time":1683910574301,"value":3},"gps_filter":{"time":1683910577969,"value":"44.10610580444336|-79.12383270263672"},"nr_satellites":null,"soc_filtered":null,"trf1.transmission_oil_level1":null,"vdhr.total_vehicle_distance":{"time":1683910577842,"value":380714.685}
payload = {"adl_004":["nr_satellites","etc2.transmission_current_gear","ccvs1.wheel_based_vehicle_speed","vdhr.total_vehicle_distance","analyses.odo_reference_per_day","eec1.engine_speed","analyses.fuel_used_per_day","analyses.fuel_used_inservice_per_km_cur_day","dd1.fuel_level1","efl_p1.engine_oil_level","efl_p1.engine_coolant_level1","trf1.transmission_oil_level1","at1_t1_i1.aftrtrtmnt1_dsl_exhst_fld_tank_level","dd1.washer_fluid_level","soc_filtered","energetic_state","gps_filter"]}

payload ={"adl_003":["online_status"],"adl_004":["online_status"],"adl_005":["online_status"],"adl_006":["online_status","alive","nr_satellites","analyses.soc_filtered","analyses.estimated_range_inservice","analyses.estimated_time_inservice","analyses.energetic_state","analyses.power","ccvs1.wheel_based_vehicle_speed","analyses.calculated_odo","analyses.odo_reference_per_day","analyses.energy_used_per_day","analyses.energy_charged_per_day","analyses.efficiency_cur_day_inservice","analyses.efficiency_cur_km_inservice","hves1_d1.hves1_voltage_level","hves1_d1.hves1_current","soc_filtered","energetic_state","gps_filter"]}


labels[0]: analyses.soc_used
time[start]: 1683864000000
time[end]: 1683950399999
time[period][0]: 1
time[period][1]: day/week/month/year
time[resolution]: hour
time[timezone]: America/Toronto




[
    {'label': 'analyses.fuel_used_inservice', 
        'time': 1672635600000, 
        'diff': {'time': 0, 'value': 0}, 
        'count': 0, 
        'length': 0
    }, 
    {'label': 'analyses.fuel_used_inservice', 'time': 1673240400000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1673845200000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1674450000000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1675054800000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1675659600000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1676264400000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1676869200000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1677474000000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1678078800000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1678680000000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1679284800000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1679889600000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1680494400000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1681099200000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1681704000000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1682308800000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1682913600000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}, {'label': 'analyses.fuel_used_inservice', 'time': 1683518400000, 'diff': {'time': 0, 'value': 0}, 'count': 0, 'length': 0}
]