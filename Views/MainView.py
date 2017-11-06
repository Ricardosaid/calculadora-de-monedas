from tkinter import Tk, Label, Button, Entry, N, S, E, W, StringVar, OptionMenu, LEFT
from Models.CurrencyManager import CurrencyManager
class MainView(Tk):
    class Constants:
        title = "Cambio de Moneda"
        heigth = 100
        width = 550
        input_width = 250
        separator_width = 50
        center = N + S + E + W
        left = W
        right = E
        event = "<Button-1>"
        convert_text = "Convertir"
        separator_text = "▶"
        convertion_base = "USD"
        convertion_final = "To"
        convertion_initial = "From"
        bleeding = 10

    def __init__(self, convert_handler = None):
        super().__init__()
        self.__convert_handler = convert_handler
        self.title(self.Constants.title)
        self.maxsize(width = self.Constants.width, height = self.Constants.heigth)
        self.minsize(width = self.Constants.width, height = self.Constants.heigth)
        self.__configure_grid()
        self.__configure_UI()

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight = True)
        self.grid_rowconfigure(1, weight = True)
        self.grid_rowconfigure(2, weight = True)
        self.grid_columnconfigure(0, minsize = self.Constants.input_width)
        self.grid_columnconfigure(2, minsize = self.Constants.input_width)
        self.grid_columnconfigure(1, minsize = self.Constants.separator_width)

    def __configure_UI(self):

        self.option_final = StringVar(self)
        self.option_final.set(self.Constants.convertion_final)
        self.list_of_convertions = self.convert_data_to_list()
        self.menu = OptionMenu(self, self.option_final, *self.list_of_convertions)
        self.menu.grid(row = 2, column = 2, sticky = self.Constants.right)
        self.menu.configure(bg = "light sea green", fg = "black", width = 30, font = ("Arial black", 8))

        self.option_initial = StringVar(self)
        self.option_initial.set(self.Constants.convertion_initial)
        self.list_of_inital_conversion = self.convert_initial_data_list()
        self.initial_menu = OptionMenu(self, self.option_initial, *self.list_of_inital_conversion)
        self.initial_menu.grid(row = 2, column = 0, sticky = self.Constants.left)
        self.initial_menu.configure(bg="light sea green", fg="black", width=30, font=("Arial black", 8))

        currency_name_label = Label(self)
        currency_name_label.configure(textvariable = self.option_initial)
        currency_name_label.grid(row = 0, column = 0, sticky = self.Constants.left)

        result_name_label = Label(self)
        result_name_label.configure(textvariable = self.option_final)
        result_name_label.grid(row = 0, column = 2, sticky = self.Constants.left)

        separator_label = Label(self)
        separator_label.configure(text = self.Constants.separator_text)
        separator_label.grid(row = 1, column = 1, sticky =self.Constants.center)

        self.__result_label = Label(self)
        self.__result_label.configure(text = "0")
        self.__result_label.grid(row = 1, column = 2, sticky = self.Constants.left)

        self.__convert_button = Button(self)
        self.__convert_button.configure(text = self.Constants.convert_text )
        self.__convert_button.configure(bg = "lawn green", fg = "black", font = ("Arial black", self.Constants.bleeding))
        self.__convert_button.grid(row = 2, column = 1, sticky = self.Constants.center, padx = self.Constants.bleeding, pady = self.Constants.bleeding)
        self.__convert_button.bind(self.Constants.event, self.__did_tap_convert)

        vcmd = (self.register(self.__checkNumberOnly), '%d', '%P')
        self.__currency_input = Entry(self, validate = "key", validatecommand = vcmd)
        self.__currency_input.grid(row = 1, column = 0, sticky = self.Constants.center)

    def __did_tap_convert(self, event):
        if self.__convert_handler is None:
            return
        try:
            ammount_to_convert = float(self.__currency_input.get())
        except ValueError:
            return
        else:
            self.__convert_handler(self.finding_initial_equivalence(), self.finding_equivalence_of_name(), ammount_to_convert)

    def update_result(self, text):
        self.__result_label.configure(text = text)

    def __checkNumberOnly(self, action, value_if_allowed):
        if action != '1':
            return True
        try:
            float(value_if_allowed)
        except ValueError:
            return False
        else:
            return True

    def convert_data_to_list(self):
        self.messy_list = CurrencyManager.get_crude_dates(self)
        return self.messy_list

    def finding_equivalence_of_name(self):
        self.sign_convertion = self.option_final.get()
        self.equivalence = CurrencyManager.finding_equivalence(self, self.sign_convertion)
        return self.equivalence

    def convert_initial_data_list(self):
        self.initial_options_list = CurrencyManager.get_initial_currency(self)
        return self.initial_options_list

    def finding_initial_equivalence(self):
        self.initial_sign_convertion = self.option_initial.get()
        self.initial_equivalence = CurrencyManager.finding_initial_equivalence(self, self.initial_sign_convertion)
        return self.initial_equivalence

