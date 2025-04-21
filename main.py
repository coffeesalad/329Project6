import random
import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Simulate energy usage data (in kWh) for each smart device over a day
def simulate_energy_usage(hours=24):
    energy_data = []
    for hour in range(hours):
        energy_data.append({
            'lights': round(random.uniform(0.1, 0.5), 2),  # Lights use less power
            'fridge': round(random.uniform(0.8, 1.2), 2),  # Fridge uses moderate power
            'AC': round(random.uniform(1.5, 3.0), 2) if 10 <= hour <= 20 else 0.0,  # AC only during day
        })
    return energy_data

# Step 2: Aggregate energy usage by device
def aggregate_energy(energy_data):
    total_energy = Counter()
    for hour_data in energy_data:
        total_energy.update(hour_data)
    return total_energy

# Step 3: Visualize the energy usage in a pie chart
def plot_energy_pie(total_energy):
    labels = list(total_energy.keys())
    sizes = list(total_energy.values())

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Smart Home Energy Usage by Device (kWh)")
    plt.axis('equal')  # Equal aspect ratio ensures pie is a circle
    plt.show()

# Run the logger
energy_data = simulate_energy_usage()
total_energy = aggregate_energy(energy_data)
plot_energy_pie(total_energy)
