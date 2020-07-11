import urllib.request as urllib
import json

url = 'https://data.epa.gov.tw/api/v1/uv_s_01?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&format=json;'

response = urllib.urlopen(url)
#print(response.read().decode('utf-8'))

jsonobj = json.load(response)
for data in jsonobj['records']:
    print('{County}{SiteName}: {UVI}'.format(**data))
