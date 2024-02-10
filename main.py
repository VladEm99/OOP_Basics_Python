def calculator():
    print("Калькулятор")
    action = int(input("Выберите действие:\n1 - деление\n2 - умножение\n3 - сложение\n\
4 - вычитание\n5 - закрыть калькулятор\nВыбор: "))
    firstValue = int(input("Введите первое число: "))
    secondValue = int(input("Введите второе число: "))
    while True:
        try:
            if action == 1:
                print("Результат: " + str(firstValue / secondValue))
                calculator()
            elif action == 2:
                print(str("Результат: " + firstValue * secondValue))
                calculator()
            elif action == 3:
                print(str("Результат: " + firstValue + secondValue))
                calculator()
            elif action == 4:
                print(str("Результат: " + firstValue - secondValue))
                calculator()
            elif action == 5:
                quit()
            else:
                print("Выберите цифру от 1 до 5")
                calculator()
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            calculator()
calculator()


