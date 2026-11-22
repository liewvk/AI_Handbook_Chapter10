import csv
from pathlib import Path

file_path = Path("ai_training_data.csv")
rows = [
    ["hours", "score"],
    [2, 50],
    [4, 65],
    [6, 80],
]

with file_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("Saved:", file_path.name)
with file_path.open("r", encoding="utf-8", newline="") as file:
    for row in csv.reader(file):
        print(row)

