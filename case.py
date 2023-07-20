#место для твоего кода
# Кейс №6 - Самые популярные фильмы
# - Чем выше рейтинг фильма, тем выше его доход
# - Чем дольше идёт фильм, тем выше его доход
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./IMDB-Movie-Data.csv')
df = df.dropna()
print(df.info())
# Rating
# Revenue (Millions)
#print(df['math score'].value_counts())
#print(df['reading score'].value_counts())
#print(df['writing score'].value_counts())
#df.plot(x='Rating',y='Revenue (Millions)', kind="scatter")
df.plot(x='Runtime (Minutes)',y='Revenue (Millions)', kind="scatter")
plt.show()