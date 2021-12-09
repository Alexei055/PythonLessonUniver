# import time


# def my_decorator(func):
#     def decor(*args, **kwargs):
#         start = time.perf_counter()
#         func(*args, **kwargs)
#         print(f"Была вызвана функция {func.__name__}\n"
#               f"Время затраченное на выполение: {time.perf_counter() - start}")
#
#     return decor



def calc_sqft_per_acre(length, width):
    print(f"Площадь в акрах: {(length * width) / 43560}")



def calc_free_fall(d):
    vi = 0
    a = 9.8
    vf = abs(vi) + 2 * a * d
    print(f"Финальная скорость: {vf} м/с")


length = int(input("Введите длину участка в футах: "))
width = int(input("Введите ширину участка в футах: "))

calc_sqft_per_acre(length, width)

d = int(input("Введите высоту в метрах с которой упадет объект: "))
calc_free_fall(d)



def what_month_days(month):
    month = month.lower()
    month_name_and_days = {"январь": 31, "февраль": 28, "март": 31, "апрель": 30, "май": 31,
                           "июнь": 30, "июль": 31, "август": 31, "сентябрь": 30, "октябрь": 31,
                           "ноябрь": 30, "декабрь": 31}
    if month in month_name_and_days:
        print(f"В этом месяце {month_name_and_days[month]} дней")
    else:
        print("Такого месяца нет")


m = str(input("Введите название месяца: "))

what_month_days(m)
