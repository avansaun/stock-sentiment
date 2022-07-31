from typing import final
import requests
import matplotlib.pyplot as plt
import json
from datetime import date

#Gets house transaction data and returns it as JSON data

baseUrl = "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com"
currDay = date.today().day
currMonth = date.today().month
currYear = date.today().year
query = "/data/transaction_report_for_" + str(currMonth) + "_" + str(25) + "_" + str(currYear) + ".json"
testurl = "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/filemap.xml"
finalUrl = baseUrl + "/data/transaction_report_for_07_26_2022.json"
print(finalUrl)
print(testurl)

req = requests.get(url = finalUrl)

response = req.json()
print(response)
