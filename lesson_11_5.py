'''Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Переопределить магические методы сравнения(равно, не равно),
сложения, вычитания, вывод на экран.
Конструктор должен производить обработку входных параметров
вида: одна строка, три числа, другой объект класса MyTime. В
остальных случаях создавать объект по-умолчанию(0-0-0).'''


class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds
        return self

    def __eq__(self, other):
        return (self.hours == other.hours) and (self.minutes == other.minutes) and (self.seconds == other.seconds)

    def __ne__(self, other):
        return (self.hours != other.hours) or (self.minutes != other.minutes) or (self.seconds != other.seconds)

    def __str__(self):
        if self.seconds > 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes > 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
        if self.hours > 24:
            self.hours = self.hours % 24

        return '{:02d}:{:02d}:{:02d}'.format(self.hours, self.minutes, self.seconds)

    def __sub__(self, other):
        self.hours -= other.hours
        self.minutes -= other.minutes
        self.seconds -= other.seconds
        if self.hours < 0:
            self.hours = -self.hours
        if self.minutes < 0:
            self.minutes = -self.minutes
        if self.seconds < 0:
            self.seconds = -self.seconds
        return self


my_time1 = MyTime(21, 28, 32)
my_time2 = MyTime(21, 37, 40)

res = my_time1 + my_time2
print(res)

print(my_time1 == my_time2)
print(my_time1 != my_time2)
print(my_time1 - my_time2)
