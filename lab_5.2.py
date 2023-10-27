import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
print(df.head(10))
# Plot
plt.figure(figsize=(12, 10), dpi=80)
sns.heatmap(df.corr(), xticklabels=df.corr().columns,  # Функции оси.
            yticklabels=df.corr().columns, cmap='RdYlGn',
            center=0, annot=True)

# Стиль
plt.title('Correlogram of mtcars', fontsize=22)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
