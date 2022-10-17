import requests

# valid post-code or invalid - url of the API address
url = "http://api.postcodes.io/postcodes/"

# store the data
# user input as postcode

postcode = "e202st"
url_arg = url + postcode # ("http://api.postcodes.io/poscodes/e202st")

# display the outcome
response = requests.get(url_arg)
print(response.status_code)
print(type(response.content))

# convert data types
response_dict = response.json()
print(response_dict)

print(response_dict['result']['postcode'])
print(response_dict['result']['longitude'])
print(response_dict['result']['latitude'])

def req_value(value):

    for key in response_dict:
        print(response_dict['result'][value])


req_value('postcode')

def postcode():
    usr_postcode = input('Please enter a valid postcode: ')

