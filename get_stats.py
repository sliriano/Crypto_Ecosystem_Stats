from dbhelper import DBHelper

db = DBHelper()

db.setup()

print(db.get_eco_stats(0))