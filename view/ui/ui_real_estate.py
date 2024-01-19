import tkinter.messagebox as msg
from controller.home_controller import *
from controller.person_controller import *

from model.da.home_da import *
from view.component.commponent import *
import random as rnd
from model.da.person_da import *
from model.entity.person import *
from model.entity.home import *


class UiMainPage:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("300x220")
        self.win.title("main page")

        Label()
        # Button

        Button(self.win, text="فروش", width=10, command=self.next_sell).place(x=110, y=50)
        Button(self.win, text="خرید", width=10, command=self.next_buy).place(x=110, y=90)
        Button(self.win, text="استعلام", width=10, command=self.inquiry).place(x=110, y=130)

        self.win.mainloop()

    def inquiry(self):
        self.win.destroy()
        UiInquiry()

    def next_sell(self):
        self.win.destroy()
        UiSell()

    def next_buy(self):
        self.win.destroy()
        UiBuy()


class UiSell:
    def __init__(self):
        self.data_random = None
        self.data_random_number = None
        self.win = Tk()
        self.win.geometry("350x450")
        self.win.title("اطلاعات فروشنده")
        self.p_controller = PersonController()
        self.h_controller = HomeController()

        self.name = LabelText(self.win, "نام :", 98, 50, 42)
        self.family = LabelText(self.win, "نام خانوادگی : ", 52, 80, 88)
        self.national_code = LabelText(self.win, "کدملی : ", 82, 110, 58)
        self.date_birth = LabelText(self.win, " سال تولد : ", 68, 140, 72)
        self.construction = LabelText(self.win, "سال ساخت :", 60, 170, 80)
        self.floor = LabelText(self.win, "طبقه :", 90, 200, 50)
        self.room = LabelText(self.win, "تعداد  اتاق :", 65, 230, 75)
        self.area = LabelText(self.win, "منطقه :", 83, 260, 57)
        self.extent = LabelText(self.win, "متراژ : ", 93, 290, 47)
        self.price = LabelText(self.win, "مبلغ : ", 95, 320, 45)

        Button(self.win, text="بعدی", width=10, command=self.save_click).place(x=180, y=370)
        Button(self.win, text="قبلی", width=10, command=self.back).place(x=90, y=370)

        self.win.mainloop()

    def reset_form(self):
        self.name.set("")
        self.family.set("")
        self.national_code.set("")
        self.date_birth.set("")

    def save_click(self):
        try:
            self.p_controller.save_person_controller(
                self.name.get(),
                self.family.get(),
                self.national_code.get(),
                self.date_birth.get()
            )

            self.h_controller.save_home_controller(
                self.construction.get(),
                self.extent.get(),
                self.room.get(),
                self.floor.get(),
                self.price.get(),
                self.area.get(),
                self.family.get(),
                self.national_code.get()
            )

            msg.showinfo("موفق", "اطلاعات ثبت شد")
            self.win.destroy()
            UiMainPage()

        except Exception as e:
            msg.showerror("خطا", str(e))
            # UiSell2(self.family.get(), self.national_code.get())

    def back(self):
        self.win.destroy()
        UiMainPage()


class UiBuy:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("350x300")
        self.win.title("خرید خانه")
        self.h_controller= HomeController()



        self.name = LabelText(self.win, "نام :", 96, 50, 44)
        self.family = LabelText(self.win, "نام خانوادگی : ", 50, 80)
        self.national_code = LabelText(self.win, "کدملی : ", 80, 110, 60)
        self.cd_home = LabelText(self.win, "کد خانه : ", 80, 140, 60, False, )
        Button(self.win, text="ثبت", width=10, command=self.edit_click).place(x=180, y=190)
        Button(self.win, text="قبلی", width=10, command=self.back).place(x=90, y=190)

        self.win.mainloop()

    def reset_form(self):
        self.name.set("")
        self.family.set("")
        self.national_code.set("")
        self.cd_home.set("")

    def edit_click(self):
        try:
            self.h_controller.save_home_sell_controller(
                self.name.get(),
                self.family.get(),
                self.national_code.get(),
                self.cd_home.get()
            )

            msg.showinfo("موفق", "اطلاعات ثبت شد")
            self.win.destroy()
            UiMainPage()
        except Exception as e:
            msg.showerror("خطا", str(e))

    def back(self):
        self.win.destroy()
        UiMainPage()


