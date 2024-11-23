import pandas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import ast

# download dataset
url = "movies_metadata.csv"
movies_df = pd.read_csv(url)

# output info about dataset
movies_df.info()
# print(movies_df.head())

# print(movies_df.describe())

def extract_genres(gebre_str):
    try:
        genres = ast.literal_eval(gebre_str)
        return [genre['name'] for genre in genres]
    except ValueError:
        return []

# print(movies_df['genres'])
movies_df['genres'] = movies_df['genres'].apply(extract_genres)

# print(movies_df['genres'])

movies_df['budget'] = pd.to_numeric(movies_df['budget'], errors='coerce')
movies_df['revenue'] = pd.to_numeric(movies_df['revenue'], errors='coerce')

movies_df.dropna(subset=['budget', 'revenue'], inplace = True)
# print(movies_df['budget'])
# print(movies_df['revenue'])

#----------------------------------------------------------------

# print(movies_df['release_date'])
movies_df['release_year'] = pd.to_datetime(movies_df['release_date'], errors='coerce').dt.year
# print(movies_df['release_year'])

#----------------------------------------------------------------

genres_exploaded = movies_df[['title', 'release_year', 'budget', 'revenue', 'genres']].explode('genres')
print(genres_exploaded)

genre_count = genres_exploaded['genres'].value_counts()
print(genre_count)

# Візуалізація жанрів
plt.figure(figsize=(10,6))
sns.barplot(x=genre_count.index, y=genre_count.values)
plt.title("Кількість фільмів за жанрами")
plt.xlabel("Жанр")
plt.ylabel("Кілкість фільмів")
plt.xticks(rotation=45)
plt.tight_layout()
# plt.show()

#----------------------------------------------------------------
movies_df['popularity'] = pd.to_numeric(movies_df['popularity'], errors='coerce')
popularity_trend = movies_df.groupby('release_year')['popularity'].mean()
# Візуалізація трендів популярності
plt.figure(figsize=(12,6))
popularity_trend.plot()
plt.title("Середня популярність фільмів за роками")
plt.xlabel("Рік")
plt.ylabel("Популярність")
# plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
