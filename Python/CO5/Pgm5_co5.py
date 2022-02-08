#dictionary to csv
import csv 
dict_value = [
{"name":"Sanal","age":22,"course":"bsc cs"},
{"name":"Shibili","age":22,"course":"bsc cs"},
{"name":"Gokul","age":19,"course":"bsc cs"},
]

fields = ["name","age","course"]

with open('dictconverted.csv','r+') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    csvfile.close()

with open('dictconverted.csv','r') as csvfiles:
    readerobj = csv.reader(csvfiles)
    for rows in readerobj:
        print(rows)
