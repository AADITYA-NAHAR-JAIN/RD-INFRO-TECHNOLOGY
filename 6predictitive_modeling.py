import pandas as pd

from sklearn.model_selection import (
    train_test_split
)

from sklearn.linear_model import (
    LinearRegression
)

from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)

df = pd.read_csv(
    "transformed_superstore.csv"
)

X = df[
    [
        "Sales",
        "Quantity",
        "Discount"
    ]
]

y = df["Profit"]

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

print(
    "MAE:",
    mean_absolute_error(
        y_test,
        predictions
    )
)

print(
    "R2 Score:",
    r2_score(
        y_test,
        predictions
    )
)

new_data = pd.DataFrame(
    [[1000, 5, 0.1]],
    columns=["Sales", "Quantity", "Discount"]
)

prediction = model.predict(
    new_data
)

print(
    "Predicted Profit:",
    prediction[0]
)