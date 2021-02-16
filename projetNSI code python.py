import sqlite3
conn = sqlite3.connect('imdb.db')
c = conn.cursor()
c.execute("select * from name_basics limit 10")
for row in c:
    print(row)
conn.close()

import sqlite3
class database:
    #https://docs.python.org/3/library/sqlite3.html
    def __init__(self, base):
        self.base = ""

    def connexion(self):
        self.con = .sqlite3.connect(self.base)
        self.cur = self.con.cursor()

    def deconnexion(self):
        self.con.close()

    def fetch(self, sql):
        self.connexion()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.deconnexion()
        return result

    def execute(self, sql):
        self.connexion()
        self.cur.execute(sql)
        self.deconnexion()

    def chargersql():
        pass

    def afficher_table():
        pass
    
    def listedesrequetes():
        pass

    def infotable():
        pass

    def informations_base():
        pass

"""
import sqlite3
def database_connexion(db_file):
    connexion = None
    try:
        connexion = sqlite3.connect(db_file)
    exept Error as e:
        return e

    return connexion
conn = database_connexion("data/imb.db")

def execute_sql(connexion,sql):
    cur = connexion.cursor()
    cur.execute(sql)
    raws = cur.fetchall()
    for row in rows:
        print(row)

run_sql = execute_sql
sql = "SELECT DISTINCT types FROM title_akas"
run_sql(conn,sql)
"""