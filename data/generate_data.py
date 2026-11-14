import random
import pandas as pd

data = []

road_types = ["highway", "city", "residential"]
weather_conditions = ["clear", "rain", "fog"]

for _ in range(1000):  # number of rows
    hour = random.randint(0, 23)
    day = random.randint(0, 6)
    road_type = random.choice(road_types)
    weather = random.choice(weather_conditions)

    # Base vehicle count
    vehicle_count = random.randint(20, 80)

    # Peak hour logic
    if hour in [8, 9, 17, 18, 19]:
        vehicle_count += random.randint(40, 80)

    # Weekend logic
    if day in [5, 6]:
        vehicle_count -= random.randint(10, 30)

    # Weather logic
    if weather == "rain":
        vehicle_count += random.randint(20, 40)
    elif weather == "fog":
        vehicle_count += random.randint(10, 20)

    # Ensure vehicle count is not negative
    vehicle_count = max(10, vehicle_count)

    # Traffic level classification
    if vehicle_count < 50:
        traffic_level = "Low"
    elif vehicle_count <= 120:
        traffic_level = "Medium"
    else:
        traffic_level = "High"

    data.append([
        hour, day, vehicle_count, road_type, weather, traffic_level
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "hour", "day", "vehicle_count", "road_type", "weather", "traffic_level"
])

# Save to CSV
df.to_csv("traffic_data.csv", index=False)

print("traffic_data.csv created successfully!")
