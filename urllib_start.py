import urllib.request


def main():
	
	# the URL to retrieve our sample data from
	url = "http://httpbin.org/xml"
	
	# TODO: Open the URL and retrieve some data.
	result = urllib.request.urlopen(url)
	
	# TODO: Print the result code from the request, should be 200 OK
	print(f"Result Code: {result.status}")
	
	# TODO: Print the returned data headers
	print(f"Headers: ---------------------")
	print(f"{result.getheaders()}")
	
	# TODO: Print the returned data itself.
	print(f"Returned Data: ----------------")
	print(f"{result.read().decode('utf-8')}")


if __name__ == '__main__':
	main()

