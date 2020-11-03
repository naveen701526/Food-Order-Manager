import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS foods (id INTEGER PRIMARY KEY, food text, customer text, quantity text, bill text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM foods")
        rows = self.cur.fetchall()
        return rows

    def insert(self, food, customer, quantity, bill):
        self.cur.execute("INSERT INTO foods VALUES (NULL, ?, ?, ?, ?)",
                         (food, customer, quantity, bill))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM foods WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, food, customer, quantity, bill):
        self.cur.execute("UPDATE foods SET food = ?, customer = ?, quantity = ?, bill = ? WHERE id = ?",
                         (food, customer, quantity, bill, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database('store.db')
# db.insert("Pizza", "1234", "2", "160")
# db.insert("Burger", "1123", "12", "360")
# db.insert("Chciken Bucket", "12341", "2", "80")
# db.insert("Chicken Sausage Pizza", "4422", "4", "70")
# db.insert("Pineapple Pastry", "4532", "5", "180")
# db.insert("Choco Lava Cake", "6127", "12", "679")