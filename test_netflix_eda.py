import pandas as pd
import numpy as np
import pytest
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans

@pytest.fixture(scope="module")
def df():
    return pd.read_csv("netflix_titles.csv")

# --- Data Import ---
def test_data_load(df):
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_missing_values_handled(df):
    df_clean = df.copy()
    df_clean['director'] = df_clean['director'].fillna('Unknown')
    df_clean['cast'] = df_clean['cast'].fillna('Unknown')
    df_clean['country'] = df_clean['country'].fillna('Unknown')
    df_clean['rating'] = df_clean['rating'].fillna('Not Rated')
    df_clean['duration'] = df_clean['duration'].fillna('Unknown')
    assert "Unknown" in df_clean['director'].values
    assert "Unknown" in df_clean['cast'].values
    assert "Not Rated" in df_clean['rating'].values

# --- TV Shows ---
def test_tvshow_average_seasons(df):
    df_shows = df[df['type'] == 'TV Show'].copy()
    df_shows['seasons'] = pd.to_numeric(
        df_shows['duration'].str.replace(' Season','').str.replace(' Seasons',''),
        errors='coerce'
    )
    assert df_shows['seasons'].mean() > 0

# --- Movies ---
def test_movie_average_length(df):
    df_movies = df[df['type'] == 'Movie'].copy()
    df_movies['duration_minutes'] = pd.to_numeric(
        df_movies['duration'].str.replace(' min',''),
        errors='coerce'
    )
    assert df_movies['duration_minutes'].mean() > 0

# --- Date Features ---
def test_year_month_extraction(df):
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month
    months = df['month_added'].dropna()
    assert months.between(1,12).all()

# --- Clustering ---
def test_cluster_labels(df):
    features = pd.DataFrame()
    features['release_year'] = df['release_year']
    features['duration_num'] = pd.to_numeric(
        df['duration'].str.replace(' min','').str.replace(' Season','').str.replace(' Seasons',''),
        errors='coerce'
    ).fillna(0)
    features['genre'] = df['listed_in'].str.split(',').str[0].str.strip()
    encoder = LabelEncoder()
    features['genre_encoded'] = encoder.fit_transform(features['genre'].fillna('Unknown'))
    scaler = StandardScaler()
    X = scaler.fit_transform(features[['release_year','duration_num','genre_encoded']])
    kmeans = KMeans(n_clusters=5, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)
    assert 'cluster' in df.columns
    assert df['cluster'].nunique() == 5

# --- Sanity Check ---
def test_type_column(df):
    assert set(df['type'].unique()) == {"Movie", "TV Show"}
