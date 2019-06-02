# using the requests library to access internet data

import requests
from requests.auth import HTTPBasicAuth


def main():
	 # Access a URL that requires authentication - the format of this
	 # URL is that you provide the username/password to auth against
	 url = 'http://httpbin.org/basic-auth/Paavan Gopala/mypassword'
	 
	 # TODO: Create a credential object using HTTPBasicAuth
	 myCredential = HTTPBasicAuth('Paavan Gopala', 'mypassword')
	 
	 # TODO: Issue the request with the authentication credentials
	 result = requests.get(url, auth=myCredential)
	 #result = requests.get(url, auth=('Paavan Gopala', 'mypassword'))
	 #result = requests.get( url, auth=('paavan Gopala', 'mypass'))
	 printResults(result)
	 
	
def printResults(resData):
	
	print(f"Result Code: {resData.status_code}")
	print(f'\n')
	
	print(f"Returned Data: -----------------------------------------------")
	print(f"{resData.text}")
	
	
if __name__ == '__main__':
	main()