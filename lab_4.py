import pandas as pd

data = pd.read_csv('listings.csv')
# Столбцы не фигурирующие в Список колонок набора данных
data = data.drop(
    ["neighbourhood_group", "number_of_reviews_ltm", "license"],
    axis=1,
)

data.head()
data.tail()
print(data.dtypes)
# Количество незаполненных значений в каждом столбце
print(data.isnull().sum())
print()
print(f"Количество строк в изначальном сете {len(data)}")
# Удаление строк с пустой ячейкой
data = data.dropna()
print(f"Количество строк в очищенном сете   {len(data)}")
# Средняя и медианая цена
print(data['price'].mean())
print(data['price'].median())
print()

# Группировка по типу комнаты
grouped_data = data.groupby('room_type')
print(grouped_data['price'].mean())
print()
print(grouped_data['price'].median())
print()

# Группировка по типу комнаты и доступности в году
grouped_data = data.groupby(['room_type', 'availability_365'])
print(grouped_data['price'].mean())
print()
print(grouped_data['price'].median())
print()
# Отбор данных по условию
filtered_data = data[(data['room_type'] == 'Private room')
                     & (data['price'] == 300)]
filtered_data
