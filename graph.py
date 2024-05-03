import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample JSON data
data = [
    {"City": "New York", "Zip Code": "10001", "Frequency": 500},
    {"City": "Los Angeles", "Zip Code": "90001", "Frequency": 300},
    {"City": "Chicago", "Zip Code": "60601", "Frequency": 200},
    {"City": "Houston", "Zip Code": "77001", "Frequency": 400},
    {"City": "Phoenix", "Zip Code": "85001", "Frequency": 600},
    {"City": "Philadelphia", "Zip Code": "19101", "Frequency": 350},
    {"City": "San Antonio", "Zip Code": "78201", "Frequency": 250},
    {"City": "San Diego", "Zip Code": "92101", "Frequency": 450},
    {"City": "Dallas", "Zip Code": "75201", "Frequency": 550},
    {"City": "San Jose", "Zip Code": "95101", "Frequency": 700}
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set City as index
df.set_index('City', inplace=True)

# Create a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df[['Frequency']], cmap='coolwarm', annot=True, fmt="d")
plt.title('Population Density Heatmap')
plt.xlabel('Frequency')
plt.ylabel('City')
plt.show()
