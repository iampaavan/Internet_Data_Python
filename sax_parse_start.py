# parse xml data using the SAX parser

import requests
import xml.sax

# TODO: define the ContentHandler subclass for our content


class MyContentHandler(xml.sax.ContentHandler):
	
	def __init__(self):
		self.slideCount = 0
		self.itemCount = 0
		self.isinTitle = False
		self.titleCount = 0
		
	# TODO: Handle startElement
	def startElement(self, tagName, attrs):
		
		if tagName == 'slideshow':
			print(f"Slideshow Title: {attrs['title']}")
			
		elif tagName == 'slide':
			self.slideCount += 1
			
		elif tagName == 'item':
			self.itemCount += 1
			
		elif tagName == 'title':
			self.isinTitle = True
			self.titleCount += 1
			
	# TODO: Handle endElement
	def endElement(self, tagName):
		if tagName == 'title':
			self.isinTitle = False
			
	# TODO: Handle text data
	def characters(self, chars):
		if self.isinTitle:
			print(f"Title: {chars}")
			
	# TODO: Handle startDocument
	def startDocument(self):
		print(f"About to start.")
	
	# TODO: Handle endDocument
	def endDocument(self):
		print(f'Finishing up!')


def main():
	# Create a new content handler for the SAX parser
	handler = MyContentHandler()
	
	# use the Request lib to get XML data from the server
	# remember that Requests auto-decodes our content
	url = 'http://httpbin.org/xml'
	result = requests.get(url)
	# print(result.text)
	
	# TODO: call the parseString method on the xml text content received
	xml.sax.parseString(result.text, handler)
	
	# when we're done, print out some interesting results
	print(f"There are {handler.slideCount} slide elements.")
	print(f"There are {handler.itemCount} item elements.")
	print(f"There are {handler.titleCount} title elements.")
	
	
if __name__ == '__main__':
	main()

