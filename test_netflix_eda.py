import pandas as pd
import numpy as np
import pytest

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "show_id": ["s1", "s2", "s3", "s4"],
        "title": ["Movie A", "Movie B", "Show C", "Show D"],
        "type": ["Movie", "Movie", "TV Show", "TV Show"],
        "duration": ["90 min", "120 min", "2 Seasons", "1 Season"],
        "release_year": [2020, 2021, 2019, 2018],
        "listed_in": ["Drama, Action", "Comedy", "Documentary", "Thriller"]
    })

def test_dataframe_not_empty(sample_df):
    assert not sample_df.empty

def test_unique_show_ids(sample_df):
    assert sample_df["show_id"].is_unique

def test_type_values(sample_df):
    assert set(sample_df["type"].unique()) == {"Movie", "TV Show"}

def test_movie_duration_numeric(sample_df):
    df_movies = sample_df[sample_df["type"] == "Movie"].copy()
    df_movies["duration_minutes"] = pd.to_numeric(
        df_movies["duration"].str.replace(" min", ""), errors="coerce"
    )
    assert df_movies["duration_minutes"].notnull().all()

def test_tvshow_seasons_numeric(sample_df):
    df_shows = sample_df[sample_df["type"] == "TV Show"].copy()
    df_shows["seasons"] = pd.to_numeric(
        df_shows["duration"].str.replace(" Seasons", "").str.replace(" Season", ""),
        errors="coerce"
    )
    assert df_shows["seasons"].notnull().all()

def test_release_year_range(sample_df):
    assert sample_df["release_year"].between(1900, 2026).all()

def test_genre_extraction(sample_df):
    sample_df["genre"] = sample_df["listed_in"].str.split(",").str[0].str.strip()
    assert sample_df["genre"].notnull().all()
