# Калькулятор денег и калорий

Файл **Money_calories_calculator.py** содержит 2 калькулятора, унаследованных от класса ```Calculator```:  

**1.** Калькулятор денег ```cash_calculator```. Содержит следующие функции:
- Сохраняет новую запись о расходах методом ```add_record()```
- Считает, сколько денег потрачено сегодня методом ```get_today_stats()```
- Определяет, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод ```get_today_cash_remained(currency)```. Принимает на вход код валюты: одну из строк "rub", "usd" или "eur". Возвращает сообщение о состоянии дневного баланса в этой валюте, округляя сумму до двух знаков после запятой (до сотых):  
**"На сегодня осталось N руб/USD/Euro"** — в случае, если лимит limit не достигнут, или   
**"Денег нет, держись"**, если лимит достигнут, или   
**"Денег нет, держись: твой долг - N руб/USD/Euro"**, если лимит превышен.
- Считает, сколько денег потрачено за последние 7 дней — метод ```get_week_stats()```

**2.** Калькулятор калорий ```calories_calculator```. Содержит следующие функции:
- Сохраняет новую запись о приёме пищи методом ```add_record()```
- Считает, сколько калорий уже съедено сегодня методом ```get_today_stats()```
- Определяет, сколько ещё калорий можно/нужно получить сегодня методом ```get_calories_remained()```. Возвращает ответ  
**"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал"**, если лимит limit не достигнут, или  
**"Хватит есть!"**, если лимит достигнут или превышен.
- Считает, сколько калорий получено за последние 7 дней методом ```get_week_stats()```

Родительский класс ```Calculator``` имеет следующие функции: 
- Хранит записи
- Знает дневной лимит 
- Суммирует записи за конкретные даты 

Конструктор класса ```Calculator``` принимает один аргумент — число limit (дневной лимит трат/калорий, который задал пользователь). 

Класс ```Record``` умеет сохранять записи:
- Число amount (денежная сумма или количество килокалорий)
- Дату создания записи date (передаётся в явном виде в конструктор, либо присваивается значение по умолчанию — текущая дата)
- Комментарий comment, поясняющий, на что потрачены деньги или откуда взялись калории.

## Используемые технологии и инструменты

- Python 3.8.2
- Модуль datetime
- Принципы объектно-ориентрованного програмирования

## Проверка работоспособности

Для проверки можно создать калькулятор денег с дневным лимитом 1000

```cash_calculator = CashCalculator(1000)```
        
Добавить пару новых записей без указания даты в параметрах, так как по умолчанию к записи должна автоматически добавиться сегодняшняя дата

```cash_calculator.add_record(Record(amount=145, comment="кофе"))```
```cash_calculator.add_record(Record(amount=400, comment="обед"))```

А здесь укажем дату

```cash_calculator.add_record(Record(amount=3000, comment="Свитер", date="08.11.2019"))```

Выведем результат на экран
                
```print(cash_calculator.get_today_cash_remained("rub"))```

В итоге должно получиться 

```На сегодня осталось 455 руб```
