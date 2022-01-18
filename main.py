import requests
from dbhelper import DBHelper
from datetime import datetime

url = "https://api.coingecko.com/api/v3/coins/categories"

res = requests.get(url).json()

db = DBHelper()

db.setup()

now = datetime.now()

for i in range(len(res)):
    data = (res[i]['id'], res[i]['name'], res[i]['market_cap'], res[i]['volume_24h'], str(now)[5:13])
    db.add_data(data)
