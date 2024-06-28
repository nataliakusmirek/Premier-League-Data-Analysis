# Premier League Data Analysis

This project involves analyzing Premier League match data to uncover various insights about team performances, goal statistics, and more.

## Dataset

The dataset used in this analysis is `premier-league-data.csv`. It contains information about Premier League matches, including the season, home and away teams, goals scored, and match results.

## Setup

1. Install necessary packages:
    ```sh
    pip install pandas
    ```
2. Load the dataset:
    ```python
    import pandas as pd
    df = pd.read_csv('premier-league-data.csv')
    df.head()
    df.info()
    ```

## Data Cleaning

### 1. Remove Invalid Values from the Season Column
Replace invalid season values:
```python
df['Season'] = df['Season'].str.replace('?', 'Unknown Season')
```

### 2. Identify and Replace Invalid Goals
Find invalid goal values:
```python
df.loc[(df['home_goals'] < 0) | (df['away_goals'] < 0)].sum()
```
Replace invalid goals with 0:
```python
df.loc[df['home_goals'] < 0, 'home_goals'] = 0
df.loc[df['away_goals'] < 0, 'away_goals'] = 0
```

### 3. Clean Invalid Results in the Result Column
Identify different values in the result column:
```python
df['result'].value_counts()
```
Correct invalid results:
```python
df.loc[df['home_goals'] > df['away_goals'], 'result'] = 'H'
df.loc[df['home_goals'] < df['away_goals'], 'result'] = 'A'
df.loc[df['home_goals'] == df['away_goals'], 'result'] = 'D'
```

## Analysis

### 1. Average Number of Goals per Match
Calculate the average goals per match:
```python
average_goals = (df['home_goals'] + df['away_goals']).mean()
```

### 2. Total Goals Column
Create a new column for total goals:
```python
df['total_goals'] = df['home_goals'] + df['away_goals']
```

### 3. Average Goals per Season
Calculate average goals per season:
```python
goals_per_season = df.groupby("Season")['total_goals'].mean().sort_index()
```

### 4. Biggest Goal Difference in a Match
Find the biggest goal difference:
```python
biggest_goal_difference = (df['home_goals'] - df['away_goals']).abs().max()
```

### 5. Team with the Most Away Wins
Identify the team with the most away wins:
```python
most_away_wins_team = df.loc[df['result'] == 'A'].groupby("away_team").size().idxmax()
most_away_wins_count = df.loc[df['result'] == 'A'].groupby("away_team").size().max()
```

### 6. Team with the Most Goals Scored at Home
Identify the team with the most home goals:
```python
most_home_goals_team = df.groupby("home_team")['home_goals'].sum().idxmax()
most_home_goals_count = df.groupby("home_team")['home_goals'].sum().max()
```

### 7. Team that Received the Least Goals at Home
Identify the team that received the least goals at home:
```python
least_goals_received_team = df.groupby("home_team")['away_goals'].sum().idxmin()
least_goals_received_count = df.groupby("home_team")['away_goals'].sum().min()
```

### 8. Team with the Most Goals Scored Away from Home
Identify the team with the most away goals:
```python
most_away_goals_team = df.groupby('away_team')['away_goals'].sum().idxmax()
most_away_goals_count = df.groupby('away_team')['away_goals'].sum().max()
```

## What I Learned

Through this project, I learned several key data science concepts and skills, including:

- **Data Cleaning**: Handling missing and invalid values, and ensuring the dataset is consistent and ready for analysis.
- **Data Exploration**: Understanding the structure and content of the dataset, and using summary statistics to gain initial insights.
- **Data Analysis**: Applying grouping, aggregation, and other analytical techniques to derive meaningful insights from the data.
- **Pandas Proficiency**: Utilizing the Pandas library for data manipulation, which is a crucial skill for any data scientist.
- **Problem-Solving**: Tackling real-world data issues and finding solutions to ensure accurate and reliable analysis.

## How This Will Help Me Practice Data Science Concepts for the Industry

This project provided practical experience in data science, helping me develop skills that are highly relevant to the industry:

1. **Real-World Data Handling**: By working with real-world data, I learned to navigate the complexities and imperfections that are common in industry datasets.
2. **Analytical Thinking**: Performing various analyses helped me hone my ability to think analytically and derive actionable insights from data.
3. **Technical Skills**: Gaining proficiency with tools and libraries like Pandas, which are essential for data manipulation and analysis in professional settings.
4. **Data-Driven Decision Making**: Understanding how to use data to make informed decisions, a crucial aspect of many roles in data science and analytics.
5. **Communication**: Documenting my process and findings in a clear and organized manner, which is important for collaborating with stakeholders and presenting results in the industry.

This hands-on project has equipped me with a solid foundation in data science, preparing me for more advanced projects and roles in the field.
