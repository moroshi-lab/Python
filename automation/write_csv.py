import csv

data = [
    ["名前", "年齢"],
    ["太郎", 20],
    ["花子", 19],
]

with open("automation/csv/output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("output.csv に書き込みました。")