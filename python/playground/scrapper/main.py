#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example of using virtualenv and requests modules
https://github.com/kennethreitz/requests
http://www.virtualenv.org/en/latest/
"""

import requests

def main():
	r = requests.get('http://net.tutsplus.com/')

	print "\n%-20s %-30s" % ("Status code", r.status_code)
	print "Headers..."

	for key, value in r.headers.iteritems():
		print "%-20s %-30s" % (key, value)

	html_file = open('index.html','w')
	html_file.write(r.text.encode('utf-8'))
	html_file.close()

	print "Open index.html to view the content...\n"

if __name__ == "__main__":
	main()