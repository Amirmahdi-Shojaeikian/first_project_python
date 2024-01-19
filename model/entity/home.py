from model.tools.validator import *


class Home:
    def __init__(self, construction, extent, room, floor, amount, area, owner, nationalId_owner):
        self.construction = construction
        self.extent = extent
        self.room = room
        self.floor = floor
        self.amount = amount
        self.area = area
        self.owner = owner
        self.nationalId_owner = nationalId_owner
        # self.state = state

    def __repr__(self):
        return str(self.__dict__)

    def tuple(self):
        return tuple(self.__dict__.values())

    @property
    def construction(self):
        return self._construction

    @construction.setter
    def construction(self, construction):
        self._construction = construction

    @property
    def extent(self):
        return self._extent

    @extent.setter
    def extent(self, extent):
        self._extent = number_extent_validator(extent, "متزاژ درست نمی باشد")

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        self._room = room
    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, floor):
        self._floor =floor

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = number_extent_validator(amount, "مبلغ درست نمی باشد")

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        self._area = area

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = name_validator(owner, "نام درست نمی باشد")

    @property
    def nationalId_owner(self):
        return self._nationalId_owner

    @nationalId_owner.setter
    def nationalId_owner(self, nationalId_owner):
        self._nationalId_owner = nationalId_validator(nationalId_owner, "کدملی درست نمی باشد")


    # @property
    # def state(self):
    #     return self._state
    #
    # @state.setter
    # def state(self, state):
    #     self._state= state