#!/bin/python3
import sys
import exurl


file = sys.argv[1]
payload = "FUZZ"

with open(file, 'r') as domain:
		splitting_urls = exurl.split_urls(domain, payload)
		print(*splitting_urls, sep='', end='\n')
