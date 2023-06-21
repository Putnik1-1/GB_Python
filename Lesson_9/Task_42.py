# Задача 42: Узнать какая максимальная households в зоне минимального значения population
# Решение:
​
df[df['население']==df['population'].min()]['домохозяйства'].max()
# 4.0
​
# Вариант 2:

df[df['population']==df['population'].min()]['домохозяйства'].agg(['max'])
# максимум 4.0
# Имя: домохозяйства, dtype: float64