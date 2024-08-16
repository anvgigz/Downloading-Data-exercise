from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('the_csv_file_format/weather_data/algonquin.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Extract dates, High/low temperatures.
dates, Snows, Waters = [],[],[]
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        Snow = int(row[9])
        Water = int(row[7])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        Snows.append(Snow)
        Waters.append(Water)

#plot the highs, lows and dates.
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.plot(dates,Snows,color='red',alpha=0.5)
ax.plot(dates,Waters,color='blue',alpha=0.5)
ax.fill_between(dates,Snows,Waters,facecolor='blue',alpha=0.1)

#Format plot.
ax.set_title("Death Valley Daily High and Low Temperature,2021", fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()