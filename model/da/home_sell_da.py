import mysql.connector


class HomeSellDa:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="realestate2"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save_sell_home(self, home_sell):
        self.connect()
        self.cursor.execute("INSERT INTO home_sell (name, family, nationalId, home_code) VALUES (%s,%s,%s,%s)"
                            , [home_sell.name,home_sell.family,home_sell.nationalId,home_sell.homeCode])

        self.cursor.execute("UPDATE home SET status=1 WHERE ID=%s ",[home_sell.homeCode])
        self.disconnect(commit=True)

    def find_all_home_sell(self):
        self.connect()
        self.cursor.execute("SELECT * FROM home_sell")
        home_sell_list = self.cursor.fetchall()
        self.disconnect()
        if home_sell_list:
            return home_sell_list

    def remove_home_sell(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM home_sell WHERE ID=%S ", [id])
        self.disconnect(commit=True)
