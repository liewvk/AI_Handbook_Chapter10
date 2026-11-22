confidence = 0.82

if confidence >= 0.90:
    print("High confidence: review the result")
elif confidence >= 0.60:
    print("Moderate confidence: check supporting data")
else:
    print("Low confidence: request human review")

