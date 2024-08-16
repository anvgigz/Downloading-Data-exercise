from pathlib import Path
import csv

path = Path('the_csv_file_format/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index,column_header in enumerate(header_row):
    print(index,column_header)
