from urllib import request
import json
from Models.Currency import Currency

class CurrencyManager():
    class Constants:
        base_url = "http://api.fixer.io/latest?base="

    @classmethod
    def get_currency(cls, currency_name):
        try:
            with request.urlopen(cls.Constants.base_url + currency_name) as response:
                data = response.read().decode()
                json_data = json.loads(data)
                return Currency(json_data)
        except Exception as error:
            return None

    def get_crude_dates(self):
        try:
            clean_number = []
            self.read_json  = json.loads(open("Data\\currency.json").read())
            for index in self.read_json:
                clean_number.append((index["name"]))
            return clean_number
        except Exception as error:
            return None

    def finding_equivalence(self, value):
        for index in self.read_json:
            if value == index["name"]:
                return index["short"]

    def get_initial_currency(self):
        try:
            clean_number = []
            self.read_json_initial =json.loads(open("Data\\currency.json").read())
            for index in self.read_json_initial:
                clean_number.append((index["name"]))
            return clean_number
        except Exception as error:
            return None

    def finding_initial_equivalence(self, value):
        for index in self.read_json_initial:
            if value == index["name"]:
                return index["short"]