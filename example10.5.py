temperatures = [22.0, 24.5, 25.0, 23.5]
model = {"name": "Demo Predictor", "version": 1}

average = sum(temperatures) / len(temperatures)
print("Model:", model["name"])
print("Measurements:", len(temperatures))
print(f"Average: {average:.2f}")
print("First value:", temperatures[0])

