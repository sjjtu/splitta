import click
from app.splitta_app import *

@click.group()
def cli():
	pass

@cli.command()
@click.argument('filename')
def create(filename):
	create_split(filename)

@cli.command()
@click.argument('filename')
@click.argument('name')
@click.argument('amount')
@click.argument('currency', required=False, default='eur')
@click.argument('description', required=False, default='')
def add(filename, name, amount, currency='eur', description=''):
	add_split(filename, name, amount, currency, description)

@cli.command()
@click.argument('filename')
def overview(filename):
	print_split(filename)

@cli.command()
@click.argument('filename')
def compute(filename):
	click.echo(compute_balance(filename))
	

@cli.command()
@click.argument('filename')
def split(filename):
	click.echo(split_balance(filename))


if __name__=="__main__":
	cli()