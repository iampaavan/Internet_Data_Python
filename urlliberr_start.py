# handling errors and status codes

# TODO: import request, error and status modules
import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError


def main():
	
	#url = 'http://no-such-server.org' # will generate a URLError
	url = 'http://httpbin.org/status/404' # will generate a HTTPError
	#url = 'http://httpbin.org/html' # should work with no errors
	
	# TODO: use exception handling to attempt the URL access
	try:
		result = urllib.request.urlopen(url)
		
	except HTTPError as err:
		print(f"Error: {err.code}")
		
	except URLError as err:
		print(f"No Server Found: {err.reason}")
		
	else:
		print(f"Result Code: {result.status}")
	
		if result.getcode() == HTTPStatus.OK:
			print(f"{result.read().decode('utf-8')}")
		

if __name__ == '__main__':
	main()

