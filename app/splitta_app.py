import csv
import time

def create_split(name):
	with open(f'{name}.txt', 'w') as f:
		writer=csv.writer(f)
		writer.writerow(['name', 'amount', 'currency', 'description', 'time'])
		
def add_split(file, name, amount, currency='eur', description=''):
	try:
		with open(f'{file}.txt', 'a') as f:
			writer=csv.writer(f)
			writer.writerow([name,amount,currency,description, time.strftime('%d %b %y', time.localtime())])
	except FileNotFoundError as ferror:
		print('please create a file first')
		
def print_split(file):
	try:
		with open(f'{file}.txt', 'r') as f:
			reader=csv.reader(f)
			for row in reader:
				print(', '.join(row))
	except FileNotFoundError as ferror:
		print('please create a file first')

def compute_balance(file):
	try:
		with open(f'{file}.txt', 'r') as f:
			reader=csv.reader(f)
			balances={'total': 0}
			next(reader, None)
			for row in reader:
				balances['total']+=int(row[1])
				if row[0] in balances:
					balances[row[0]]+=int(row[1])
				else:
					balances[row[0]]=int(row[1])
		return balances
						
	except FileNotFoundError as ferror:
		print('please create a file first')


if __name__ == '__main__':
	create_split('test')
	add_split('test', 'john', 30)
	add_split('test', 'john', 46)
	add_split('test', 'wanda', '36')
	print_split('test')
	print(compute_balance('test'))
		