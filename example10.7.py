def predict(x1, x2, w1=0.5, w2=0.8, bias=0.2):
    return x1 * w1 + x2 * w2 + bias

first = predict(2, 3)
second = predict(4, 1)

print(f"Prediction 1: {first:.2f}")
print(f"Prediction 2: {second:.2f}")

