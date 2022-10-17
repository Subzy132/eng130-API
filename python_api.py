# APIs with Python
# install package called requests
# pip install requests
import requests

#Get
request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")

# Check the outcome of our API call
# print(request_bbc_status_code.status_code)

# Lets check the header
# print(request_bbc_status_code.headers)

# Lets check the content
# print(request_bbc_status_code.content)

# print the status code with success message

succ_youtube_status_code = requests.get("https://www.youtube.com")

print(succ_youtube_status_code.status_code)

# print unsuccessful if status code is not 200

unsucc_youtube_status_code = requests.get("https://www.bbc.com/asf/234/233")

print(unsucc_youtube_status_code.status_code)

# print(succ_youtube_status_code.text)
