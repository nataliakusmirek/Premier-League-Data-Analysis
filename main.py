import pandas as pd
df = pd.read_csv('premier-league-data.csv')
df.head()
df.info()

## Data Cleaning!

## Remove invalid values from the season column.
df['Season'] = df['Season'].str.replace('?', 'Unknown Season')

## Identify invalid values in goals scored
df.loc[(df['home_goals'] < 0) | (df['away_goals'] < 0)].sum()

## Replace invalid goals for 0
df.loc[df['home_goals'] < 0, 'home_goals'] = 0
df.loc[df['away_goals'] < 0, 'away_goals'] = 0

## Identify and clean invalid results in the result column
df['result'].value_counts() # See all the different values in the result column
df.loc[(df['home_goals'] > (df['away_goals'], 'result'] = 'H'
df.loc[(df['home_goals'] < (df['away_goals'], 'result'] = 'A'
df.loc[(df['home_goals'] = (df['away_goals'], 'result'] = 'D'



## Analysis!

## What is the average number of goals per match?
(df['home_goals'] + df['away_goals']).mean()

## Create a new column 'total_goals'
df['total_goals'] = (df['home_goals'] + df['away_goals'])

## Calculate average goals per season.
goals_per_season = df.groupby("season")['total_goals'].mean().sort_index()

## What is the biggest goal difference in a match?
(df['home_goals'] - df['away_goals']).abs().max()

## What is the team with the most away wins?
df.loc[df['result'] == 'A'].groupby("away_team")['away_goals'].sum().sort_values(ascending=False)

## What is the team with the most goals scored at home?
df.groupby("home_team")['home_goals'].sum().sort_values(ascending=False)

## What is the team that received the least amount of goals while playing at home?
df.groupby("home_team")[['home_team', 'away_goals']].agg({
    "home_team" : "size",
    "away_goals" : "sum"
    }).rename(
        columns={"home_team" : "total_games", "away_goals" : "goals_received"}
).sort_values(by=["total_games", "goals_received"], ascending=[False, True])

## What is the team with most goals scored playing as a visitor (away from home)?
df.groupby('away_team')['away_goals'].sum().sort_values(ascending=False)
