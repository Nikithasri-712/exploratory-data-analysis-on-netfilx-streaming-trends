import pandas as pd
import numpy as np

# ✅ Load Netflix dataset
df = pd.read_csv(r"C:\Projects\exploratary_data_analysis_netfilx\netflix_titles.csv")

# ✅ Quick checks
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head(3))

# ✅ Basic cleaning
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('Unknown')

# ✅ Normalize ratings
valid_ratings = [
    'TV-MA','TV-14','TV-PG','R','PG-13','TV-Y7','TV-Y',
    'PG','TV-G','NR','G','TV-Y7-FV','Not Rated','NC-17','UR'
]
df = df[df['rating'].isin(valid_ratings)]
df['rating'] = df['rating'].replace({'Not Rated': 'NR', 'UR': 'NR'})

# ✅ Add decade column
df['decade'] = (df['release_year'] // 10) * 10

# ✅ Save cleaned dataset for Power BI
df.to_csv("netflix_clean.csv", index=False)

print("Cleaned dataset saved as netflix_clean.csv")