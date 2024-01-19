from model.tools.validator import *


class Person:
    def __init__(self, name, family, nationalId, date_birth):
        self.name = name
        self.family = family
        self.nationalId = nationalId
        self.date_birth = date_birth

    def __repr__(self):
        return str(self.__dict__)

    def tuple(self):
        return tuple(self.__dict__.values())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name_validator(name, "نام درست نمی باشد")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = name_validator(family, "نام خانوادگی درست نمی باشد")

    @property
    def date_birth(self):
        return self._dateBirth

    @date_birth.setter
    def date_birth(self, date_birth):
        self._dateBirth = date_birth_validator(date_birth, "تاریخ تولد درست نمی باشد")


    @property
    def nationalId(self):
        return  self._nationalId

    @nationalId.setter
    def nationalId(self, nationalId):
        self._nationalId = nationalId_validator(nationalId,"کد ملی درست نمی باشد")