
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = r"C:\DataScience\Assignment2_Delhi_AQI\delhiaqi.csv"
df = pd.read_csv(file_path)
  

df = pd.read_csv(file_path)
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['season'] = df['month'].map({
    12: 'Winter', 1: 'Winter', 2: 'Winter',
    3: 'Spring', 4: 'Spring',
    5: 'Summer', 6: 'Summer',
    7: 'Monsoon', 8: 'Monsoon', 9: 'Monsoon',
    10: 'Post-Monsoon', 11: 'Post-Monsoon'
})

# 2. Time series plot
plt.figure(figsize=(14, 6))
plt.plot(df['date'], df['pm2_5'], label='PM2.5', color='red', alpha=0.6)
plt.plot(df['date'], df['pm10'], label='PM10', color='blue', alpha=0.6)
plt.xlabel('Date')
plt.ylabel('Concentration (µg/m³)')
plt.title('PM2.5 and PM10 Over Time in Delhi')
plt.legend()
plt.tight_layout()
plt.show()

# 3. Seasonal boxplot
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='season', y='pm2_5', palette='Set2')
plt.title('Seasonal Variation of PM2.5')
plt.ylabel('PM2.5 Concentration (µg/m³)')
plt.xlabel('Season')
plt.tight_layout()
plt.show()

# 4. Correlation matrix
pollutants = ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']
corr_matrix = df[pollutants].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Pollutants')
plt.tight_layout()
plt.show()

# 5. Monthly averages
monthly_avg = df.groupby('month')['pm2_5'].mean()

plt.figure(figsize=(10, 6))
monthly_avg.plot(kind='bar', color='darkgreen')
plt.xlabel('Month')
plt.ylabel('Average PM2.5 (µg/m³)')
plt.title('Monthly Average PM2.5 Levels in Delhi')
plt.xticks(ticks=range(0,12), labels=[
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])
plt.tight_layout()
plt.show()

# 6. Summary statistics
summary_stats = df[pollutants].describe()
print(summary_stats)
