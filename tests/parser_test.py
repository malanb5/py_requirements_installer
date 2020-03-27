import unittest, yaml
from pyreqgen.ReqParser import *

class TestParser(unittest.TestCase):

	def test_files(self):

		with open("../config.yaml", 'r+') as config_f:
			configs = yaml.load(config_f, Loader=yaml.FullLoader)
			print(configs)

		py_files = ReqParser.__get_py_files(configs)
		reqs = ReqParser.__get_reqs(py_files)

		with open("requirements.txt", 'w+') as req_f:
			req_f.write('\n'.join(reqs))

		with open("requirements.txt", "r") as req_f:
			lines = req_f.readlines()
			print(lines.sort())

		exp_lines = ['IPython\n',
					 'altair\n',
					 'bayes_opt\n',
					 'catboost\n',
					 'category_encoders\n',
					 'collections\n',
					 'datetime\n',
					 'eli5\n',
					 'gc\n',
					 'itertools\n',
					 'joblib\n',
					 'json\n',
					 'lightgbm\n',
					 'matplotlib\n',
					 'networkx\n',
					 'numba\n',
					 'numpy\n',
					 'os\n',
					 'pandas\n',
					 're\n',
					 'seaborn\n',
					 'shap\n',
					 'sklearn\n',
					 'time\n',
					 'tqdm\n',
					 'typing\n',
					 'warnings\n',
					 'xgboost\n']

		lines = set(map(lambda x: x.strip(), lines))
		exp_lines = set(map(lambda x: x.strip(), exp_lines))

		self.assertEqual(lines, exp_lines)

if __name__ == "__main__":
	unittest.main()