class UiInquiry:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("1200x600")
        self.win.title("استعلام خانه")
        self.h_controller = HomeController()

        self.table_buy = Table(self.win,
                               (60, 100, 100, 100, 100, 100, 100, 100, 100, 50),
                               ("Id", "construction", "extent", "room", "floor", "amount", "area", "owner"
                                , "nationalId_owner",
                                "state"),
                               self.h_controller.find_home_buy(),
                               10,
                               25,
                               12
                               )
        # self.table_sell = Table(self.win,
        #                         (60, 100, 100, 100, 100, 100, 100, 100, 100, 50),
        #                         ("Id", "construction", "extent", "room", "floor", "amount", "area", "owner",
        #                          "nationalId_owner",
        #                          "state"),
        #                         self.h_controller.find_home_sell(),
        #                         10,
        #                         300,
        #                         12
        #                         )

        self.search_code_home = LabelText(self.win, " کدخانه :", 970, 25, 50)
        Button(self.win, text="جستجو", width=14, command=self.search_home_code).place(x=1028, y=60)
        # Button(self.win, text="قبلی", width=10, command=self.back).place(x=1200, y=100)

        self.search_nationalId = LabelText(self.win, " کدملی :", 970, 120, 50)
        Button(self.win, text="جستجو", width=14, command=self.search_national_code).place(x=1028, y=155)

        self.price = LabelText(self.win, " مبلغ :", 978, 210, 40)
        Button(self.win, text="جستجو", width=14,command=self.search_price).place(x=1028, y=240)

        self.extent = LabelText(self.win, " متراژ :", 978, 300, 40)
        Button(self.win, text="جستجو", width=14,command=self.search_extent).place(x=1028, y=330)

        Button(self.win, text="استعلام فروشنده", width=14 , command=self.next_person_seller).place(x=1027, y=400)
        Button(self.win, text="استعلام خریدار", width=14 , command=self.next_person_buyer).place(x=1027, y=440)
        Button(self.win, text="قبلی", width=14 , command=self.back).place(x=1027, y=480)
        Button(self.win, text="خروج", width=14 , command=self.end).place(x=1027, y=520)

        self.win.mainloop()


    def next_person_buyer(self):
        self.win.destroy()
        UiSearchPersonBuyer()

    def next_person_seller(self):
        self.win.destroy()
        UiSearchPersonSeller()

    def end(self):
        self.win.destroy()
    def back(self):
        self.win.destroy()
        UiMainPage()

    def search_home_code(self):
        self.finded_by_id =  self.h_controller.find_home_by_id_controller(self.search_code_home.get())

        if self.finded_by_id:
            self.table_sell = Table(self.win,
                                    (60, 100, 100, 100, 100, 100, 100, 100, 100, 50),
                                    ("Id", "construction", "extent", "room", "floor", "amount", "area", "owner",
                                     "nationalId_owner",
                                     "state"),
                                    self.finded_by_id,
                                    10,
                                    300,
                                    12
                                    )
        else:
            msg.showinfo("err", "not found")

    def search_national_code(self):
        self.finded_by_nationalId =  self.h_controller.find_home_by_nationalId_controller(self.search_nationalId.get())

        if self.finded_by_nationalId:
            self.table_sell = Table(self.win,
                                    (60, 100, 100, 100, 100, 100, 100, 100, 100, 50),
                                    ("Id", "construction", "extent", "room", "floor", "amount", "area", "owner",
                                     "nationalId_owner",
                                     "state"),
                                    self.finded_by_nationalId,
                                    10,
                                    300,
                                    12
                                    )
        else:
            msg.showinfo("err", "not found")
    def search_price(self):
        self.finded_by_price =  self.h_controller.find_home_by_amount_controller(self.price.get())

        if self.finded_by_price:
            self.table_sell = Table(self.win,
                                    (60, 100, 100, 100, 100, 100, 100, 100, 100, 50),
                                    ("Id", "construction", "extent", "room", "floor", "amount", "area", "owner",
                                     "nationalId_owner",
                                     "state"),
                                    self.finded_by_price,
                                    10,
                                    300,
                                    12
                                    )
        else:
            msg.showinfo("err", "not found")
    def search_extent(self):
        self.finded_by_extent=  self.h_controller.find_home_by_extent_controller(self.extent.get())

        if self.finded_by_extent:
            self.table_sell = Table(self.win,
                                    (60, 100, 100, 100, 100, 100, 100, 100, 100, 50),
                                    ("Id", "construction", "extent", "room", "floor", "amount", "area", "owner",
                                     "nationalId_owner",
                                     "state"),
                                    self.finded_by_extent,
                                    10,
                                    300,
                                    12
                                    )
        else:
            msg.showinfo("err", "not found")



