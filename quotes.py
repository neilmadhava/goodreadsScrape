from csv import reader
from random import randint
from random import choice

path=["/home/adama/Documents/(2) Programs/Python Programming/Scrapy/criminal_minds/quotes.csv","/home/adama/Documents/(2) Programs/Python Programming/Scrapy/goodreads_quotes/quotes.csv"]
f=choice(path)

if f == '/home/adama/Documents/(2) Programs/Python Programming/Scrapy/criminal_minds/quotes.csv':
	up_limit=562
else:
	up_limit=3001

with open(f) as file:
	x = randint(1, up_limit)
	i = 0
	csv_reader = reader(file)
	while i<x:
		next(csv_reader)
		i+=1

	for quote in csv_reader:
		if f == '/home/adama/Documents/(2) Programs/Python Programming/Scrapy/criminal_minds/quotes.csv':
			print("\n{}".format(quote[0]))
		else:
			print("\n{} \n\n― {}\n".format(quote[0].replace("\n", "").replace("―          ", ""), quote[1].replace("\n", "")))
		break