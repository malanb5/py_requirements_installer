#!/usr/bin/env python3
import yaml
from Parser import Parser

def main():
	with open("config.ini", 'r+') as config_f:
		configs = yaml.load(config_f, Loader=yaml.FullLoader)
		print(configs)

	py_files = Parser.get_py_files(configs)
	reqs = Parser.get_reqs(py_files)

	with open("requirements.txt", 'w+') as req_f:
		req_f.write('\n'.join(reqs))

	print("Done.")

if __name__== "__main__":
	main()