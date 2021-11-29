import time


def my_decorator(func):
    def decor(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        print(f"Была вызвана функция {func.__name__}\n"
              f"Время затраченное на выполение: {time.perf_counter()-start}")
    return decor


@my_decorator
def calc_sqft_per_acre(length, width):
    print(f"Площадь в акрах: {(length*width)/43560}")


@my_decorator
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


