# ============================================================
# EERS - PROGRAM 04
# AI Battery Condition Prediction
# ============================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

print("=" * 65)
print("       EERS - AI BATTERY CONDITION PREDICTION")
print("=" * 65)

# ------------------------------------------------------------
# TRAINING DATA
# ------------------------------------------------------------
# Features:
# SOC       = Battery State of Charge (%)
# Voltage   = Battery voltage (V)
# Power     = Motor power (W)
# Temp      = Battery temperature (°C)
#
# Label:
# 0 = NORMAL
# 1 = LOW
# 2 = CRITICAL
# 3 = EMERGENCY
# ------------------------------------------------------------

data = {

    "SOC": [
        90, 85, 80, 75, 70,
        60, 55, 50, 45, 40,
        35, 30, 28, 25, 22,
        18, 15, 12, 10, 8
    ],

    "Voltage": [
        12.6, 12.5, 12.4, 12.3, 12.2,
        12.0, 11.9, 11.8, 11.7, 11.6,
        11.5, 11.4, 11.3, 11.2, 11.1,
        10.9, 10.8, 10.7, 10.6, 10.5
    ],

    "Power": [
        30, 35, 40, 45, 50,
        50, 55, 60, 60, 65,
        65, 70, 70, 75, 75,
        80, 80, 85, 90, 90
    ],

    "Temperature": [
        25, 26, 27, 28, 29,
        30, 30, 31, 31, 32,
        32, 33, 34, 34, 35,
        36, 37, 38, 39, 40
    ],

    "Status": [
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        2, 2, 2, 2, 2,
        3, 3, 3, 3, 3
    ]
}

# ------------------------------------------------------------
# CREATE DATAFRAME
# ------------------------------------------------------------

df = pd.DataFrame(data)

print("\nTRAINING DATA")
print("-" * 65)

print(df)

# ------------------------------------------------------------
# INPUT AND OUTPUT
# ------------------------------------------------------------

X = df[
    [
        "SOC",
        "Voltage",
        "Power",
        "Temperature"
    ]
]

y = df["Status"]

# ------------------------------------------------------------
# SPLIT DATA
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

print("\nTraining samples :", len(X_train))
print("Testing samples  :", len(X_test))

# ------------------------------------------------------------
# CREATE AI MODEL
# ------------------------------------------------------------

model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

# ------------------------------------------------------------
# TRAIN MODEL
# ------------------------------------------------------------

print("\nTraining AI model...")

model.fit(X_train, y_train)

print("AI model training completed.")

# ------------------------------------------------------------
# TEST MODEL
# ------------------------------------------------------------

y_prediction = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_prediction
)

print("\nAI MODEL ACCURACY")
print("-" * 65)

print(f"Accuracy : {accuracy * 100:.2f}%")

# ------------------------------------------------------------
# TEST NEW EV CONDITION
# ------------------------------------------------------------

print("\nNEW EV CONDITION")
print("-" * 65)

new_vehicle = [[
    18,     # SOC %
    10.9,   # Voltage
    80,     # Motor Power
    36      # Temperature
]]

prediction = model.predict(new_vehicle)[0]

# ------------------------------------------------------------
# CONVERT PREDICTION TO STATUS
# ------------------------------------------------------------

status_names = {
    0: "NORMAL",
    1: "LOW",
    2: "CRITICAL",
    3: "EMERGENCY"
}

predicted_status = status_names[prediction]

print("Battery SOC     : 18 %")
print("Battery Voltage : 10.9 V")
print("Motor Power     : 80 W")
print("Temperature     : 36 °C")

print("\nAI PREDICTION")
print("-" * 65)

print("Predicted Status :", predicted_status)

# ------------------------------------------------------------
# EERS DECISION
# ------------------------------------------------------------

if predicted_status == "NORMAL":

    print("Decision : Continue normal operation.")

elif predicted_status == "LOW":

    print("Decision : Enter energy-saving mode.")

elif predicted_status == "CRITICAL":

    print("Decision : Prepare emergency battery.")

else:

    print("Decision : Activate emergency battery.")

print("=" * 65)
print("EERS PROGRAM 04 FINISHED")
print("=" * 65)