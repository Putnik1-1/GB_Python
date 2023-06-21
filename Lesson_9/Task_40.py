
# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
Решение:
​
df[df['population']<501]['median_house_value'].agg(['среднее значение'])
# означает 206799.951402
# Имя: median_house_value, dtype: float64
​
Вариант 2:
​
df[df['population']<501]['median_house_value'].mean()
206799.95140186916
