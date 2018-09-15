# -*- coding: utf-8 -*-
#Author:http://github.com/CrypticWizard 
#mail:mdarifulislam.protik@gmail.com
#Follow Me For More If You Like It Give It A Star
import requests 
def FindAll():
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	f=open('list.txt', 'r').read().split('\n')
	o=open('fixed.txt', 'r').read().split('\n')
	with open('result.txt', 'w') as result:
		for line in f:
			if line == "":
				continue;
			newline=line.split('/')
			parent_url=newline[2]
			for line in o:
				if line == "":
					continue;
				final_url='http://' + parent_url + '/' + line 
				try:
					r = requests.get(final_url,headers=headers,timeout=3)
					r.raise_for_status()
				except requests.exceptions.HTTPError:
					continue;
				except requests.exceptions.ConnectionError:
					continue;
				except requests.exceptions.Timeout:
					continue;
				else:
					print('\033[92m' + 'Found->' + final_url) 
					result.write(final_url+"\n")
print('\033[94m'+'Just Started The Panel_FInder. Please Wait')

FindAll()
print("Program Finished, See The result.txt File For Ur Result")
