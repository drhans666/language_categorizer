import sqlite3
import datetime


def create_table():
    conn = sqlite3.connect('database/language_categorizer.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS samples'
              '(id INTEGER PRIMARY KEY, datestamp TEXT, keywords TEXT,'
              ' lang_code TEXT, lang_name TEXT, lang_text TEXT, link TEXT)')


def data_entry(links, texts, lang_codes, lang_names, keys):
    conn = sqlite3.connect('database/language_categorizer.db')
    c = conn.cursor()
    # searches database for last cycle nr, so already named cycles wont be repeated
    c.execute("SELECT max(id) FROM samples")
    for row in c.fetchall():
        id_nr = (row[0])
        if id_nr is None:
            id_nr = 0
        else:
            pass
    id_nr = id_nr + 1
    # populates database with date, cycle nr, measure nr and measure value
    c.execute('BEGIN')
    for i in range(len(lang_names)):
        datestamp = str(datetime.datetime.now())
        c.execute("INSERT INTO samples "
                  "(id, datestamp, keywords, lang_code, lang_name, lang_text, link) "
                  "VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (id_nr, datestamp, keys[-1], lang_codes[i], lang_names[i], texts[i], links[i]))
        id_nr = id_nr + 1
    conn.commit()
    c.close()
    conn.close()


# gets full language name based on language code
def get_language_name(lang_code):
    conn = sqlite3.connect('database/language_categorizer.db')
    c = conn.cursor()
    c.execute("SELECT english "
              "FROM langs "
              "WHERE alpha3b = ? OR alpha3t = ? OR alpha2 = ?",
              (lang_code, lang_code, lang_code))
    lang_name = c.fetchone()
    return lang_name[0]


# feeds classification algorythm with data
def get_db_data(limit):
    conn = sqlite3.connect('database/language_categorizer.db')
    c = conn.cursor()
    c.execute("SELECT id, lang_text, lang_name "
              "FROM samples "
              "WHERE lang_name IN (SELECT lang_name "
              "FROM samples "
              "GROUP BY lang_name "
              "HAVING COUNT(lang_name) > 160) "
              "LIMIT %s" %limit)
    data = c.fetchall()
    return data
