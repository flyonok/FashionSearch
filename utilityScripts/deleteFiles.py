# -*- coding: utf-8 -*-
import json
import sys
from collections import OrderedDict
import csv
import os

with open("/root/deepstack/github/FashionSearch/csvFiles/deleteJsonFiles.csv", "rU") as f:
	reader=csv.DictReader(f)
        
	for row in reader:

		jsonFile=row['file_name']

		if os.path.exists(jsonFile):
			os.remove(jsonFile)
			print("File is deleted")
			print(row['file_name'])

		else:
			print("The file does not exist")
			print(row['file_name'])