# pyHusteblume

## Installation
Install the dependencies using pip:
`pip install -r requirements.txt`

## Usage
`python3 main.py`

## Example

```

  File "/Users/arisum/pyhusteblume/main.py", line 27, in <module>
    f = Forecast.get(station_for_hannover, user=u)
  File "/Users/arisum/pyhusteblume/husteblume/api.py", line 52, in get
    r = api('get', 'https://api.husteblume-app.de/forecast/' + station, user=user)
  File "/Users/arisum/pyhusteblume/husteblume/__init__.py", line 20, in api
    r.raise_for_status()
  File "/usr/local/lib/python3.9/site-packages/requests/models.py", line 943, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.husteblume-app.de/forecast/DEHANN

pyhusteblume on  master [?] via 🐍 v2.7.16
❯ cat ../te
cat: ../te: No such file or directory

pyhusteblume on  master [?] via 🐍 v2.7.16
❯ cat ../test.py
import requests

headers = {
    'authorization': 'Basic MTBGRkMzQkQ6M3VlaTUwcTVoOGphbGZraDN1OWRwN29tZmo=',
    'user-agent': 'okhttp/4.4.0',
}

response = requests.get('https://api.husteblume-app.de/forecast/DEHANN', headers=headers)
print(response, response.text)

pyhusteblume on  master [?] via 🐍 v2.7.16
❯

pyhusteblume on  master [?] via 🐍 v2.7.16
❯ vim ./husteblume/__init__.py

pyhusteblume on  master [!?] via 🐍 v2.7.16 took 1m2s
❯ python3 main.py
{'user-agent': 'okhttp/4.4.0'}
<husteblume.api.Stations object at 0x105b713d0>
'DEHANN'
<User: appId=6C17808F>
{'authorization': 'Basic NkMxNzgwOEY6bmxZTGtkVnNpWm5SR2tzTWpwa01aeFFoY2o=',
 'user-agent': 'okhttp/4.4.0'}
<husteblume.api.Forecast object at 0x104d84eb0>
{'ALNU': [0, 0, 0],
 'AMBR': [0, 0, 0],
 'ARTE': [1, 1, 1],
 'BETU': [0, 0, 0],
 'CORY': [0, 0, 0],
 'FRAX': [0, 0, 0],
 'POAC': [2, 2, 2],
 'SECA': [0, 0, 0]}
```
