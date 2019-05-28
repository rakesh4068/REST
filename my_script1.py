import requests

movie = raw_input("Enter the Movie name: ")
uri = "http://www.omdbapi.com/?t="+movie+"&apikey=efcb54fa"
r = requests.get(uri)

data = r.json() # data is the dict
for i in data:  # i is the key of the dict
	if i == "Ratings":
		list1 = data[i]
		d = list1[1]   # d is the dict
		print(d["Source"] + " : " + d["Value"])
