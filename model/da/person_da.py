import mysql.connector


class PersonDa:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="mft"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, person):
        self.connect()
        self.cursor.execute("INSERT INTO property"
                            " (NAME,FAMILY,NATIONAL_code,year_creat,floor,room,price,home_code,national_code_buyer,state)"
                            " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            [person.name, person.family, person.national_id,person.creat_home,
                             person.floor,person.room,person.price ,person.cd_home,person.national_code_buyer,person.state])
        self.disconnect(commit=True)

    def edit(self, person):
        self.connect()
        self.cursor.execute("INSERT INTO property"
                            " (NAME,FAMILY,NATIONAL_code,home_code)"
                            " VALUES (%s,%s,%s,%s)",
                            [person.name,person.family,person.national_id,person.cd_home])

        self.cursor.execute("UPDATE property SET national_code_buyer=%s ,state=%s WHERE home_code=%s  ",
                            [person.national_id, 1,person.cd_home])
        self.disconnect(commit=True)

    # def remove(self, id):
    #     self.connect()
    #     self.cursor.execute(
    #         "DELETE FROM PERSON_TBL WHERE ID=%s", [id])
    #     self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM property ")
        person_list = self.cursor.fetchall()
        self.disconnect()
        if person_list:
            return person_list

    def find_all_inquiry_buy(self):
        self.connect()
        self.cursor.execute("SELECT * FROM property where state = 0  ")
        person_list = self.cursor.fetchall()
        self.disconnect()
        if person_list:
            return person_list

    def find_all_inquiry_sell(self):
        self.connect()
        self.cursor.execute("SELECT * FROM property where state = 1 and room is not null  ")
        person_list = self.cursor.fetchall()
        self.disconnect()
        if person_list:
            return person_list


    def find_by_code_home_buy(self, cd_home):
        self.connect()
        self.cursor.execute("SELECT * FROM property WHERE home_code=%s ", [cd_home])
        person_list = self.cursor.fetchall()
        self.disconnect()
        if person_list:
            return person_list
        else:
            return None

    def find_by_code_home_sell(self, cd_home):
        self.connect()
        self.cursor.execute("SELECT * FROM property WHERE home_code=%s and state = 1 ", [cd_home])
        person_list = self.cursor.fetchall()
        self.disconnect()
        if person_list:
            return person_list
        else:
            return None


    def find_by_national_code(self, cd_national):
        self.connect()
        self.cursor.execute("SELECT * FROM property WHERE national_code=%s  ", [cd_national])
        person_list = self.cursor.fetchall()
        self.disconnect()
        if person_list:
            return person_list
        else:
            return None
