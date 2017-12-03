#!/usr/bin/python

#token validator python program

import base64
import requests
import json
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from base64 import b64encode
from Crypto.Cipher import AES
import binascii,os

grantType = 'client_credentials'
keyAndSecret = 'F0RyazY7__u7k2I4ISxgH2dttywa:j6Gmu2iHJF7CFblAXy432Dtoydga'
tokenEndpoint = 'https://10.100.8.2:8243/token'
testApi = 'http://10.100.8.2:8280/pizzashack/1.0.0/menu'


# Get token function
def getToken( str ):
	response = requests.post(url=tokenEndpoint, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36', 		'Authorization': 'Basic %s' % str }, data={'grant_type': grantType}, verify=False)

	resp_str = response.content
	resp_dict = json.loads(resp_str)
	if 'access_token' in resp_dict:
    		return resp_dict['access_token']
	else:
		print("error occured while getting new token...")
    		return null
		

# Token validation function
def validateToken( str ):
	response = requests.get(url=testApi, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36', 		'Authorization': 'Bearer %s' % str }, data={'grant_type': grantType}, verify=False)
	return response.status_code


# Token encryption function
def aes_encrypt( plaintext ):
    key = "00112233445566778899aabbccddeeff"
    iv = os.urandom(16)
    aes_mode = AES.MODE_CFB
    obj = AES.new(key, aes_mode, iv)
    ciphertext = obj.encrypt(plaintext)
    return ciphertext


# Program start

logger = logging.getLogger('TokenValidator')
fileHandler = logging.FileHandler('TokenValidator.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler) 
logger.setLevel(logging.WARNING)

encodedCredentials = b64encode(keyAndSecret).decode("ascii")
token = getToken(encodedCredentials)

# Running validateToken function to capture 401 status codes
while True:
	status = validateToken(token)
	if status == 200:
		print("status 200: API call successful...")
	elif status == 401:
		logger.error('Status 401: Token expired or unauthorized. Access Token: %s , Grant Type: %s , Credentials: %s' % (token, grantType, keyAndSecret))
		print("Status 401: Token expired or unauthorized, getting new token....")
		token = getToken(encodedCredentials)
	else:
		print("error while validating token...")

