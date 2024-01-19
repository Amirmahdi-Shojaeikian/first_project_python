from model.entity.person import *
from model.da.person_da import *


class PersonController:
    def save_person_controller(self, name, family, national_id, date_birth):

            person = Person(name, family, national_id, date_birth)
            da = PersonDa()
            da.save_person(person)
            return "فرد ثبت شد"

    def remove_person_controller(self, id):
        try:
            da = PersonDa()
            da.remove_person(id)
            return "فرد حذف شد"
        except Exception as e:
            return e

    def find_all_person(self):
        try:
            da = PersonDa()
            return da.find_all_person()
        except Exception as e:
            return e

    def find_person_by_family_controller(self,family):
        try:
            da = PersonDa()
            return da.find_person_by_family(family)
        except Exception as e:
            return e
    def find_person_by_nationalId_controller(self,nationalId):
        try:
            da = PersonDa()
            return da.find_person_by_nationalId(nationalId)
        except Exception as e:
            return e
