import csv

data = []
with open("extra_data.csv", "r")as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

headers = data[0]
planetdata = data[1:]

for data in planetdata:
    data[2] = data[2].lower()

planetdata.sort(key = lambda planetdata:planetdata[2]) 

with open ("newdata.csv", "a+")as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planetdata)