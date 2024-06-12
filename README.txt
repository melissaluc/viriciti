** Electric Vehicle Bus Battery Monitoring ETL **

The Python-based ETL pipeline is scheduled to run daily at 9:00 AM through the Windows Task Scheduler and a bat file. Its primary objective is to fetch vendor data (ChargePoint) regarding electric vehicle performance and conduct calculations to update an engineer's Excel tracking sheet. This pipeline was developed to seamlessly integrate with existing systems like the vehicle dispatch system (CAD/AVL) via Oracle Database. By leveraging trip start-end time data, it accurately computes performance metrics within trip timeframes.

Key features of the pipeline include:
Interaction with CAD/AVL System: The pipeline interacts with the CAD/AVL system via Oracle, specifically querying electric vehicles (EVs) in service for the day. The retrieved dataframe, containing start-end times for trips/service blocks, is utilized to extract vendor data for the day, eliminating the need for manual communication regarding vehicle service departures.
Data Extraction: CAD/AVL data is utilized to extract vendor-collected EV data. This involves querying for each vehicle and providing start-end times to evaluate performance exclusively during service.
Output to Performance Tracking Sheet: The pipeline generates a CSV file utilizing vendor data to compile specific metrics tracked by the engineer. These metrics are instrumental in reporting on the performance of EVs in service.


Due to the absence of explicit APIs, the pipeline employs web scraping techniques to interact with the UI and internal APIs for data retrieval. This automation streamlines a labor-intensive process previously managed by a team of three individuals. Specifically, two engineers manually filtered route data based on dispatch personnel reports and recorded the data into an Excel spreadsheet.

The metrics collected from Chargepoint encompass temperature, state of charge, odometer reading, energy consumption, idling time, charging, driving duration, regeneration rate, charging events, and vehicle speed. 








































-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|| ViriCiti ||

Manage Account
https://portal.viriciti.com/

Documentation
https://viricitihelp.zendesk.com/hc/en-us'

Monitor Fleet
https://dashboard.viriciti.com/






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


https://dashboard.viriciti.com/api/v1/viostate POST to get Status of vehicle
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


|| DASHBOARD ||
|| PERFORMANCE ||
The electric buses are charged with 0% renewable energy. The amount of emissions produced per kWh is set to:
0.593	kg	CO₂
0.2	g	NOx
5 x 10⁻³	g	PM
The non-electric bus has a consumption rate of 35 l / 100 km. The amount of emissions per liter is set to:
2.642	kg	CO₂
4.44	g	NOx
111 x 10⁻³	g	PM

UTILIZATION: Time in service vs. time not in service vs charging time
ENERGY: energy used in service vs energy not used in service vs energy charged
CONSUMPTION: consump overall per day v consump in service per day v regeneration rate per day
SOC used
Average Speed

|| ROUTE LOG ||
https://dashboard.viriciti.com/api/v2/delta/multilabel/adl_006
?labels=time_inservice
&labels=energy_inservice
&labels=soc_used
&labels=odo_reference
&labels=energy_recovered
&labels=time_driven
&labels=fuel_used_inservice
&labels=hydrogen_used_inservice
&start=1680667200000
&end=1680753600000

---------------------------------------------------------------------------------------------
SAMPLE RESPONSE DATA
---------------------------------------------------------------------------------------------
Route	
Driver	
Start time	05-04-2023 00:00
End time	06-04-2023 00:00
Time in service	01:36 h<<--------------------------------------------------------------------------  ["time_inservice"]["delta"]
Time driving	00:49 h<<-------------------------------------------------------------------------- ["time_driven"]["delta"]
Battery used	11.5 %<<--------------------------------------------------------------------------["soc_used"["delta"]]
Distance	19.2 km<<-------------------------------------------------------------------------- ["odo_reference"]["delta"]
Energy used in service	51.83 kWh<<-------------------------------------------------------------------------- ["energy_inservice"]["delta"]
Energy regenerated	8.23 kWh<<-------------------------------------------------------------------------- ["energy_recovered"]["delta"]
Average speed	23.2 km/h
Consumption in service	2.71 kWh/km 

