#!/usr/bin/python3

"""
    This script will try to create a new account in Firebase instances.
	Need the Google Key, Firebase Instance and Email (default password is: 'testingPasswd') 

	Usage: python3 file.py HOST GOOGLE_KEY EMAIL
"""

from requests import post, get
from sys import argv
from json import loads

try:
	host = argv[1]
	key = argv[2]
	email = argv[3]

	headers = {
		'Content-Type': 'application/json',
	}

	headers2 = {
		'Content-Type': 'x-www-form-urlencoded',
	}

	params = (
		('key', '{}'.format(key)),
	)

	data = '{"email":"cihifi2533@provamail.com","password":"testingPasswd","returnSecureToken":true}'
	data2 = '{"returnSecureToken":true}'
	data3 = '{"grant_type":"refresh_token","refresh_token":"4feec49a0f252d2d4543b48b5fa85f6cf6979860_eb4f180a10b54a98bcc195608d1b09c6f4233189"}'

	response = post('https://identitytoolkit.googleapis.com/v1/accounts:signUp', headers=headers, params=params, data=data)
	print(response.text)

	response = post('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword', headers=headers, params=params, data=data)
	print(response.text)

	response = post('https://identitytoolkit.googleapis.com/v1/accounts:signUp', headers=headers, params=params, data=data2)
	print(response.text)

	response = post('https://securetoken.googleapis.com/v1/token', headers=headers, params=params, data=data3)
	print(response.text)

	if("identitytoolkit#SignupNewUserResponse" in response.text):
		token = loads(response.text)['idToken']	
		response = get('{}/.json?auth={}&print=pretty'.format(host, token))
		print(response.text)

except IndexError as e:
	print('Usage: python3 {} HOST GOOGLE_KEY EMAIL'.format(argv[0]))