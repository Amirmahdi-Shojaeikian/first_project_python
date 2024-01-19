import tkinter.messagebox as msg
from commponent.commponent import *
import random as rnd
from model.da.person_da import *
from entity.person import *


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
        self.win.geometry("350x400")
        self.win.title("فروش خانه")
        self.p_da = PersonDa()


        self.dataYearHome()
        self.dataFloor()
        self.dataRoom()
        self.randomnumber()

        self.name = LabelText(self.win, "نام :", 96, 50, 44)
        self.family = LabelText(self.win, "نام خانوادگی : ", 50, 80)
        self.national_code = LabelText(self.win, "کدملی : ", 80, 110, 60)
        self.creat_home = ComboBox(self.win, "سال ساخت :", 17, self.year_home_data, 60, 140, 80)
        self.floor = ComboBox(self.win, "طبقه :", 17, self.floor_data, 90, 170, 50)
        self.room = ComboBox(self.win, "تعداد  اتاق :", 17, self.room_data, 65, 200, 75)
        self.price = LabelText(self.win, "مبلغ : ", 95, 230, 45)
        self.cd_home = LabelText(self.win, "کد خانه : ", 80, 260, 60, True, self.data_random)

        Button(self.win, text="ثبت", width=10,command=self.save_click).place(x=180, y=320)
        Button(self.win, text="قبلی", width=10, command=self.back).place(x=90, y=320)

        self.win.mainloop()



    def reset_form(self):
        self.name.set("")
        self.family.set("")
        self.national_code.set("")
        self.creat_home.set("")
        self.floor.set("")
        self.room.set("")
        self.price.set("")
        self.cd_home.set("")

    def save_click(self):
        person = Person(
            self.name.get(),
            self.family.get(),
            self.national_code.get(),
            self.creat_home.get(),
            self.floor.get(),
            self.room.get(),
            self.price.get(),
            self.cd_home.get()

        )
        self.p_da.save(person)
        msg.showinfo("Save", "Home Saved")
        self.reset_form()


    def back(self):
        self.win.destroy()
        UiMainPage()

    def dataYearHome(self):
        self.year_home_data = []
        for i in range(1290, 1404):
            self.year_home_data.append(i)

    def dataFloor(self):
        self.floor_data = []
        for i in range(1, 20):
            self.floor_data.append(i)

    def dataRoom(self):
        self.room_data = []
        for i in range(1, 10):
            self.room_data.append(i)

    def randomnumber(self):
        # self.data_random = rnd.randint(2,100)
        self.data_random_number = []
        for i in range(10):
            self.data_random = rnd.randrange(1, 40, 1)
        if self.data_random in self.data_random_number:
            self.data_random = rnd.randrange(21, 60, 1)
            self.data_random_number.append(self.data_random)
        else:
            self.data_random_number.append(self.data_random)
        print(self.data_random_number)


class UiBuy:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("350x300")
        self.win.title("خرید خانه")


        self.p_da = PersonDa()

        self.name = LabelText(self.win, "نام :", 96, 50, 44)
        self.family = LabelText(self.win, "نام خانوادگی : ", 50, 80)
        self.national_code = LabelText(self.win, "کدملی : ", 80, 110, 60)
        self.cd_home = LabelText(self.win, "کد خانه : ", 80, 140, 60, False, )
        Button(self.win, text="ثبت", width=10,command=self.edit_click).place(x=180, y=190)
        Button(self.win, text="قبلی", width=10, command=self.back).place(x=90, y=190)

        self.win.mainloop()
    def reset_form(self):
        self.name.set("")
        self.family.set("")
        self.national_code.set("")
        self.cd_home.set("")

    def edit_click(self):
        person_buy = PersonBuy(
            self.name.get(),
            self.family.get(),
            self.national_code.get(),
            self.cd_home.get(),

        )
        self.p_da.edit(person_buy)
        msg.showinfo("Buy it", "buy home")
        self.reset_form()

    def back(self):
        self.win.destroy()
        UiMainPage()


class UiInquiry:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("2000x900")
        self.win.title("خرید خانه")
        self.p_da = PersonDa()



        self.table_buy = Table(self.win,
              (60, 100, 100, 100, 100, 100, 100, 100, 100,100,50),
              ("Id", "Name", "Family", "NationalId", "Creat", "Floor", "Room", "Price", "Home code","NationalId","state"),
              self.p_da.find_all_inquiry_buy(),

              10,
              50,
              15
              )
        self.table_sell = Table(self.win,
              (60, 100, 100, 100, 100, 100, 100, 100, 100,100,50),
              ("Id", "Name", "Family", "NationalId", "Creat", "Floor", "Room", "Price", "Home code","NationalId","state"),
              self.p_da.find_all_inquiry_sell(),

              10,
              400,
              15
              )


        self.search_code_home = LabelText(self.win, " کدخانه :", 1200, 50, 50)
        Button(self.win, text="جستجو", width=14,command=self.search_home_code).place(x=1250, y=100)
        # Button(self.win, text="قبلی", width=10, command=self.back).place(x=1200, y=100)



        self.search_nationalId=LabelText(self.win, " کدملی :", 1200, 200, 50)
        Button(self.win, text="جستجو", width=14,command=self.search_national_code).place(x=1250, y=250)


        LabelText(self.win, " مبلغ :", 1210, 350, 40)
        Button(self.win, text="جستجو", width=14).place(x=1255, y=400)

        LabelText(self.win, " متراژ :", 1210, 500, 40)
        Button(self.win, text="جستجو", width=14).place(x=1255, y=550)

        Button(self.win, text="قبلی", width=14).place(x=1180, y=700)
        Button(self.win, text="خروج", width=14).place(x=1320, y=700)



        self.win.mainloop()



    def back(self):
        self.win.destroy()
        UiMainPage()

    def search_home_code(self):
        # print(self.search_code_home.get())
        # self.rnt_search_buy = self.p_da.find_by_code_home_buy(int(self.search_code_home.get()))
        self.rnt_search_sell = self.p_da.find_by_code_home_sell(int(self.search_code_home.get()))

        if  self.rnt_search_sell:
            msg.showinfo("sell", "sell it")
        else:
            msg.showinfo("find", "find it")

    def search_national_code(self):
        # print(self.search_code_home.get())
        # self.rnt_search_buy = self.p_da.find_by_code_home_buy(int(self.search_nationalId.get()))
        self.rnt_search_sell = self.p_da.find_by_national_code(self.search_nationalId.get())

        if  self.rnt_search_sell:
            msg.showinfo("find", "id : " + str(self.rnt_search_sell)[2])

        else:
            msg.showinfo("not find", "not find person")

