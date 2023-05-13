# Starter code

from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions

import seleniumwire.undetected_chromedriver as uc
import requests, lxml.html
import bs4
import pandas as pd
import urllib.parse
import os
import time
import logging
import re
from datetime import date, datetime
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)

import datetime
from datetime import datetime
import calendar

options = uc.ChromeOptions()
# options.add_argument("--headless=new")
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--disable-gpu")
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.implicitly_wait(60)


URLS = {
    4000 : "https://dashboard.viriciti.com/vio/adl_006/route_log" ,
    4001 : "https://dashboard.viriciti.com/vio/adl_005/route_log"
    }

# TODO: Put in a config
username = "melissa.luc@metrolinx.com"
password = "CUgB4t9017ibkH^!"

driver.get(URLS[4000])

# Access requests via the `requests` attribute
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(username)
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(username)
time.sleep(10)
print("Login Sucessful")

# Get site cookie
cookies_list = map(lambda req: req.headers["Cookie"], driver.requests)
for cookie in cookies_list:
    if (cookie != None) and (re.match(re.compile("^web.viriciti.com="),cookie)):
        site_cookie = cookie
        print(site_cookie)
        break

# Get current time
currentTIME = datetime.now().strftime("%H:%M:%S")
currentHOUR = datetime.now().strftime("%H")
currentDATE = date.today().strftime("%d/%m/%Y")

# epoch time 1683777600000
# year/month/day/hours/minutes/seconds: milliseconds
epochstamp = datetime.now()
datetimestamp =datetime.utcfromtimestamp(epochstamp)

print(epochstamp)
start_dt = 0
end_dt = 0
vehID = {
        4001:"adl_005",
        4000:"adl_006"
        }
baseURL = "https://dashboard.viriciti.com/api/"
# increment
page = 1
analysis = ["analyses.soc_used","analyses.energy_inservice","analyses.gps_filter","ccvs1.wheel_based_vehicle_speed"]
# change once
time_res = 6
time_res_unit = "hours"
# route info 
route_info_URL = f"{baseURL}v2/delta/multilabel/{vehID}?"+"labels=time_inservice&"+"labels=energy_inservice&"+"labels=soc_used&"+"labels=odo_reference&"+"labels=energy_recovered&"+"labels=time_driven&"+"labels=fuel_used_inservice&"+"labels=hydrogen_used_inservice&"+f"start={start_dt}&"+f"end={end_dt}"

# Graph Data 
graph_URL = f"{baseURL}v1/time/{vehID}?page={page}&time%5Bstart%5D={start_dt}&time%5Bend%5D={end_dt}&time%5Bstep%5D%5B0%5D={time_res}&time%5Bstep%5D%5B1%5D={time_res_unit}&time%5Btype%5D=first&label={analysis}"
