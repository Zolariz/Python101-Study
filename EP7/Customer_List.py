import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('Customer list.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT, email TEXT, age INTEGER, address TEXT)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM customers")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, email, age, address):
        self.cur.execute("INSERT INTO customers VALUES (NULL, ?, ?, ?, ?)", (name, email, age, address))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM customers WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, email, age, address):
        self.cur.execute("UPDATE customers SET name=?, email=?, age=?, address=? WHERE id=?",
                         (name, email, age, address, id))
        self.conn.commit()

    def search(self, keyword):
        self.cur.execute("SELECT * FROM customers WHERE name LIKE ? OR email LIKE ? OR address LIKE ?",
                         ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()
