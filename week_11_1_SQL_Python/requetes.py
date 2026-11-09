def consultation(  ):
  import sqlite3
  conn = sqlite3.connect("aeroport.db")
try:
  cur = conn.cursor()
  cur.execute("SELECT *FROM id_aeroport")
  cur.executet("SELECT * FROM nom")
  cur.execute ("SELECT *FROM ville")
  for id_aeroport, nom , ville in  cur.fetchall():
    print(id_aeroport,nom,ville)
    cur.closea()
finally:
    conn.close()
      
      
  