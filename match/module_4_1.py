from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Пример вызова функций с аргументами
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

# Выводим результаты
print(result1)  # Ожидаемый результат: 23.0
print(result2)  # Ожидаемый результат: 'Ошибка'
print(result3)  # Ожидаемый результат: 7.0
print(result4)  # Ожидаемый результат: inf