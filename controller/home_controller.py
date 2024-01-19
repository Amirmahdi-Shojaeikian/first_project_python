from model.entity.home import *
from model.entity.home_sell import *
from model.da.home_da import *
from model.da.home_sell_da import *
import tkinter.messagebox as msg


class HomeController:
    def save_home_controller(self, construction, extent, room, floor, amount, area, owner, nationalId_owner):

        home = Home(construction, extent, room, floor, amount, area, owner, nationalId_owner)
        da = HomeDa()
        da.save_home(home)
        return "خانه ثبت شد"

    def save_home_sell_controller(self, name,family,nationalId,homeCode):

        home = HomeSell(name,family,nationalId,homeCode)
        da = HomeSellDa()
        da.save_sell_home(home)
        return "خانه ثبت شد"

    def remove_home_controller(self, id):
        try:
            da = HomeDa()
            da.remove_home(id)
            return "فرد حذف شد"
        except Exception as e:
            return e

    def find_home_sell(self):
        try:
            da = HomeDa()
            return da.find_home_sell()
        except Exception as e:
            return e

    def find_home_buy(self):
        try:
            da = HomeDa()
            return da.find_home_buy()
        except Exception as e:
            return e
    def find_home_by_id_controller(self, id):
        try:
            da = HomeDa()
            return da.find_home_by_id(id)
        except Exception as e:
            return e
    def find_home_by_nationalId_controller(self,nationalId):
        try:
            da = HomeDa()
            return da.find_home_by_nationalId(nationalId)
        except Exception as e:
            return e
    def find_home_by_amount_controller(self,amount):
        try:
            da = HomeDa()
            return da.find_home_by_amount(amount)
        except Exception as e:
            return e
    def find_home_by_extent_controller(self,extent):
        try:
            da = HomeDa()
            return da.find_home_by_extent(extent)
        except Exception as e:
            return e

    def find_person_by_family_controller(self,family):
        try:
            da = HomeDa()
            return da.find_person_by_family(family)
        except Exception as e:
            return e
    def find_person_by_nationalId_controller(self,nationalId):
        try:
            da = HomeDa()
            return da.find_person_by_nationalId(nationalId)
        except Exception as e:
            return e
    def find_all_person(self):
        try:
            da = HomeDa()
            return da.find_all_person()
        except Exception as e:
            return e
