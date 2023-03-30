import sqlite3

# connect to Customer list.db
conn1 = sqlite3.connect('Customer list.db')
c1 = conn1.cursor()

# connect to Nutrition list.db
conn2 = sqlite3.connect('Nutrition list.db')
c2 = conn2.cursor()

# retrieve id, name, and age columns from Customer list.db and insert into Nutrition list.db
c2.execute('''INSERT INTO Nutrition list (id, name, age)
            SELECT id, name, age
            FROM Customer list''')

# commit the changes and close the connections
conn2.commit()
conn1.close()
conn2.close()


class NutritionData():
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

    def add_data(self, id, weight, fat_percentage):
        self.c.execute("INSERT INTO Nutrition list (id, weight, fat_percentage) VALUES (?, ?, ?)",
                       (id, weight, fat_percentage))
        self.conn.commit()

    def update_data(self, id, weight=None, fat_percentage=None):
        if weight is not None:
            self.c.execute("UPDATE Nutrition list SET weight=? WHERE id=?", (weight, id))
        if fat_percentage is not None:
            self.c.execute("UPDATE Nutrition list SET fat_percentage=? WHERE id=?", (fat_percentage, id))
        self.conn.commit()

    def delete_data(self, id):
        self.c.execute("DELETE FROM Nutrition list WHERE id=?", (id,))
        self.conn.commit()

    def get_data(self, id):
        self.c.execute("SELECT * FROM Nutrition list WHERE id=?", (id,))
        return self.c.fetchone()


# create an instance of NutritionData
nutrition_data = NutritionData('Nutrition list.db')


def get_customer_data(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT id, name, age FROM Customer list")
    return c.fetchall()


# get customer data from Customer list.db
customer_data = get_customer_data('Customer list.db')

# add data to Nutrition list.db for each customer
for customer in customer_data:
    nutrition_data.add_data(customer[0], None, None)
