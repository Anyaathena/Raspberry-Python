import urllib.request as urllib

url = 'https://cdn2.ettoday.net/images/3348/d3348014.jpg'

response = urllib.urlopen(url)

with open('image.jpg', 'wb') as f:
    f.write(response.read())

