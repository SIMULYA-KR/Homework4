my_string = input("Напишите слово, которое сейчас пришло вам в голову: ")
print("Количество символов введенного текста:", len(my_string))
print("Я верхний регистр: ", my_string. upper())
print("Я нижний регистр: ", my_string.lower())
print("У меня нет пробелов: ", my_string.replace(" ", ""))
a = my_string[0]
print("Первый символ строки: ", a)
b = my_string[-1]
print("Последний символ строки: ", b)
