import csv
import re


with open("log_file.csv","r") as f:
    text = f.read()

new_text = re.sub(r";", r",", text)
new_text = re.sub(r" ", r"_", new_text)

f2 = open("log_file_2.csv", "w")
f2.write(new_text)
f2.close()

manchester_file = "manchester.csv"
f_manchester = open(manchester_file,"w")

with open("log_file_2.csv") as f:
    csv_f = csv.DictReader(f)
    csv_writer = csv.DictWriter(f_manchester, fieldnames = csv_f.fieldnames)
    csv_writer.writeheader()
    for row in csv_f:
        match = re.match(r"Manchester$", row["Location"])
        if match != None:
            csv_writer.writerow(row)

f_manchester.close()