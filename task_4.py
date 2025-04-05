# Напиши класс EmployeeSalary. Он рассчитывает почасовую заработную плату сотрудников за неделю.
class EmployeeSalary:
    # С помощью переменной hourly_payment установи почасовой уровень оплаты, равный 400.
    hourly_payment = 400
    # Проинициализируй атрибуты name, hours, rest_days, email через конструктор.
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    # Добавь метод класса get_hours(). 
    # Если значение hours неизвестно, метод рассчитывает часы, исходя из количества выходных — rest_days.
    # Формула для этого случая такая: (7 - rest_days) * 8.
    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    # Добавь метод класса get_email(). Если значение email неизвестно, метод генерирует его так: f"{name}@email.com".
    @classmethod
    def get_email(cls, name):
        return f"{name}@email.com"
    
    # Добавь метод класса set_hourly_payment(). Он меняет значение переменной hourly_payment.
    @classmethod
    def set_hourly_payment(cls, new_rate):
        cls.hourly_payment = new_rate


    # Добавь метод расчёта заработной платы salary(). Формула расчёта такая: hours * hourly_payment.
    def salary(self):
        return self.hours * self.hourly_payment
