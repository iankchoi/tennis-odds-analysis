# Tennis Odds Analysis

Do bookmaker odds accurately predict tennis match outcomes? An analysis of ~288K completed ATP and WTA matches, 2014-2025.

## Question
When bookmakers make a player the favorite, how often does that player actually win, and do the odds price that probability correctly?

## Data
Kaggle dataset: Tennis Results and Betting Odds (2014-2025).
The CSV is not included because of its size. Download it from Kaggle and place it in the project folder as `tennis_matches_2014_2025.csv`.

## How to run
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python explore.py

## Findings so far
- Favorites (lower best odds) won 71.2% of 281,807 completed matches with valid odds.

## Next steps
- Remove the bookmaker margin and compare implied probability to actual win rate
- Break results down by odds bucket, surface, and tour
- Backtest a simple betting strategy