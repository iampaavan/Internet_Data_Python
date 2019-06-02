# Process JSON data returned from a server

# TODO: use the JSON Module
import json


def main():
	
	# define a string of JSON code
	jsonstr = '''{
				"sandwich": "Reuben",
				"toasted": "true",
				"toppings": [
					"Thousand Island Dressing",
					"Sauerkraut",
					"Pickles"
				],
				"price": 8.99
		}'''
	
	# TODO: parse the JSON data using loads
	data = json.loads(jsonstr)
	
	# TODO: print information from the data structure
	print(f"Sandwich: {data['sandwich']}")
	if data['toasted']:
		print(f"And it's toasted!")
		
	for topping in data['toppings']:
		print(f"Topping: {topping}")
	
	
if __name__ == '__main__':
	main()