import sqlite3

import pandas

# creates lists from csv columns
colnames = ['alpha3b', 'alpha3t', 'alpha2', 'English', 'French']
data = pandas.read_csv('language-codes-full.csv', names=colnames)
english = data.English.tolist()
french = data.French.tolist()
alpha3b = data.alpha3b.tolist()
alpha3t = data.alpha3t.tolist()
alpha2 = data.alpha2.tolist()

# deletes csv headers from lists
english.pop(0)
french.pop(0)
alpha3b.pop(0)
alpha3t.pop(0)
alpha2.pop(0)

# populates database with data
conn = sqlite3.connect('language_categorizer.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS langs(id INTEGER PRIMARY KEY, alpha3b TEXT,'
          ' alpha3t TEXT, alpha2 TEXT, english TEXT, french TEXT)')

c.execute('BEGIN')
for i in range(len(english)):
    id_nr = i + 1
    c.execute("INSERT INTO langs (id, alpha3b, alpha3t, alpha2, english, french)"
              " VALUES (?, ?, ?, ?, ?, ?)",
              (id_nr, alpha3b[i], alpha3t[i], alpha2[i], english[i], french[i]))
    id_nr = id_nr + 1
conn.commit()
c.close()
conn.close()
