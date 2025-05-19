import pandas as pd
import matplotlib.pyplot as plt

# Fielding data (same as before)
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

weights = {
    'CP': 1, 'GT': 1, 'C': 5, 'DC': -3, 'ST': 3,
    'RO': 4, 'MRO': -2, 'DH': 3, 'RS': 1
}

df = pd.DataFrame(data)
df['Performance Score'] = df[list(weights.keys())].mul(pd.Series(weights)).sum(axis=1)

# Plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(df['Player Name'], df['Performance Score'], color=['skyblue', 'salmon', 'limegreen'])
plt.title('Fielding Performance Score (PS)')
plt.xlabel('Player')
plt.ylabel('Performance Score')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
