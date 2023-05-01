import requests

response = requests.post('https://census-toy.nceng.net/prod/toy-census')
print(response.status_code)
