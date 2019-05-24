import requests

# Taking Input from the User
movie_name = raw_input("Enter the Movie Name: ")

#Putting each word in the list
list1 = movie_name.split(" ")

#Constructing Movie name with "+" sign
s1 = ""
for i in list1:
    s1 = s1+"+"+i

uri = "http://www.omdbapi.com/?t="+s1+"&apikey=efcb54fa"

r = requests.get(uri)
key = ""
value = ""

data = r.json()
for i in data:
    if i == "Ratings":
        if len(data[i]) > 1:
            d = data[i][1] # d is the dict and data[i] is the list
            for i in d:
                if i == "Value":
                    value = d[i]
if value != "":
    print("The Rotten Tomatoes are: " + value)
else:
    print("Rotten Tomatoes entry not found")
