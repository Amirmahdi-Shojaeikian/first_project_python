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
            database="realestate2"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save_person(self, person):
        self.connect()
        self.cursor.execute("INSERT INTO PERSON (NAME,FAMILY,national_id,date_birth) VALUES (%s,%s,%s,%s)"
                            , [person.name, person.family, person.nationalId, person.date_birth])
        self.disconnect(commit=True)

    def find_all_person(self):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSON")
        person_list = self.cursor.fetchall()
        self.disconnect()
        if person_list:
            return person_list

    def remove_person(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM PERSON WHERE ID=%S ", [id])
        self.disconnect(commit=True)


    def find_person_by_family(self,family):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSON where family=%s",[family])
        person_list = self.cursor.fetchall()
        self.disconnect()
        if person_list:
            return person_list
    def find_person_by_nationalId(self,nationlId):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSON where national_id=%s",[nationlId])
        person_list = self.cursor.fetchall()
        self.disconnect()
        if person_list:
            return person_list
