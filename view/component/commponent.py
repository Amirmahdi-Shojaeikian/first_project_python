from tkinter import *
import tkinter.ttk as ttk


class LabelText:
    def __init__(self, master, lable, x, y, distance=90, state=False, data=None):
        if state == False:
            Label(master, text=lable).place(x=x, y=y)
            self.value = StringVar()
            Entry(master, textvariable=self.value).place(x=x + distance, y=y)
        else:
            Label(master, text=lable).place(x=x, y=y)
            self.value = StringVar()
            Entry(master, textvariable=self.value, state=DISABLED).place(x=x + distance, y=y)
            self.value.set(data)

    def get(self):
        return self.value.get()

    def set(self, value):
        self.value.set(value)

class ComboBox:
    def __init__(self, master, lable, width, data_list, x, y, distance=50, text=None):
        Label(master, text=lable).place(x=x, y=y)
        self.combo_value = StringVar()
        if self.combo_value:
            self.combo_value.set(text)
        self.combo = ttk.Combobox(master, width=width, values=data_list, textvariable=self.combo_value)
        self.combo.grid(column=1, row=15)
        self.combo.current(0)
        self.combo.place(x=x + distance, y=y)

    def get(self):
        return self.combo_value.get()

    def set(self, value):
        self.combo_value.set(value)

class Table:
    def __init__(self, master, columns, headings, data_list, x, y, height):
        self.select_item = None
        self.table = ttk.Treeview(master, columns=tuple(range(len(headings))), height=height, show="headings")

        for i in range(len(headings)):
            self.table.column(i, width=columns[i])
            self.table.heading(i, text=headings[i])

        self.refresh_table(data_list)


        self.table.place(x=x, y=y)


    def refresh_table(self, data_list):
        if data_list:
            for item in self.table.get_children():
                self.table.delete(item)
            for data in data_list:
                self.table.insert("", END, values=data)
                #
                # if data[10] == 0:
                #     self.tag = "buy"
                #     print("buy")
                #     self.table.tag_configure(self.tag, background="green")
                # else:
                #     self.tag = "sell"
                #     print("sell")
                #     self.table.tag_configure(self.tag, background="yellow")
