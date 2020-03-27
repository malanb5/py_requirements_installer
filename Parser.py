#!/usr/bin/env python3
import os

class Parser(object):

	@staticmethod
	def __check_py(file_s: str):
		"""
		check to see if a file is a python file
		:return: boolean: whether the file is a python file or not
		"""
		if type(file_s) is not str:
			raise Exception("file name must be a string")
		return file_s.endswith("py")

	@staticmethod
	def get_py_files(configs):
		if type(configs["src_dir"]) is str:
			src_dir_d = os.walk(configs["src_dir"])
			file_set = set()
			for r, d_s, f_s in src_dir_d:
				for f in f_s:
					if Parser.__check_py(f):
						file_set.add(os.path.join(r, f))
		return file_set

	@staticmethod
	def parse_package(p_l):
		if len(p_l) == 1:
			return None

		if '.' in p_l:
			return p_l.split(".")[0]

		return p_l

	@staticmethod
	def parse_line(l):
		"""
		parses a line of text for the package to install
		"""
		s_l = l.split()

		if len(s_l) < 2:
			return None

		if any(x in s_l[0] for x in ("from", "import")):
			return Parser.parse_package(s_l[1])
		else:
			return None

	@staticmethod
	def parse_file(f_s, reqs):
		with open(f_s, "r+") as f:
			lines = f.readlines()
			for l in lines:
				req = Parser.parse_line(l)
				if req is not None:
					reqs.add(req)
		return reqs

	@staticmethod
	def get_reqs(py_files):
		reqs = set()

		while (len(py_files) > 0):
			f = py_files.pop()
			reqs = Parser.parse_file(f, reqs)

		return reqs