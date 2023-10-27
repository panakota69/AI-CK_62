'''Box plot — график, использующийся в описательной статистике, компактно
изображающий одномерное распределение вероятностей.
Такой вид диаграммы в удобной форме показывает медиану
(или, если нужно, среднее), нижний и верхний квартили, минимальное
и максимальное значение выборки и выбросы. Несколько таких ящиков
можно нарисовать бок о бок, чтобы визуально сравнивать одно
распределение с другим; их можно располагать как горизонтально,
так и вертикально. Расстояния между различными частями ящика позволяют
определить степень разброса (дисперсии) и асимметрии данных и выявить
выбросы.'''
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(10)

data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]

fig = plt.figure(figsize=(10, 7))

# Создание экземпляра осей
ax = fig.add_axes([0, 0, 1, 1])

# Palette — задают цвет.
sns.boxplot(data=data, palette='Set2')
plt.show()

# Загрузим датсет titanic
titanic = sns.load_dataset("titanic")
titanic.head()

plt.figure(figsize=(15, 6))

plt.subplot(121)
ax = sns.boxplot(x='pclass', y='fare', data=titanic, palette='Set3')
ax.legend().get_frame().set_facecolor("white")
plt.ylabel('Стоимость проезда')
