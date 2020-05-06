"""Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build
"""
import os
import argparse

HELP = "one of [install, build]"

parser = argparse.ArgumentParser()
parser.add_argument("subcommand", action="store", help=HELP)
args = parser.parse_args()

if args.subcommand == "build":
	print("Building docs, requirements.txt, setup.py, poetry build")
	os.system("pydoc-markdown > DOCS.md")
	os.system("dephell deps convert --envs=main")
	os.system("dephell deps convert --to setup.py")
	os.system("poetry build")
elif args.subcommand == "install":
	print("Poetry install")
	os.system("poetry install")
