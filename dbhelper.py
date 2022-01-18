import sqlite3

class DBHelper:

    def __init__(self, dbname="ecodata.db"):
        # sets database name and establishes a connection to it
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        # creates a table within our databse 
        create_table = "CREATE TABLE IF NOT EXISTS ecosystem_stats (id, name, market_cap, volume_24h, time)"
        self.conn.execute(create_table)
        self.conn.commit()
    
    def add_data(self, request_tuple):
        # inserts an item into the table
        insert = "INSERT INTO ecosystem_stats VALUES (?,?,?,?,?)"
        self.conn.execute(insert, request_tuple)
        self.conn.commit()
    
    def remove_data(self, id):
        remove = "DELETE FROM ecosystem_stats WHERE name = (?)"
        id_tuple = (id,)
        self.conn.execute(remove,id_tuple)
        self.conn.commit()

    def get_table(self):
        table = []
        for row in self.conn.execute('SELECT * FROM requests'):
            table.append(row)
        return table
    
    def get_eco_stats(self, id):
        table = []
        get_eco = 'SELECT * FROM ecosystem_stats WHERE id = (?)'
        id_tuple = (id,)
        for row in self.conn.execute(get_eco,id_tuple):
            table.append(row)
        return table
