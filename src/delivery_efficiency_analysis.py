import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv('data/raw/Cold_Chain_Logistics_Dataset.csv')

# Create visualization folder
os.makedirs('visualizations', exist_ok=True)

# Calculate averages
summary = df.groupby('Delivery_Status').agg({
    'Estimated_Freshness_Percent': 'mean',
    'Energy_Consumption_kWh': 'mean'
})

# Freshness comparison
summary['Estimated_Freshness_Percent'].plot(
    kind='bar', title='Average Freshness by Delivery Status'
)
plt.ylabel('Freshness (%)')
plt.tight_layout()
plt.savefig('visualizations/delivery_freshness_comparison.png')
plt.close()

# Energy comparison
summary['Energy_Consumption_kWh'].plot(
    kind='bar', title='Average Energy Consumption by Delivery Status'
)
plt.ylabel('Energy (kWh)')
plt.tight_layout()
plt.savefig('visualizations/delivery_energy_comparison.png')
plt.close()

print("Visualizations created successfully!")
print(summary.round(2))