#nathional weather information report
import requests
from bs4 import BeautifulSoup
import pandas

web_page = requests.get("https://forecast.weather.gov/MapClick.php?textField1=33.22&textField2=-97.15#.XaXfI0ZKjb0")
soup = BeautifulSoup(web_page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")

first_one = forecast_items[0]
period = first_one.find(class_="period-name").get_text()
short_desc = first_one.find(class_="short-desc").get_text()
temp = first_one.find(class_="temp").get_text()
desc=seven_day.select(".tombstone-container img")

#part-one
print("First Forecast Item Details")
print("Period :",period)
print("Short Description:",short_desc)
print("Temperature:",temp)
print("Description :",desc[0]["title"], "\n")

print("Forecast items have to saved to \"Inclass_exercise3_output.csv\"")
#part-two
all_period=[pd.get_text() for pd in seven_day.select(".tombstone-container .period-name")]
all_short_desc = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
all_temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
all_descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

a = pandas.DataFrame({
    "period": all_period,
    "short_desc":all_short_desc,
    "temp":all_temps,
    "desc":all_descs
})
a.to_csv("Inclass_exercise3_output.csv")

