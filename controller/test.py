import urllib.request
url = "https://www.google.com"

status_code = urllib.request.urlopen(url).getcode()
print(status_code)
website_is_up = status_code == 200

print(website_is_up)
