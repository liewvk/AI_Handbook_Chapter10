def categorize_score(score):
    if score >= 80:
        return "High"
    if score >= 60:
        return "Medium"
    return "Low"

scores = [45, 61, 79, 93]
for score in scores:
    print(f"Score {score}: {categorize_score(score)}")

