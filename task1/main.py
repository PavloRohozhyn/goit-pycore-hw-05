""" no module imported """

def caching_fibonacci():
    """ fibonacci """
    # cache
    cache_pool = {}
    def fibonacci(n):
        """ recursive calculate and store result into cache """
        # check if 0
        if n <= 0:
            return 0
        #check if 1
        elif n == 1:
            return 1
        # check if "n" inside cache
        elif n in cache_pool:
            return cache_pool[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            # save result of "n" in cache
            cache_pool[n] = result
            return result
    return fibonacci


def main():
    """ main function """
    fib = caching_fibonacci()
    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10)) # Виведе 55
    print(fib(15)) # Виведе 610


if __name__ == "__main__":
    main()
