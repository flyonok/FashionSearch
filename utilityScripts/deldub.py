# -*- coding: utf-8 -*-
import json
import sys
from collections import OrderedDict
import csv
import os

with open("/root/deepstack/github/FashionSearch/csvFiles/jsonFiles.csv", newline=None) as f:
	reader=csv.DictReader(f)
        
	for row in reader:

		jsonFile=row['jsonFile_prep']

		with open(jsonFile) as json_file:

			data = json.load(json_file)

			seen = OrderedDict()
			dubs = OrderedDict()

			for d in data:
				oid = d["productId"]

		
				if oid not in seen:
					seen[oid] = d	
			
				else:
					dubs[oid]=d

			baseFileName=os.path.splitext(jsonFile)[0]

			with open('/root/deepstack/github/FashionSearch/jsonFiles/'+row['file_name_final'], 'w') as out:
				json.dump(list(seen.values()), out)

			with open('/root/deepstack/github/FashionSearch/jsonFiles/'+'DELETED'+row['file_name_final'], 'w') as out:
				json.dump(list(dubs.values()), out)