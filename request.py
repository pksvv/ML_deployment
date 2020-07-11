import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'bumpiness':200, 'skill':400,'cc':455})

print(r.json())