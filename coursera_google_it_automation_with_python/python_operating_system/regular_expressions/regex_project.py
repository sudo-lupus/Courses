import csv
import re

with open("log_file.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
