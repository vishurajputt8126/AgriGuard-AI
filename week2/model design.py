# AgriGuard AI - preliminary Week 2 model design
# This is a baseline implementation skeleton, not a claimed production result.

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

FEATURES = [
    "temperature_c",
    "humidity_percent",
    "rainfall_mm",
    "leaf_wetness_hours",
    "crop_age_days",
    "previous_disease_cases",
]

TARGET = "risk_class"

def build_baseline_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        class_weight="balanced"
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(classification_report(y_test, predictions))
    print(confusion_matrix(y_test, predictions))

    return model

# Usage after loading a real dataset:
# X = df[FEATURES]
# y = df[TARGET]
# model = build_baseline_model(X, y)
