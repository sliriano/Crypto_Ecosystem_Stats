import requests
from dbhelper import DBHelper
from datetime import datetime

url = "https://api.coingecko.com/api/v3/coins/categories"

res = requests.get(url).json()

db = DBHelper()

db.setup()

now = datetime.now()

for i in range(len(res)):
    data = (res[i]['id'], res[i]['name'], res[i]['market_cap'], res[i]['content'], res[i]['volume_24h'], now)
    db.add_data(data)
