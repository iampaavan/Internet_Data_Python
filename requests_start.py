# using the requests library to access internet data

# import the requests library
import requests


def main():
	# TODO: Use requests to issue a standard HTTP GET request
	#url = 'http://httpbin.org/xml'
	#result = requests.get(url)
	#printResults(result)
	
	# TODO: Send some parameters to the URL via a GET request
	# Note that requests handles this for you, no manual encoding
	#url = 'http://httpbin.org/get'
	#url = 'http://httpbin.org/post'
	'''dataValues = {
		'key1': 'value1',
		'key2': 'value2'
	}'''
	#result = requests.get(url, params=dataValues)
	#result = requests.post(url, data=dataValues)
	#printResults(result)
	
	# TODO: Pass a custom header to the server
	url = 'http://httpbin.org/get'
	headerValues = {
		"User-Agent": "Paavan Gopala App/1.0.0"
	}
	result = requests.get(url, headers=headerValues)
	printResults(result)
	
	
def printResults(resData):

	print(f"Result Code: {resData.status_code}")
	print(f'\n')
	
	print(f"Headers: ----------------------------------------------------")
	print(f"{resData.headers}")
	print(f'\n')
	
	print(f"Returned Data: ----------------------------------------------")
	#print(f'{resData.content}')
	print(f"{resData.text}")
	
	
if __name__ == '__main__':
	main()
	