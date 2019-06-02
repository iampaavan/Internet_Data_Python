# Process JSON data returned from a server

# use the JSON module
import json


def main():
	
	# define a dictionary
	pythonData = {
				"sandwich": "Reuben",
				"toasted": "true",
				"toppings": [
					"Thousand Island Dressing",
					"Sauerkraut",
					"Pickles"
				],
				"price": 8.99
		}
	
	# TODO: serialize the JSON using dumps
	jsonStr = json.dumps(pythonData, indent=4)
	
	# TODO: print the resulting JSON string
	print(f"JSON Data: -----------------------------------------------------")
	print(jsonStr)


if __name__ == '__main__':
	main()