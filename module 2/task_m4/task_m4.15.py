#Лінією найкращої відповідності називається пряма, що проходить на найменшій відстані від набору з n точок. У цій вправі
# ми припустимо, що кожна точка в колекції має координати x і y. Символи  𝑥¯  і  𝑦¯  ми використовуватимемо для
# підрахунку середніх значень по осях x і y відповідно. Лінія найкращої відповідності представлена формулою  𝑦=𝑚𝑥+𝑏,
# де  𝑚  і  𝑏  обчислюються за такими формулами:  𝑚=∑𝑥𝑦−(∑𝑥)(∑𝑦)𝑛∑𝑥2−(∑𝑥)2𝑛
#𝑏=𝑦¯−𝑚⋅𝑥¯
#Напишемо програму, яка запитуватиме в користувача координати колекції точок. При цьому користувач має вводити спочатку
# координату x, а потім y. Введення координат може тривати до тих пір доти, доки користувач не залишить порожнім
# введення координати x. Відобразіть формулу, що характеризує лінію найкращої відповідності, виду  𝑦=𝑚𝑥+𝑏  шляхом
# заміни змінних m і b на значення, обчислені за попередніми формулами. Наприклад, якщо користувач введе
# три точки (1, 1), (2, 2.1) і (3, 2.9), підсумкова формула має набути вигляду:  𝑦=0,95𝑥+0,1 .
def best_fit_line(data):
    list_x  = list()
    list_y  = list()

    for coord in data:
        list_x.append(coord[0])
        list_y.append(coord[1])

    m1 = 0.0

    for i in range(len(data)):
        m1 += list_x[i] * list_y[i]

    m2 = (sum(list_x) * sum(list_y)) / len(data)

    m3 = 0.0

    for i in range(len(data)):
        m3 += pow(list_x[i], 2)

    m4 = pow(sum(list_x), 2) / len(data)

    m = round((m1 - m2) / (m3 - m4), 2)

    b = round((sum(list_y)/ len(list_y)) - m * (sum(list_x)/ len(list_x)), 2)

    return m, b

data = list()
x = input("Enter x coord: ")
while x != '':
    y = input("Enter Y coord: ")
    data.extend([[float(x), float(y)]])
    x = input("Enter x coord: ")

m, b = best_fit_line(data)
print(f"y = {m}x + {b} ")