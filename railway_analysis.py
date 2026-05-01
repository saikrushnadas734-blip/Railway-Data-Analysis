import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("railway_data.csv")

# Show dataset
print("\n--- Railway Data ---")
print(data)

# 1. Average Delay
avg_delay = data["Delay_min"].mean()
print("\nAverage Delay:", avg_delay, "minutes")

# 2. Most Delayed Train
max_delay = data.loc[data["Delay_min"].idxmax()]
print("\nMost Delayed Train:")
print(max_delay)

# 3. Total Passengers
total_passengers = data["Passengers"].sum()
print("\nTotal Passengers:", total_passengers)

# 4. Fuel Consumption Analysis
avg_fuel = data["Fuel_Consumption"].mean()
print("\nAverage Fuel Consumption:", avg_fuel)

# 5. Plot: Delay of each train
plt.figure()
plt.bar(data["Train_Name"], data["Delay_min"])
plt.xlabel("Train Name")
plt.ylabel("Delay (minutes)")
plt.title("Train Delay Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Plot: Passengers per train
plt.figure()
plt.plot(data["Train_Name"], data["Passengers"], marker='o')
plt.xlabel("Train Name")
plt.ylabel("Passengers")
plt.title("Passenger Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()