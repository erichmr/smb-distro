# libraries
import csv
import json
from datetime import datetime
import matplotlib as plt
import pandas as pd
import pytz
import requests
import time

# variables
olist_all = []
olister_vacation = []
olister_off = []
error_box = []

count_succ = 0
count_fail = 0

ttm = datetime.now()
## print("Local:", ttm.strftime("%m/%d/%Y, %H:%M:%s"))

localtime = ttm.strftime("%m/%d/%Y %H:%M:%S")
print(localtime)


# read flat file (csv)
## read csv with data tp change
## validate errors (local)
## remove blanks fields


# pre processing conditions
## read arrays, show
## error_box handle fail executions


# post processing conditions
## calculations
# conditions


# final results
## get output data
## get output chart
## get output log (local file only)