# начнем просто с калькулятора

counter_while = 0
new_loop = 'y'

while new_loop == 'y':
    counter_while = counter_while + 1
    counter = 0
    first_number = input('введите первое число ')
    operator = input('введите оператор ')
    second_number = input('введите второе число ')

    if operator == '+':
        counter = float(first_number) + float(second_number)
        print("результат равен " + str(counter))
    elif operator == '-':
        counter = float(first_number) - float(second_number)
        print("результат равен " + str(counter))
    elif operator == '*':
        counter = float(first_number) * float(second_number)
        print("результат равен " + str(counter))
    try:
        if operator == '/':
            counter = float(first_number) / float(second_number)
            print("результат равен " + str(counter))
    except ZeroDivisionError:
        print("не стоит делить на ноль")

    print(" Количество выполненных циклов операций : " + str(counter_while))
    new_loop = input(" Ещё разок? (y/n) : ")
    if new_loop == "y":
        continue
    if new_loop == "n":
        print(" Спасибо. До новых встреч")
        break
    if new_loop != "y" or "n":
       print("введен неправильный символ")
       new_loop = input(" Ещё разок? (y/n) : ")
