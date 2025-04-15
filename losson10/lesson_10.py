# def additional_logic(func):
#     def wrapper():
#         print("Some logic 1")
#         func()
#         print("Some logic 2")
#     return wrapper
#
#
# @additional_logic
# def hello():
#     print("Hello World!")
#
#
# hello()

####
# def check_permissions(func):
#     def wrapper(role):
#         if role == 'admin':
#             print("Permissions granted!")
#             func(role)
#         else:
#             print("Permission denied!")
#     return wrapper
#
#
# @check_permissions
# def get_secret_information(user_role):
#     print(f"Hi {user_role}, this is secret information.")


# # v1
# wrapper_function = check_permissions(get_secret_information)
# wrapper_function("user")
#
# # v2
# check_permissions(get_secret_information)("admin")

# get_secret_information("user")
# get_secret_information("admin")

####
# def start(func):
#     def wrapper1(name):
#         print("Hello ", end="")
#         func(name)
#     return wrapper1
#
#
# def end(func):
#     def wrapper2(name):
#         print("Goodbye ", end="")
#         func(name)
#     return wrapper2
#
#
# @start
# @end
# def hello(name):
#     print(name)
#
#
# hello("Vasya")

##
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 15)
#         func(*args, **kwargs)
#         print("*" * 15)
#
#     return inner
#
#
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 15)
#         func(*args, **kwargs)
#         print("%" * 15)
#
#     return inner
#
#
# @star
# @percent
# def printer(msg):
#     print(msg)
#
#
# printer("Hello")

####################
# import time
#
#
# current_working_status = True
# current_seconds = 1
#
#
# def delay(seconds=0, is_working=True):
#     def decorator(func):
#         if not is_working:
#             return func
#         # if seconds < 0:
#         #     return func
#
#         def wrapper(*args, **kwargs):
#             print(f"Waiting for {seconds} seconds...")
#             time.sleep(seconds)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @delay(current_seconds, current_working_status)
# def hello():
#     print("Hello")
#
#
# hello()

#########################
# closure - замыкание

# 1. вложенные функции
# 2. внешняя функция возвращает адрес вложенной функции
# 3. вложенная функция должна использовать хотя бы одну переменную из внешней функции

# def outer():
#     number = 0
#     number2 = 20
#     number3 = 30
#
#     print(number2)
#
#     def inner():
#         nonlocal number
#         number += 1
#         print(number)
#         print(number3)
#         print("*" * 10)
#
#     return inner
#
#
# result_func1 = outer()
# result_func1()
# result_func1()
#
#
# result_func2 = outer()
# result_func2()
# result_func2()
#
# print("---------------")
# result_func1()
# result_func2()


##########
# add = lambda num1: lambda num2: num1 + num2
#
# configured_add = add(3)
#
# for i in range(1, 10):
#     print(configured_add(i))

#######################
# Генераторні функції
# Генератор - це об'єкт, який відразу при створенні не обчислює значення всіх своїх елементів
# generator = (i for i in range(3))
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))  # StopIteration
# close() -> зупинка генератора
# throw() -> генератор кине виняток

# for i in generator:
#     print(i)


# def create_generator():
#     number = 1
#     while True:
#         yield number
#         number += 1
#
#
# my_gen = create_generator()
# # print(my_gen)
# # print(next(my_gen))
# # print(next(my_gen))
# # print(next(my_gen))
# # print(next(my_gen))
# #
# try:
#     for i in my_gen:
#         print(i)
#         if i > 10:
#             # my_gen.close()
#             my_gen.throw(Exception("End!"))
# except Exception as e:
#     print(e)

#########

