study_hours = 6
practice_hours = 4
weight_study = 0.6
weight_practice = 0.4
bias = 2.0

score = (study_hours * weight_study
         + practice_hours * weight_practice + bias)

print(f"Predicted score: {score:.2f}")
print("Value type:", type(score).__name__)

