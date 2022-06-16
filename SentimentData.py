from matplotlib.markers import MarkerStyle
import requests
import matplotlib.pyplot as plt
import json
import dateutil.parser

class SentimentData():

    #----Get sentiment data from GDELT----
    def QuerySentimentData(searchStr):
        #searchPhrase = input("Stock Ticker Symbol or Company Name: ")

        baseUrl = "https://api.gdeltproject.org/api/v2/doc/doc?"
        query = "query=%22" + searchStr + " %20stock" + "%22"
        finalUrl = baseUrl + query + "&mode=TimelineTone&format=JSON"

        req = requests.get(url = finalUrl)

        response = req.json()

        #----Load test data from file----
        # testFile = open("TestData/tslastock-sentiment-timeline.json")
        # testData = json.load(testFile)

        dataPoints = response['timeline'][0]['data']
        return dataPoints


    #----Graph The Sentiment Data----
    def GraphDataValues(dataPoints):
        xAxisValues = []
        for date in dataPoints:
            dateStr = dateutil.parser.parse(date['date'])
            readableDate = dateStr.strftime('%m/%d/%Y')
            xAxisValues.append(readableDate)

        yAxisValues = [item['value'] for item in dataPoints]
        xAxisTickLabels = xAxisValues[::7] # only set label for every 7th value

        plt.grid(True)
        plt.plot(xAxisValues, yAxisValues, color='green', marker='.')
        plt.xlabel('Date')
        plt.ylabel('Average Tone')
        plt.xticks(rotation = 90)
        axes = plt.gca()
        axes.get_xaxis().set_ticks(xAxisTickLabels)
        plt.show()


    #----Get Sentiment Graph Data For Stock Symbol----
    def GetSentimentData(tickerSymbol):
        graphData = SentimentData.QuerySentimentData(tickerSymbol)
        SentimentData.GraphDataValues(graphData)