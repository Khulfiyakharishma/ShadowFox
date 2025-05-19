import pandas as pd

# Step 1: Define fielding weights
weights = {
    'CP': 1,
    'GT': 1,
    'C': 5,
    'DC': -3,
    'ST': 3,
    'RO': 4,
    'MRO': -2,
    'DH': 3,
    'RS': 1
}

# Step 2: Create fielding data
data = {
    'Player Name': ['Vaibhav Suryavanshi', 'Noor Ahmed', 'Abhishek Sharma'],
    'CP': [3, 4, 2],
    'GT': [2, 1, 3],
    'C': [1, 0, 2],
    'DC': [0, 1, 0],
    'ST': [0, 0, 1],
    'RO': [1, 0, 1],
    'MRO': [1, 2, 0],
    'DH': [0, 1, 2],
    'RS': [3, 1, 4]
}

# Step 3: Create DataFrame
df = pd.DataFrame(data)

# Step 4: Calculate performance score (PS) with step-by-step print
print("----- Step-by-Step Performance Score Calculation -----\n")
scores = []
for i, row in df.iterrows():
    player = row['Player Name']
    print(f"▶ {player}")
    total = 0
    for action, weight in weights.items():
        value = row[action]
        contrib = value * weight
        print(f"{action}: {value} × {weight} = {contrib}")
        total += contrib
    print(f"✅ Total Performance Score: {total}\n")
    scores.append(total)

# Step 5: Add PS to DataFrame
df['Performance Score'] = scores
df.to_csv('fielding_performance.csv', index=False)

# Step 6: Display final table
print("===== Final Fielding Performance Table =====\n")
print(df[['Player Name', 'CP', 'GT', 'C', 'DC', 'ST', 'RO', 'MRO', 'DH', 'RS', 'Performance Score']])
