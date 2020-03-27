# Python Requirements Tool

This package compiles and puts all of the required python packages into a single requirements.txt file.

## Quick Start

#### Usage
Put root directory of your project that you are installing in the config.ini file in the
line src_dir eg.

*config.ini*
```
src_dir: "/home/<username>/projects/src"
```

Run the command 
```
python main.py
```

This will generate the requirements.txt file in the specified directory.
If nothing is set this will default to the root of the project directory.


### Contributing
Please submit an issue or pull request if you have suggestions on how to make this project better.