class UiSearchPersonSeller:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("750x350")
        self.win.title("استعلام فروشنده")
        self.p_controller = PersonController()

        self.table_sell = Table(self.win,
                                (60, 100, 100, 100, 100),
                                ("Id","name","family","nationalId","date_birth"),
                                self.p_controller.find_all_person(),
                                10,
                                25,
                                12
                                )
        self.family = LabelText(self.win, " نام خانوادگی:", 500, 25, 80)
        Button(self.win, text="جستجو", width=14 , command=self.searche_family).place(x=580, y=60)

        self.nationalId = LabelText(self.win, " کدملی :", 528, 100, 50)
        Button(self.win, text="جستجو", width=14 , command=self.searche_nationalId).place(x=580, y=140)

        Button(self.win, text="قبلی", width=10, command=self.back).place(x=595, y=230)
        Button(self.win, text="بروزرسانی", width=10, command=self.fresh_table).place(x=595, y=200)



        self.win.mainloop()

    def fresh_table(self):

        self.table_sell = Table(self.win,
                                (60, 100, 100, 100, 100),
                                ("Id","name","family","nationalId","date_birth"),
                                self.p_controller.find_all_person(),
                                10,
                                25,
                                12
                                )

    def searche_family(self):
        self.finded_by_family= self.p_controller.find_person_by_family_controller(self.family.get())

        if self.finded_by_family:
            self.table_sell = Table(self.win,
                                    (60, 100, 100, 100, 100),
                                    ("Id", "name", "family", "nationalId", "date_birth"),
                                    self.finded_by_family,
                                    10,
                                    25,
                                    12
                                    )
        else:
            msg.showinfo("err", "not found")

    def searche_nationalId(self):
        self.finded_by_nationalId= self.p_controller.find_person_by_nationalId_controller(self.nationalId.get())

        if self.finded_by_nationalId:
            self.table_sell = Table(self.win,
                                    (60, 100, 100, 100, 100),
                                    ("Id", "name", "family", "nationalId", "date_birth"),
                                    self.finded_by_nationalId,
                                    10,
                                    25,
                                    12
                                    )
        else:
            msg.showinfo("err", "not found")


    def back(self):
        self.win.destroy()
        UiInquiry()


class UiSearchPersonBuyer:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("750x350")
        self.win.title("استعلام خریدار")
        self.h_controller = HomeController()

        self.table_sell = Table(self.win,
                                (60, 100, 100, 100, 100),
                                ("Id","name","family","nationalId","code_home"),
                                self.h_controller.find_all_person(),
                                10,
                                25,
                                12
                                )
        self.family = LabelText(self.win, " نام خانوادگی:", 500, 25, 80)
        Button(self.win, text="جستجو", width=14 , command=self.searche_family).place(x=580, y=60)

        self.nationalId = LabelText(self.win, " کدملی :", 528, 100, 50)
        Button(self.win, text="جستجو", width=14 , command=self.searche_nationalId).place(x=580, y=140)

        Button(self.win, text="بروزرسانی", width=10, command=self.fresh_table).place(x=595, y=200)
        Button(self.win, text="قبلی", width=10, command=self.back).place(x=595, y=230)


        self.win.mainloop()



    def fresh_table(self):

        self.table_sell = Table(self.win,
                                (60, 100, 100, 100, 100),
                                ("Id","name","family","nationalId","date_birth"),
                                self.h_controller.find_all_person(),
                                10,
                                25,
                                12
                                )

    def searche_family(self):
        self.finded_by_family= self.h_controller.find_person_by_family_controller(self.family.get())

        if self.finded_by_family:
            self.table_sell = Table(self.win,
                                    (60, 100, 100, 100, 100),
                                    ("Id", "name", "family", "nationalId", "date_birth"),
                                    self.finded_by_family,
                                    10,
                                    25,
                                    12
                                    )
        else:
            msg.showinfo("err", "not found")

    def searche_nationalId(self):
        self.finded_by_nationalId= self.h_controller.find_person_by_nationalId_controller(self.nationalId.get())

        if self.finded_by_nationalId:
            self.table_sell = Table(self.win,
                                    (60, 100, 100, 100, 100),
                                    ("Id", "name", "family", "nationalId", "date_birth"),
                                    self.finded_by_nationalId,
                                    10,
                                    25,
                                    12
                                    )
        else:
            msg.showinfo("err", "not found")


    def back(self):
        self.win.destroy()
        UiInquiry()

