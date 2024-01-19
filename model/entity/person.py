class Person:
    def __init__(self, name, family, national_id, creat_home,floor,room,price,cd_home,national_code_buyer=None,state = 0):
        self.name = name
        self.family = family
        self.national_id = national_id
        self.creat_home =creat_home
        self.floor = floor
        self.room =room
        self.price = price
        self.cd_home = cd_home
        self.national_code_buyer=national_code_buyer
        self.state =state

    def __repr__(self):
        return str(self.__dict__)

    def values(self):
        return tuple(self.__dict__.values())


class PersonBuy:
    def __init__(self, name, family, national_id,cd_home,):
        self.name = name
        self.family = family
        self.national_id = national_id
        self.cd_home = cd_home
        # self.state =state

    def __repr__(self):
        return str(self.__dict__)

    def values(self):
        return tuple(self.__dict__.values())




