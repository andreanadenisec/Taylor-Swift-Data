import pandas as pd
csv_path = 'spotify_taylor-swift.csv'
df = pd.read_csv(csv_path)

print(df['name'].to_string())