from model.tools.validator import *


class HomeSell:
    def __init__(self, name, family, nationalId, homeCode):
        self.name = name
        self.family = family
        self.nationalId = nationalId
        self.homeCode = homeCode

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
    def homeCode(self):
        return self._homeCode

    @homeCode.setter
    def homeCode(self, homeCode):
        self._homeCode = homeCode


    @property
    def nationalId(self):
        return  self._nationalId

    @nationalId.setter
    def nationalId(self, nationalId):
        self._nationalId = nationalId_validator(nationalId,"کد ملی درست نمی باشد")