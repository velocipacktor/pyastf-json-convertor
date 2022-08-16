#!/usr/bin/env python3

import sys
import os
import importlib

if not sys.argv[1]:
  sys.stderr.write('Input file required\n')
  sys.exit(1)

input_file = str(sys.argv[1])

if not os.path.isfile(input_file):
  sys.stderr.write('Input file not found\n')
  sys.exit(1)

basedir = os.path.dirname(input_file)
sys.path.insert(0, basedir)

file = os.path.basename(input_file).split('.')[0]
module = importlib.import_module(file, package='./')

profile = module.register().get_profile('')
print(profile.to_json_str())
