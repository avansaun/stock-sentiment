from typing import final
import requests
import matplotlib.pyplot as plt
import json
from datetime import date

#Gets house transaction data and returns it as JSON data

baseUrl = "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com"
currDay = date.today().day
currMonth = date.today().month;
currYear = date.today().year;
query = "/your_transaction_report_for_" + str(currDay) + "_" + str(currMonth) + "_" + str(currYear) + ".json"
finalUrl = baseUrl + query
print(finalUrl)

req = requests.get(url = finalUrl)

#response = req.json()
print(req)
