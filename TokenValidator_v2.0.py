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
import random
from multiprocessing import Process

grantType = 'client_credentials'
keyAndSecret = 'F0RyazY7__u7k2I4ISxgH2dttywa:j6Gmu2iHJF7CFblAXy432Dtoydga'
tokenEndpoint = 'https://10.100.8.2:9444/oauth2/token'
testApi = 'http://10.100.8.2:8280/pizzashack/1.0.0/menu'



# Get token function
def getToken( str , scope):
	response = requests.post(url=tokenEndpoint, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36', 		'Authorization': 'Basic %s' % str }, data={'grant_type': grantType, 'scope': scope}, verify=False)

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
	print(response)
	return response.status_code


# Token encryption function
def aes_encrypt( plaintext ):
    key = "00112233445566778899aabbccddeeff"
    iv = os.urandom(16)
    aes_mode = AES.MODE_CFB
    obj = AES.new(key, aes_mode, iv)
    ciphertext = obj.encrypt(plaintext)
    return ciphertext

def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

# Run function
def run(count):
	print('Thread %s started....' % str(count))	

	# Running validateToken function to capture 401 status codes
	while True:
		number =  random.randint(0, 1000000)
		scope = "openid device_" + str(number)
		print(scope)

		token = getToken(encodedCredentials, scope)
		status = validateToken(token)
		if status == 200:
			print("status 200: API call successful...")
		elif status == 401:
			logger.error('Status 401: Token expired or unauthorized. Access Token: %s , Grant Type: %s , Credentials: %s' % (token, grantType, keyAndSecret))
			print("Status 401: Token expired or unauthorized, getting new token....")
			token = getToken(encodedCredentials, scope)
		else:
			print("Status %s:error while validating token..." % status)



# Program start
if __name__ == '__main__':
	logger = logging.getLogger('TokenValidator')
	fileHandler = logging.FileHandler('TokenValidator.log')
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	fileHandler.setFormatter(formatter)
	logger.addHandler(fileHandler) 
	logger.setLevel(logging.WARNING)
	encodedCredentials = b64encode(keyAndSecret).decode("ascii")
	#runInParallel(run(str(1)), run(str(2))) 

	Process(target=run, args=(1,)).start()
	Process(target=run, args=(2,)).start()
	Process(target=run, args=(3,)).start()
	Process(target=run, args=(4,)).start()
	Process(target=run, args=(5,)).start()
	Process(target=run, args=(6,)).start()
	Process(target=run, args=(7,)).start()
	Process(target=run, args=(8,)).start()
	Process(target=run, args=(9,)).start()
	Process(target=run, args=(10,)).start()
	Process(target=run, args=(11,)).start()
	Process(target=run, args=(12,)).start()
	Process(target=run, args=(13,)).start()
	Process(target=run, args=(14,)).start()
	Process(target=run, args=(15,)).start()
	Process(target=run, args=(16,)).start()
	Process(target=run, args=(17,)).start()
	Process(target=run, args=(18,)).start()
	Process(target=run, args=(19,)).start()
	Process(target=run, args=(20,)).start()
	Process(target=run, args=(21,)).start()
	Process(target=run, args=(22,)).start()
	Process(target=run, args=(23,)).start()
	Process(target=run, args=(24,)).start()
	Process(target=run, args=(25,)).start()
	Process(target=run, args=(26,)).start()
	Process(target=run, args=(27,)).start()
	Process(target=run, args=(28,)).start()
	Process(target=run, args=(29,)).start()
	Process(target=run, args=(30,)).start()
	Process(target=run, args=(31,)).start()
	Process(target=run, args=(32,)).start()
	Process(target=run, args=(33,)).start()
	Process(target=run, args=(34,)).start()
	Process(target=run, args=(35,)).start()
	Process(target=run, args=(36,)).start()
	Process(target=run, args=(37,)).start()
	Process(target=run, args=(38,)).start()
	Process(target=run, args=(39,)).start()
	Process(target=run, args=(40,)).start()
	Process(target=run, args=(41,)).start()
	Process(target=run, args=(42,)).start()
	Process(target=run, args=(43,)).start()
	Process(target=run, args=(44,)).start()
	Process(target=run, args=(45,)).start()
	Process(target=run, args=(46,)).start()
	Process(target=run, args=(47,)).start()
	Process(target=run, args=(48,)).start()
	Process(target=run, args=(49,)).start()
	Process(target=run, args=(50,)).start()
	Process(target=run, args=(51,)).start()
