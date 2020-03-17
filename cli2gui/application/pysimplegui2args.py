"""Functions to create args from pysimplegui values
"""

import argparse


def argparseFormat(values):
	'''Format args for argparse '''
	args = {}
	for key in values:
		if key[-1] == "#": # File
			args[key[:-1]] = open(values[key], "r", encoding="utf-8")
		elif isinstance(values[key], str) and len(values[key]) == 0: # Empty strings are None
			args[key] = None
		else:
			args[key] = values[key]
	return argparse.Namespace(**args)


def optparseFormat(values):
	'''Format args for optparse '''
	args = {}
	for key in values:
		args[key] = values[key] if values[key] else None
	return args


def getoptFormat(values):
	'''Format args for getopt '''
	return ([(key, values[key]) for key in values if values[key]], [])

def docoptFormat(values):
	'''Format args for docopt '''
	args = {}
	for key in values:
		args[key] = values[key] if not (isinstance(values[key], str) and len(values[key]) == 0) else None
	return args

def argFormat(values, argument_parser):
	"""Format the args for the desired parser

	Args:
		values (dict): values from simple gui
		argument_parser (str): argument parser to use

	Returns:
		args: args
	"""
	formattedArgs = None
	if argument_parser == "argparse":
		formattedArgs = argparseFormat(values)
	elif argument_parser == "optparse":
		formattedArgs = optparseFormat(values)
	elif argument_parser == "getopt":
		formattedArgs = getoptFormat(values)
	elif argument_parser == "docopt":
		formattedArgs = docoptFormat(values)
	return formattedArgs
