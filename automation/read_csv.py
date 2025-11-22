
import csv

with open("automation/csv/sample.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)