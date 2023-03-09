import csv

#1
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print(f"Name: {name}, Phone: {phone}, Role: {role}")

f.close()

#2
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts) 

#3
with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(f"{row['name']} has {row['users']} users")

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
         {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
keys = users[0].keys()
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
