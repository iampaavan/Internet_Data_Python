# Send data to a server using urllib

# TODO: import the request and parse modules
import urllib.request
import urllib.parse


def main():

	# url = 'http://httpbin.org/get'
	url = 'http://httpbin.org/post'
	
	# TODO: create some data to pass to the GET request
	args = {
		'Name': 'Paavan Gopala',
		'Is_Author': True
	}
	
	# TODO: the data needs to be url-encoded before passing as arguments
	data = urllib.parse.urlencode(args)
	
	# TODO: issue the request with a data parameter as part of the URL
	#result = urllib.request.urlopen(url + '?' + data)
	
	# TODO: issue the request with a data parameter to use POST
	data = data.encode('utf-8')
	result = urllib.request.urlopen(url, data=data)
	
	print(f"Result Code: {result.status}")
	print(f"Returned Data ----------------------------------------")
	print(f"{result.read().decode('utf-8')}")


if __name__ == '__main__':
	main()
