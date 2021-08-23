import csv
import time
import os
from forex_python. converter import CurrencyRates



def create_split(name):
	with open(f'{name}.txt', 'w') as f:
		writer=csv.writer(f)
		writer.writerow(['name', 'amount', 'currency', 'description', 'time'])
		
def add_split(file, name, amount, currency='eur', description=''):
	if not os.path.exists(file):
		with open(f'{file}.txt', 'a') as f:
			writer=csv.writer(f)
			writer.writerow([name,amount,currency,description, time.strftime('%d %b %y', time.localtime())])
	else:
		print('please create a file first')
		
def print_split(file):
	try:
		with open(f'{file}.txt', 'r') as f:
			reader=csv.reader(f)
			for row in reader:
				print(', '.join(row))
	except FileNotFoundError as ferror:
		print('please create a file first')

def compute_balance(file, target_currency='eur'):
	c = CurrencyRates()
	target_currency = target_currency.upper()
	try:
		with open(f'{file}.txt', 'r') as f:
			reader=csv.reader(f)
			total = 0
			balances = {}
			next(reader, None)
			for row in reader:
				amount = c.convert(row[2], target_currency, int(row[1])) if row[2].upper() != target_currency else int(row[1])
				total+= amount
				if row[0] in balances:
					balances[row[0]]+= amount
				else:
					balances[row[0]]= amount

			balances = {person: amount for person, amount in sorted(balances.items(), key=lambda item: item[1])}
		return balances, total
						
	except FileNotFoundError as ferror:
		print('please create a file first')
	

def split(filename, target_currency='eur', tol=0.01):
	balances, total = compute_balance(filename, target_currency)
	target = total/(len(balances))
	mutable_balances = balances.copy()
	instructions = []
	for person, amount in balances.items():
		diff = target - amount
		if diff <= 0:
			break
		for receiver, bonus in reversed(mutable_balances.items()):
			if abs(bonus - target) <= tol:
				continue
			if abs(diff - (bonus - target)) <= tol:
				instructions.append(f'{person} should give {receiver} {diff}')
				mutable_balances[receiver] -= diff
				break
			else:
				instructions.append(f'{person} should give {receiver} {bonus - target}')
				mutable_balances[receiver] -= bonus - target
				diff -= bonus - target
	return instructions

if __name__ == '__main__':
	create_split('test')
	add_split('test', 'john', 30, 'Sek')
	add_split('test', 'john', 46, 'Sek')
	add_split('test', 'wanda', '36', 'Sek')
	add_split('test', 'simon', '38', 'Sek')
	add_split('test', 'leni', '58', 'Sek')
	add_split('test', 'thad', '34', 'Sek')
	add_split('test', 'mel', '58', 'Sek')
	#print_split('test')
	print(compute_balance('test'))		
	print(split('test'))
