# exploratory-data-analysis-on-netfilx-streaming-trends
# Netflix Content Analysis: An EDA-Based Approach Using Python, Pandas and Matplotlib

Exploratory data analysis on Netflix's content catalog to uncover patterns in what Netflix has added over time — genres, countries, ratings, and content types — using an EDA/CRISP-DM style workflow.

## Overview

This project explores a Netflix content catalog dataset (sourced from Kaggle) to understand trends in the platform's library — how the mix of Movies vs. TV Shows has changed, which countries produce the most titles, how content ratings are distributed, and how the catalog has grown year over year.

**Note:** This dataset describes the content catalog only (titles, genres, cast, country, release year, rating, etc.) — it does not include user-level viewership or engagement data. So metrics here reflect catalog composition and metadata trends, not actual audience viewing behavior.

## Dataset

- **Source:** Kaggle Netflix Titles dataset
- **Columns:** `show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`

## Objectives

- Clean and prepare the raw catalog data for analysis
- Analyze the split between Movies and TV Shows
- Identify top contributing countries and genres
- Examine trends in content additions over time
- Explore rating distributions across the catalog
- Visualize findings using Matplotlib

## Tech Stack

- **Python**
- **Pandas** — data cleaning and manipulation
- **Matplotlib** — data visualization
- **Jupyter Notebook**

## Approach

This project follows a CRISP-DM inspired workflow:

1. **Data Understanding** — initial exploration of the raw dataset
2. **Data Preparation** — handling missing values, fixing data types, standardizing text fields
3. **Exploratory Analysis** — univariate and bivariate analysis across content type, country, genre, rating, and release year
4. **Visualization** — charts summarizing key trends
5. **Insights** — key takeaways from the analysis

## Project Structure

```
├── data/               # Raw dataset (Netflix titles CSV)
├── notebooks/          # Jupyter notebooks with the EDA workflow
├── visuals/            # Exported charts and plots
└── README.md
```

## Key Insights

*(To be updated as the analysis progresses)*

## How to Run

1. Clone the repository
   ```
   git clone https://github.com/Nikithasri-712/exploratory-data-analysis-on-netfilx-streaming-trends.git
   ```
2. Install dependencies
   ```
   pip install pandas matplotlib jupyter
   ```
3. Open the notebook and run the cells
   ```
   jupyter notebook
   ```

## Author

**Nikitha Sri**
[GitHub](https://github.com/Nikithasri-712)
