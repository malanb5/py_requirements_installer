#!/usr/bin/env python3
import argparse
from pyreqgen.ReqParser import ReqParser

def main():

	parser = argparse.ArgumentParser(description='Takes a source directory compiles and puts all of the required python packages '
												 'into a single requirements.txt file')
	parser.add_argument('--src_dir', type=str,
						help='the root project directory')

	args = parser.parse_args()
	print(args.src_dir)
	ReqParser.run(args.src_dir, write_o=True, alpha=True)

	# print("Done.")

if __name__== "__main__":
	main()