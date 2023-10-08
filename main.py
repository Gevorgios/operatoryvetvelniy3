# number = int(input("Введите число от 1 до 100: "))
# if number < 1 or number > 100: print("Ошибка! Введено число вне диапазона.")
# elif number % 3 == 0 and number % 5 == 0: print("Fizz Buzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print(number)

# number = int(input("Введите число"))
#
# for i in range(8):
#
#    print("{0}^{1} = {2}".format(number, i, number**i))


# def calculate_cost(cost, from_operator, to_operator):
#    if from_operator.lower() == to_operator.lower():
#       return cost
#    elif from_operator.lower() == "мегафон" and to_operator.lower() == "мтс":
#       return cost * 1.2
#    elif from_operator.lower() == "мтс" and to_operator.lower() == "мегафон":
#       return cost * 1.5
#    elif from_operator.lower() == "мегафон" and to_operator.lower() == "билайн":
#       return cost * 1.1
#    elif from_operator.lower() == "билайн" and to_operator.lower() == "мегафон":
#       return cost * 1.3
#    elif from_operator.lower() == "мегафон" and to_operator.lower() == "теле2":
#       return cost * 1.4
#    elif from_operator.lower() == "теле2" and to_operator.lower() == "мегафон":
#       return cost * 1.6
#    elif from_operator.lower() == "мтс" and to_operator.lower() == "билайн":
#       return cost * 1.3
#    elif from_operator.lower() == "билайн" and to_operator.lower() == "мтс":
#       return cost * 1.4
#    elif from_operator.lower() == "мтс" and to_operator.lower() == "теле2":
#       return cost * 1.5
#    elif from_operator.lower() == "теле2" and to_operator.lower() == "мтс":
#       return cost * 1.7
#    elif from_operator.lower() == "билайн" and to_operator.lower() == "теле2":
#       return cost * 1.2
#    elif from_operator.lower() == "теле2" and to_operator.lower() == "билайн":
#       return cost * 1.3
#    else:
#       return "Неверно указаны операторы"
#
#
# cost = float(input("Введите стоимость разговора: "))
# from_operator = input("Введите оператор, с которого звонят (Мегафон, МТС, Билайн или Теле2): ")
# to_operator = input("Введите оператор, на который звонят (Мегафон, МТС, Билайн или Теле2): ")
#
# result = calculate_cost(cost, from_operator, to_operator)
# print("Стоимость разговора:", result)

# # Ввод уровня продаж для трех менеджеров
# sales_manager1 = float(input("Введите уровень продаж для менеджера 1: "))
# sales_manager2 = float(input("Введите уровень продаж для менеджера 2: "))
# sales_manager3 = float(input("Введите уровень продаж для менеджера 3: "))
#
# # Расчет зарплаты для каждого менеджера
# salary_manager1 = 200 + (sales_manager1 * 0.03)
# salary_manager2 = 200 + (sales_manager2 * 0.03)
# salary_manager3 = 200 + (sales_manager3 * 0.03)
#
# # Определение лучшего менеджера
# best_manager = max(salary_manager1, salary_manager2, salary_manager3)
#
# # Начисление премии лучшему менеджеру
# salary_with_bonus = best_manager + 200
#
# # Вывод результатов на экран
# print("Зарплата менеджера 1:", salary_manager1)
# print("Зарплата менеджера 2:", salary_manager2)
# print("Зарплата менеджера 3:", salary_manager3)
# print("Лучший менеджер получит премию:", salary_with_bonus)