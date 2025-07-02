class User:
    def __init__(self, db, name):
        self.db = db
        self.user_id = str(uuid.uuid4())
        self.name = name

    def add_to_db(self):
        self.db.cursor.execute('''
            INSERT INTO users (user_id, name)
            VALUES (?, ?)
        ''', (self.user_id, self.name))
        self.db.conn.commit()
        print(f"User '{self.name}' added successfully.")