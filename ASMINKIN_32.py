# 32. Действительный номерной знак машины? Допустим, в нашей стране старый формат номерных знаков автомобилей состоял из трех заглавных букв,
# следом за которыми шли три цифры. После того как все возможные номера были использованы, формат был изменен на четыре
# цифры, предшествующие трем заглавным буквам. Напишите программу, запрашивающую у пользователя номерной знак машины и
# оповещающую о том, для какого формата подходит данная последовательность символов: для старого или нового. Если введенная
# последовательность не соответствует ни одному из двух форматов, укажите это в сообщении;
number_plate = input("Введите номерной знак машины: ")

if len(number_plate) == 6: # проверяем длину введенной последовательности символов
    if number_plate[:3].isalpha() and number_plate[3:].isdigit():
        print("Данная последовательность символов соответствует старому формату номерного знака.")
    else:
        print("Данная последовательность символов не соответствует ни одному из двух форматов.")
elif len(number_plate) == 7:
    if number_plate[:4].isdigit() and number_plate[4:].isalpha():
        print("Данная последовательность символов соответствует новому формату номерного знака.")
    else:
        print("Данная последовательность символов не соответствует ни одному из двух форматов.")
else:
    print("Данная последовательность символов не соответствует ни одному из двух форматов.")