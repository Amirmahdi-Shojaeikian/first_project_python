import mysql.connector


class HomeDa:
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

    def save_home(self, home):
        self.connect()
        self.cursor.execute \
            ("insert into home (construction, extent, room, floor, amount, area, owner, nationalId_owner,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
             [
                 home.construction, home.extent, home.room, home.floor, home.amount, home.area, home.owner,
                 home.nationalId_owner,0
             ])
        self.disconnect(commit=True)


    def find_all_home(self):
        self.connect()
        self.cursor.execute("SELECT * FROM HOME")
        home_list = self.cursor.fetchall()
        self.disconnect()
        if home_list:
            return home_list

    def remove_home(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM HOME WHERE ID=%S ", [id])
        self.disconnect(commit=True)


    def find_home_sell(self):
        self.connect()
        self.cursor.execute("SELECT * FROM HOME WHERE STATUS=1")
        home_list = self.cursor.fetchall()
        self.disconnect()
        if home_list:
            return home_list

    def find_home_buy(self):
        self.connect()
        self.cursor.execute("SELECT * FROM HOME WHERE STATUS=0")
        home_list = self.cursor.fetchall()
        self.disconnect()
        if home_list:
            return home_list

    def find_home_by_id(self,id):
        self.connect()
        self.cursor.execute("SELECT * FROM HOME WHERE id=%s and status = 0",[id])
        home_list = self.cursor.fetchall()
        self.disconnect()
        if home_list:
            return home_list

    def find_home_by_nationalId(self, nationaId):
        self.connect()
        self.cursor.execute("SELECT * FROM HOME WHERE nationalId_owner=%s and status = 0", [nationaId])
        home_list = self.cursor.fetchall()
        self.disconnect()
        if home_list:
            return home_list

    def find_home_by_amount(self, amount):
        self.connect()
        self.cursor.execute("SELECT * FROM HOME WHERE amount=%s and status = 0 ", [amount])
        home_list = self.cursor.fetchall()
        self.disconnect()
        if home_list:
            return home_list
    def find_home_by_extent(self, extent):
        self.connect()
        self.cursor.execute("SELECT * FROM HOME WHERE extent=%s and status = 0", [extent])
        home_list = self.cursor.fetchall()
        self.disconnect()
        if home_list:
            return home_list
    def find_person_by_family(self,family):
        self.connect()
        self.cursor.execute("SELECT * FROM home_sell where family=%s",[family])
        person_list = self.cursor.fetchall()
        self.disconnect()
        if person_list:
            return person_list
    def find_person_by_nationalId(self,nationlId):
        self.connect()
        self.cursor.execute("SELECT * FROM home_sell where nationalId=%s",[nationlId])
        person_list = self.cursor.fetchall()
        self.disconnect()
        if person_list:
            return person_list


    def find_all_person(self):
        self.connect()
        self.cursor.execute("SELECT * FROM home_sell")
        home_list = self.cursor.fetchall()
        self.disconnect()
        if home_list:
            return home_list
