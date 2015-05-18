#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script Python Example

import os
from sets import Set

extracted_domains = []
filename = "test.txt"
lines = open(filename).read().splitlines()


import tldextract

for line in lines:
	res = tldextract.extract(line)
	extracted_domains.append(res.registered_domain)

extracted_domains = Set(extracted_domains)
with open('filename.txt', 'w') as f:
    f.write('\n'.join(extracted_domains))

#print "#################"
