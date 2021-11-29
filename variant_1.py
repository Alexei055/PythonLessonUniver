import time


def my_decorator(func):
    def decor():
        start = time.perf_counter()
        func()
        print(f"Была вызвана функция {func.__name__}\n"
              f"Время затраченное на выполение: {time.perf_counter()-start}")
    return decor


@my_decorator
def calc_sqft_per_acre():
    length = int(input("Введите длину участка в футах: "))
    width = int(input("Введите ширину участка в футах: "))
    print(f"Площадь в акрах: {(length*width)/43560}")


@my_decorator
def calc_free_fall():
    vi = 0
    a = 9.8
    d = int(input("Введите высоту в метрах с которой упадет объект: "))
    vf = abs(vi) + 2 * a * d
    print(f"Финальная скорость: {vf} м/с")


calc_sqft_per_acre()
calc_free_fall()


