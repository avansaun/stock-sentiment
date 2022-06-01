from typing import final
import requests
import matplotlib.pyplot as plt
import json

#Gets sentiment data from GDELT and returns it as JSON data
searchPhrase = input("Stock Ticker Symbol or Company Name: ")

baseUrl = "https://api.gdeltproject.org/api/v2/doc/doc?"
query = "query=%22" + searchPhrase + " %20stock" + "%22"
finalUrl = baseUrl + query + "&mode=TimelineTone&format=JSON"

req = requests.get(url = finalUrl)

data = req.json()
#print(data)

#plot the data
xAxis = [key for key, value in data.items()] #TODO: how to get the correct data from the JSON object?
yAxis = [value for key, value in data.items()]
plt.grid(True)

plt.plot(xAxis, yAxis, color='blue', marker='o')
plt.xlabel('Date')
plt.ylabel('Average Tone')

plt.show()
