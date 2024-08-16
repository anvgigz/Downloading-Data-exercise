from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('the_csv_file_format/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Extract dates and high temperatures.
dates,precipitation = [],[]
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rain = int(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        precipitation.append(rain)

#plot the highs, lows and dates.
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.plot(dates,precipitation,color='purple',alpha=0.5)

#Format plot.
ax.set_title("Daily High and Low Temoperatures, 2021", fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
print(precipitation)
plt.show()
