import sqlite3
conn = sqlite3.connect("aeroports.db")
try:
  cur = conn.cursor()
  cur.execute ("SELECT * FROM aeroports.db")
  for id_vol, id_depat, date_vol in cur.fetchall():
   print(id_vol,date_vol, id_depat)
  cur.close()
finally:
 conn.close()
            
