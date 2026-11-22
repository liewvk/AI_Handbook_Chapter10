actual = [10.0, 12.0, 15.0]
predicted = [11.0, 11.0, 14.0]

squared_errors = []
for truth, estimate in zip(actual, predicted):
    error = estimate - truth
    squared_errors.append(error ** 2)

mse = sum(squared_errors) / len(squared_errors)
print("Squared errors:", squared_errors)
print(f"Mean squared error: {mse:.2f}")

