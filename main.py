def ancient_cipher(l):
    password = ""

    # Перебираем все возможные пары чисел от 1 до l-1
    for i in range(1, l):
        for j in range(i + 1, l):  # Пары только с j > i
            if l % (i + j) == 0:  # Если l делится на сумму пары
                password += str(i) + str(j)

    return password


# Ввод данных
l = int(input("Введите число от 3 до 20: "))
if 3 <= l <= 20:
    result = ancient_cipher(l)
    print(f"Пароль для числа {l}: {result}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")


# Тестирование
test_values = {
    3: "12",
    4: "13",
    5: "1423",
    6: "121524",
    7: "162534",
    8: "13172635",
    9: "1218273645",
    10: "141923283746",
    11: "11029384756",
    12: "12131511124210394857",
    13: "112211310495867",
    14: "1611325212343114105968",
    15: "1214114232133124115106978",
    16: "1317115262143531341251161079",
    17: "11621531441351261171089",
    18: "12151811724272163631545414513612711810",
    19: "118217316415514613712811910",
    20: "13141911923282183731746416515614713812911"
}

for l, expected in test_values.items():
    result = ancient_cipher(l)
    print(f"l = {l}: {result} {'✔️' if result == expected else '❌'}")
    print(ancient_cipher(l))