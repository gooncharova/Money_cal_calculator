import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_date = dt.datetime.now().date()
        day_sum = 0
        for record in self.records:
            if record.date == today_date:
                day_sum += record.amount
        return day_sum

    def get_week_stats(self):
        week_sum = 0
        today_date = dt.datetime.now().date()
        week_date = dt.datetime.now().date() - dt.timedelta(weeks=1)
        for record in self.records:
            if week_date < record.date <= today_date:
                week_sum += record.amount
        return week_sum


class Record:
    def __init__(self, amount, comment='', date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.limit - self.get_today_stats()
        if calories_remained > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей'
                    f' калорийностью не более {calories_remained} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    RUB_RATE = 1.00
    USD_RATE = 73.44
    EURO_RATE = 80.39

    def get_today_cash_remained(self, currency):
        currencies = ['rub', 'usd', 'eur']
        if currency in currencies:
            if currency == 'rub':
                currency = 'руб'
                rate = self.RUB_RATE
            elif currency == 'usd':
                currency = 'USD'
                rate = self.USD_RATE
            else:
                currency = 'Euro'
                rate = self.EURO_RATE
        else:
            return 'Используйте только rub, usd или eur'

        cash_remained = (self.limit - self.get_today_stats())/rate
        if cash_remained > 0:
            return f'На сегодня осталось {round(cash_remained, 2)} {currency}'
        elif cash_remained == 0:
            return 'Денег нет, держись'
        else:
            cash_remained = abs(cash_remained)
            return f'Денег нет, держись: твой долг -'\
                   f' {round(cash_remained, 2)} {currency}'