---------------------------------------------------------------------------------------------
|| DIAGNOSTIC MESSAGES ||
Diagnostic Message
FOR SINGLE VEH
https://dashboard.viriciti.com/api/v1/messages/diagnostic-message
?vids%5B0%5D=adl_004
&query=%7B%22onGoing%22%3Atrue%7D

FOR FLEET
https://dashboard.viriciti.com/api/v1/messages/diagnostic-message?query=%7B%22onGoing%22%3Atrue%7D

ALERTS
https://dashboard.viriciti.com/api/v1/messages/message?query=%7B%22onGoing%22%3Atrue%7D

[{"vid":"adl_004","messages":[{"_id":"645e216b3025b86f8f97eca8","message":{"spn":"520229","occurence":126,"fmi":"5","description":"Unknown proprietary message","priority":"Low"},"source":49,"firstOccurence":1683890538826,"lastOccurence":1683907631832,"onGoing":true,"vid":"adl_004","partName":"Cab Controller - Primary"},{"_id":"645e64243025b86f8f97ed07","message":{"spn":"520209","fmi":"5","occurence":126,"description":"Unknown proprietary message","priority":"Low"},"source":49,"firstOccurence":1683907619958,"lastOccurence":1683907631832,"onGoing":true,"vid":"adl_004","partName":"Cab Controller - Primary"},{"_id":"645e642c3025b86f8f97ed09","message":{"spn":"929","occurence":127,"fmi":"12","description":"Tire Location - Failure","priority":"High"},"source":51,"firstOccurence":1683907627981,"lastOccurence":1683907627981,"onGoing":true,"vid":"adl_004","partName":"Tire Pressure Controller"}]}]

|| INCIDENTS ||
https://dashboard.viriciti.com/api/v1/incidents
?limit=20
&skip=0
&sort%5Bstart.time%5D=-1
&query=%7B%22start.time%22%3A%7B%22%24gte%22%3A1 672549200000 %2C%22%24lt%22%3A 1682913600000 %7D%7D


TO GET FLEET Status - OPERATIONS
ONLINE | TITLE | STATE | SOC | REMAINING RANGE | REMAINING TIME
POST
https://dashboard.viriciti.com/api/v1/viostate
{"adl_005":
["analyses.soc_used_inservice_per_day",
"analyses.energy_inservice_per_day",
"analyses.time_inservice_per_day",
"analyses.soc_used_not_inservice_per_day",
"analyses.energy_not_inservice_per_day",
"analyses.time_not_inservice_per_day",
"analyses.odo_reference_per_day",
"analyses.average_inservice_speed",
"analyses.efficiency_cur_day_inservice",
"analyses.soc_charged_per_day",
"analyses.soc_used_per_day",
"analyses.energy_used_per_day",
"analyses.time_used_per_day",
"analyses.efficiency_cur_day",
"analyses.energy_idled_per_day",
"analyses.time_idled_per_day",
"analyses.energy_driven_per_day",
"analyses.time_driven_per_day",
"analyses.efficiency_cur_day_driving",
"analyses.energy_consumed_per_day",
"analyses.time_consumed_per_day",
"analyses.energy_recovered_per_day",
"analyses.time_recovered_per_day",
"analyses.recuperation_rate_cur_day",
"analyses.energy_charged_per_day",
"analyses.time_charged_per_day",
"analyses.energy_gained_fastcharging_per_day",
"analyses.time_fastcharging_per_day",
"analyses.energy_gained_slowcharging_per_day",
"analyses.time_slowcharging_per_day"]
}

response[vid][key][value]

POST TO get fleet postion & status
https://dashboard.viriciti.com/api/v1/viostate
{"adl_003":
["gps_filter","soc_filtered",
"fuel_level","energetic_state",
"alive"],
"adl_004":
["gps_filter","soc_filtered",
"fuel_level",
"energetic_state",
"alive"],
"adl_005":
["gps_filter","soc_filtered","fuel_level","energetic_state","alive"],"adl_006":["gps_filter","soc_filtered","fuel_level","energetic_state","alive"]}
