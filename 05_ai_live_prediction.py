# ============================================================
# EERS - PROGRAM 05
# AI LIVE BATTERY CONDITION PREDICTION
# ============================================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

print("=" * 65)
print("       EERS - AI LIVE BATTERY PREDICTION")
print("=" * 65)

# ------------------------------------------------------------
# TRAINING DATA
# ------------------------------------------------------------

data = {
    "SOC": [
        95, 90, 85, 80, 75,
        65, 60, 55, 50, 45,
        35, 30, 25, 22, 20,
        18, 15, 12, 10, 8
    ],

    "Voltage": [
        12.6, 12.5, 12.4, 12.3, 12.2,
        12.0, 11.9, 11.8, 11.7, 11.6,
        11.5, 11.4, 11.2, 11.1, 11.0,
        10.9, 10.8, 10.7, 10.6, 10.5
    ],

    "Power": [
        20, 25, 30, 35, 40,
        45, 50, 55, 60, 65,
        65, 70, 75, 75, 80,
        80, 85, 90, 90, 95
    ],

    "Temperature": [
        25, 25, 26, 27, 28,
        29, 30, 30, 31, 32,
        32, 33, 34, 35, 35,
        36, 37, 38, 39, 40
    ],

    "Status": [
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        2, 2, 2, 2, 2,
        3, 3, 3, 3, 3
    ]
}

df = pd.DataFrame(data)

# ------------------------------------------------------------
# TRAIN AI MODEL
# ------------------------------------------------------------

X = df[
    ["SOC", "Voltage", "Power", "Temperature"]
]

y = df["Status"]

model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

model.fit(X, y)

print("\nAI MODEL READY")
print("-" * 65)

# ------------------------------------------------------------
# TEST DIFFERENT VEHICLE CONDITIONS
# ------------------------------------------------------------

test_cases = [

    [85, 12.4, 30, 27],
    [55, 11.8, 50, 30],
    [32, 11.4, 70, 33],
    [18, 10.9, 80, 36],
    [10, 10.6, 90, 40]

]

status_names = {
    0: "NORMAL",
    1: "LOW",
    2: "CRITICAL",
    3: "EMERGENCY"
}

# ------------------------------------------------------------
# AI PREDICTION
# ------------------------------------------------------------

for number, vehicle in enumerate(test_cases, start=1):

    prediction = model.predict([vehicle])[0]

    status = status_names[prediction]

    print("\nVehicle Test", number)
    print("-" * 40)

    print(f"SOC         : {vehicle[0]} %")
    print(f"Voltage     : {vehicle[1]} V")
    print(f"Motor Power : {vehicle[2]} W")
    print(f"Temperature : {vehicle[3]} C")

    print(f"AI STATUS   : {status}")

    # --------------------------------------------------------
    # EERS ACTION
    # --------------------------------------------------------

    if status == "NORMAL":

        print("EERS ACTION : Normal operation")

    elif status == "LOW":

        print("EERS ACTION : Energy saving mode")

    elif status == "CRITICAL":

        print("EERS ACTION : Prepare emergency battery")

    else:

        print("EERS ACTION : Activate emergency backup")

# ------------------------------------------------------------
# END
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("EERS PROGRAM 05 FINISHED")
print("=" * 65)