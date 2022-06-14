import requests
import matplotlib.pyplot as plt
import json
import dateutil.parser

#----Gets sentiment data from GDELT and returns it as JSON data----
searchPhrase = input("Stock Ticker Symbol or Company Name: ")

baseUrl = "https://api.gdeltproject.org/api/v2/doc/doc?"
query = "query=%22" + searchPhrase + " %20stock" + "%22"
finalUrl = baseUrl + query + "&mode=TimelineTone&format=JSON"

req = requests.get(url = finalUrl)

response = req.json()

#----Load test data from file----
# testFile = open("TestData/tslastock-sentiment-timeline.json")
# testData = json.load(testFile)

dataPoints = response['timeline'][0]['data']

#----Create Graph Axes----
xAxisValues = []
for date in dataPoints:
    dateStr = dateutil.parser.parse(date['date'])
    readableDate = dateStr.strftime('%m/%d/%Y')
    xAxisValues.append(readableDate)

yAxisValues = [item['value'] for item in dataPoints]
xAxisTickLabels = xAxisValues[::7] # get every 7th value of the array, so not every tick has a label

plt.grid(True)
plt.plot(xAxisValues, yAxisValues, color='blue', marker='o')
plt.xlabel('Date')
plt.ylabel('Average Tone')
plt.xticks(rotation = 90)
axes = plt.gca()
axes.get_xaxis().set_ticks(xAxisTickLabels)

plt.show()