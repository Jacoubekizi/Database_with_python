import sqlite3

class Database():
    def __init__(self, db) -> None:
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            job TEXT,
            gender TEXT,
            contact INTEGER,
            email TEXT,
            address TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()
    
    def insert(self, name, age, job, email, gender, contact, address):
        self.cur.execute('INSERT INTO employees VALUES(NULL,?,?,?,?,?,?,?)',
                        (name, age, job, email, gender, contact, address)
                        )
        self.con.commit()
    
    def fetch(self):
        self.cur.execute('SELECT * FROM employees')
        rows = self.cur.fetchall()
        return rows
    
    def remove(self, id):
        self.cur.execute('DELETE FROM employees WHERE id = ?', (id,))
        self.con.commit()

    def update(self, id,name, age, job, email, gender, contact, address):
        self.cur.execute('UPDATE employees SET name=?,age=?,job=?,email=?,gender=?,contact=?,address=? WHERE id=?',
                        (name, age, job, email, gender, contact, address, id),
                        )
        self.con.commit()

    def get_employee(self, id):
        self.cur.execute(f'SELECT * FROM employees WHERE id={id}')
        rows = self.cur.fetchone()
        self.con.commit()
        return rows