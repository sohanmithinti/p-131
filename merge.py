import csv

data1 = []
data2 = []

with open("scraper.csv", "r")as file:
    reader = csv.reader(file)
    for row in reader:
        data1.append(row)

header1 = data1[0]
planetdata1 = data1[1:]    

with open("newdata.csv", "r")as file1:
    reader = csv.reader(file1)
    for row in reader:
        data2.append(row)

header2 = data2[0]
planetdata2 = data2[1:]    

final_header = header1 + header2

final_data = []

for index, row in enumerate(planetdata1):
    final_data.append(planetdata1[index]+planetdata2[index]) 

with open ("finaldata.csv", "a+")as f:
    writer = csv.writer(f)
    writer.writerow(final_header)
    writer.writerows(final_data)     