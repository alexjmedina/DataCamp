# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?i=tt3896198&apikey=b8aaa2ce&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)
