import pandas

fileobj = pandas.read_csv('file.csv',usecols=['name'])
print(fileobj)
