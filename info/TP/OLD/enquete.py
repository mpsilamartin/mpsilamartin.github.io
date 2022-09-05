import sqlite3

conn=sqlite3.connect('sql-murder-mystery.db')

cur=conn.cursor()

cur.execute('SELECT * FROM PERSON')

print(cur.fetchone())

cur.execute('SELECT * FROM crime_scene_report where  date=20180115 AND type="murder" AND city="SQL City"')


print(cur.fetchall())