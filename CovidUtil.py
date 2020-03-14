import csv
import urllib.request
import codecs
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class COVID_19():
  """ COVID-19 Utility Class

  covid = COVID_19() \n
  covid.data[category][country] = list_of_cases \n

  category = ["confirmed", "deaths", "recovered"] \n
  country = list of countries in category \n
  list_of_cases = a list of integers representing cases on that date
  """ 
  def __init__(self):
    self.data = {
      "confirmed": {},
      "deaths": {},
      "recovered": {}
    }
    self.dates = set()
    self.__populate_data()
    self.countries = list(self.data["confirmed"].keys())
      
  def __populate_data(self):
    # Get Confirmed, Deaths, and Recovered timeseries data from Github
    self.__read_write("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv", "confirmed")
    self.__read_write("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv", "deaths")
    self.__read_write("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv", "recovered")

  def __read_write(self,url,cat):
    urlResponse = urllib.request.urlopen(url)
    csvfile = csv.reader(codecs.iterdecode(urlResponse, 'utf-8'))
    self.dates.update(next(csvfile, []))
    for line in csvfile:
      if line[1] in self.data[cat]:
        self.data[cat][line[1]] = [x + y for x, y in zip(self.data[cat][line[1]], [int(i) if i != '' else int(line[-2]) for i in line[4:]] )]
      else:
        self.data[cat][line[1]] = [int(i) if i != '' else int(line[-2]) for i in line[4:]  ]

  def chart_countries(self, countries = [], top=0 ):

    if len(countries) < 1:
      countries = [i[1] for i in sorted(
                  [[v[-1],k] for k,v in self.data["confirmed"].items()], 
                  reverse=True)]
    if top > 0:
      countries = countries[:top]

    dateArr = sorted([ datetime.strptime(i, '%m/%d/%y') 
                        for i in sorted(list(self.dates))[0:-4] ])

    for country in countries:
      fig, ax = plt.subplots()
      locator = mdates.AutoDateLocator()
      formatter = mdates.ConciseDateFormatter(locator)
      ax.xaxis.set_major_locator(locator)
      ax.xaxis.set_major_formatter(formatter)

      # Plot all three attributes (Confirmed, Deaths, Recovered)
      plt.plot( dateArr, self.data["confirmed"][country], 
                marker='', color='black', linewidth=2, label="Confirmed")
      plt.plot( dateArr, self.data["deaths"][country], 
                marker='', color='red', linewidth=2, label="Deaths")
      plt.plot( dateArr, self.data["recovered"][country], 
                marker='', color='green', linewidth=2, label="Recovered")
                
      # display chart
      ax.set_title(country)
      ax.xaxis_date()
      fig.autofmt_xdate()

      # plt.xticks(dateArr, dateArr, rotation=70)
      ax.grid(True)
      fig.tight_layout()
      plt.legend()
      plt.show()


if __name__ == '__main__':
  # Driver
  covid = COVID_19()
  # # covid.chart_countries(top=10)
  print(covid.countries)
  # print(covid.data)