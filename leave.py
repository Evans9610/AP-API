#coding=utf8

import requests
import re
from pprint import pprint
from bs4 import BeautifulSoup 


main_url = "http://leave.kuas.edu.tw"
session = requests.session()


def login(username, password):
	url = "/"
	post_data = {"Login1$UserName":username,"Login1$Password":password,"Login1$LoginButton":u"登入"}
	response = session.get(main_url + url)
	bs = BeautifulSoup(response.content)
	for x in bs.findAll(name='input'):
		if re.match("^__",x["id"]):
			post_data[x["name"]] = x["value"]
		
	response = session.post(main_url + url, data=post_data)
	print response.content


def main():
	username = ""
	password = ""
	login(username, password)


if __name__ == "__main__":
	main()
