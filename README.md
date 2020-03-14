## The Corona Virus Utility Class for Python
Performs two primary functions:
- Get data from the Johns Hopkins Time Series Data on GitHub [here](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series) and work it into a dictionary.
- Quickly create charts based on the available data

## Using
```python
from CovidUtil import COVID_19
covid = COVID_19()

data_dict = covid.data
data_dict["confirmed"]   # "recovered", "deaths"
#=> {"country": [0,0,0,0,1,1,2,2,...]}
data_dict["confirmed"]["US"]
#=> [0,0,0,1,1,1,2,...]

# plot every country with matplotlib (descending by total confirmation)
covid.chart_countries() 
# plot ten countries with highest amount of confirmations
covid.chart_countries(top=10) 
# plot only US and China
covid.chart_countries(countries=["US","China"]) 
```


