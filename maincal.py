from Views.MainView import MainView
from Models.CurrencyManager import CurrencyManager

class MainApp():
    def __init__(self):
        self.__master = MainView(convert_handler = self.__convert)

    def run(self):
        self.__master.mainloop()

    def __convert(self, from_currency, to_currency, ammount):
        self.initial_currency = from_currency
        self.initial_convertion = CurrencyManager.get_currency(self.initial_currency)
        result = str(self.initial_convertion.get_convertion(to_currency, ammount))
        self.__master.update_result(result)


if __name__ == "__main__":
    app = MainApp()
    app.run()