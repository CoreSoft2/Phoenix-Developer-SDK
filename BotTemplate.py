from __future__ import unicode_literals
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--infile', nargs=1,
                    help="JSON file to be processed",
                    type=argparse.FileType('r'))
args = parser.parse_args()

# Loading a JSON object returns a dict.
d = json.load(args.infile[0])

profileInfo = {}
profileInfo.update(d)
input = profileInfo[u'input']
output = profileInfo[u'output']
location = profileInfo[u'location']

name = None
greeting = None

for data in input:
	if data[u'name'] == u'Name':
		name = data[u'value']
	if data[u'name'] == u'Greeting':
		greeting = data[u'value']

import os

if __name__ == "__main__":
	 print(str(name) + " " + str(greeting))