import sqlite3

conn = sqlite3.connect('dominios.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
fh = open(fname)

for line in fh:
    line = line.rstrip()
    if line.startswith('From: '):
        words = line.split()
        email = words[1]
        pieces = email.split('@')
        org = pieces[1]

        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
conn.commit()
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
