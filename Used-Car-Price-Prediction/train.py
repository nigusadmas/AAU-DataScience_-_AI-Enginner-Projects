# ==========================================================
# Used Car Price Prediction - Training Pipeline
# ==========================================================

import warnings
warnings.filterwarnings("ignore")

import os
import time
import joblib
import numpy as np
import pandas as pd

from pathlib import Path

# ==========================================================
# Machine Learning
# ==========================================================

from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    RandomizedSearchCV,
)

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler,
)

from sklearn.impute import SimpleImputer

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

# ==========================================================
# Regression Models
# ==========================================================

from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso,
)

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    ExtraTreesRegressor,
    AdaBoostRegressor,
)

from sklearn.svm import SVR

# ==========================================================
# Project Directories
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "used_cars.csv"

MODEL_DIR = BASE_DIR / "models"
TRAINED_MODEL_DIR = MODEL_DIR / "trained_models"
PREPROCESS_DIR = MODEL_DIR / "preprocessing"
METADATA_DIR = MODEL_DIR / "metadata"

TRAINED_MODEL_DIR.mkdir(parents=True, exist_ok=True)
PREPROCESS_DIR.mkdir(parents=True, exist_ok=True)
METADATA_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Load Dataset
# ==========================================================

print("=" * 60)
print("Loading dataset...")
print("=" * 60)

df = pd.read_csv(DATA_PATH)

print(f"Shape : {df.shape}")
print(df.head())

# ==========================================================
# Remove Duplicates
# ==========================================================

df.drop_duplicates(inplace=True)

# ==========================================================
# Handle Missing Values
# ==========================================================

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# ==========================================================
# Feature Engineering
# ==========================================================

CURRENT_YEAR = 2026

# Vehicle Age
df["vehicle_age"] = CURRENT_YEAR - df["model_year"]

# Alias used by previous pipeline
df["car_age"] = df["vehicle_age"]

# Mileage per year
df["milage_per_year"] = (
    df["milage"] /
    np.where(df["vehicle_age"] == 0, 1, df["vehicle_age"])
)

# Luxury Brand
luxury_brands = [
    "BMW",
    "Mercedes-Benz",
    "Audi",
    "Jaguar",
    "Volvo",
    "Land Rover",
    "Lexus",
    "Porsche",
]

df["luxury_brand"] = (
    df["brand"]
    .isin(luxury_brands)
    .astype(int)
)

# ==========================================================
# Features / Target
# ==========================================================

TARGET = "price"

X = df.drop(columns=[TARGET])

y = df[TARGET]

print("\nFeatures")
print(X.columns.tolist())

# ==========================================================
# Save Feature Names
# ==========================================================

joblib.dump(
    X.columns.tolist(),
    METADATA_DIR / "feature_columns.pkl"
)

# ==========================================================
# Numerical / Categorical Columns
# ==========================================================

numeric_features = X.select_dtypes(
    include=np.number
).columns.tolist()

categorical_features = X.select_dtypes(
    exclude=np.number
).columns.tolist()

print("\nNumerical Features")
print(numeric_features)

print("\nCategorical Features")
print(categorical_features)

# ==========================================================
# Preprocessing Pipeline
# ==========================================================

numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
        ),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            numeric_transformer,
            numeric_features,
        ),
        (
            "cat",
            categorical_transformer,
            categorical_features,
        ),
    ]
)

# ==========================================================
# Train / Test Split
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
)

print("\nTraining Samples :", X_train.shape[0])
print("Testing Samples  :", X_test.shape[0])

# ==========================================================
# Regression Models
# ==========================================================

models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(random_state=42),
    "Lasso Regression": Lasso(random_state=42),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42),
    "Support Vector Regression": SVR(),
    "Extra Trees": ExtraTreesRegressor(random_state=42),
    "AdaBoost": AdaBoostRegressor(random_state=42),
}

results = []

best_score = -999999
best_model_name = None
best_pipeline = None

print("\n" + "=" * 70)
print("Training Regression Models...")
print("=" * 70)

for name, model in models.items():

    print(f"\n{name}")

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    start_time = time.time()

    pipeline.fit(X_train, y_train)

    training_time = time.time() - start_time

    predictions = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, predictions)

    cv_scores = cross_val_score(
        pipeline,
        X_train,
        y_train,
        cv=5,
        scoring="r2",
        n_jobs=-1
    )

    cv_mean = cv_scores.mean()

    print(f"R² Score : {r2:.4f}")
    print(f"CV Score : {cv_mean:.4f}")

    results.append({
        "Algorithm": name,
        "Training Time": round(training_time, 3),
        "MAE": round(mae, 2),
        "MSE": round(mse, 2),
        "RMSE": round(rmse, 2),
        "R2 Score": round(r2, 4),
        "CV Score": round(cv_mean, 4),
    })

    if r2 > best_score:
        best_score = r2
        best_model_name = name
        best_pipeline = pipeline

# ==========================================================
# Model Comparison
# ==========================================================

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="R2 Score",
    ascending=False
)

print("\n")
print("=" * 70)
print("Regression Model Comparison")
print("=" * 70)

print(results_df)

# Save comparison table
results_df.to_csv(
    BASE_DIR / "outputs" / "model_comparison.csv",
    index=False
)

print("\nBest Model :", best_model_name)
print("Best R² Score :", round(best_score, 4))

# ==========================================================
# Hyperparameter Tuning (Random Forest)
# ==========================================================

print("\n" + "=" * 70)
print("Hyperparameter Tuning")
print("=" * 70)

param_grid = {
    "model__n_estimators": [100, 200, 300],
    "model__max_depth": [None, 10, 20, 30],
    "model__min_samples_split": [2, 5, 10],
    "model__min_samples_leaf": [1, 2, 4],
    "model__max_features": ["sqrt", "log2"],
}

rf_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(random_state=42))
    ]
)

random_search = RandomizedSearchCV(
    estimator=rf_pipeline,
    param_distributions=param_grid,
    n_iter=20,
    cv=5,
    scoring="r2",
    random_state=42,
    n_jobs=-1,
    verbose=1
)

random_search.fit(X_train, y_train)

best_pipeline = random_search.best_estimator_

print("\nBest Parameters")
print(random_search.best_params_)

print("\nBest CV Score")
print(random_search.best_score_)

# ==========================================================
# Final Evaluation
# ==========================================================

predictions = best_pipeline.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("\n")
print("=" * 70)
print("Final Model Performance")
print("=" * 70)

print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# ==========================================================
# Save Model
# ==========================================================

joblib.dump(
    best_pipeline,
    TRAINED_MODEL_DIR / "best_model.pkl"
)

joblib.dump(
    preprocessor,
    PREPROCESS_DIR / "preprocessor.pkl"
)

print("\nBest model saved successfully.")
# ==========================================================
# Residual Analysis
# ==========================================================

import matplotlib.pyplot as plt

os.makedirs(BASE_DIR / "outputs", exist_ok=True)

residuals = y_test - predictions

plt.figure(figsize=(8,6))

plt.scatter(predictions, residuals)

plt.axhline(0,color="red")

plt.xlabel("Predicted Price")

plt.ylabel("Residual")

plt.title("Residual Error Analysis")

plt.tight_layout()

plt.savefig(
    BASE_DIR / "outputs" / "residual_plot.png"
)

plt.close()

# ==========================================================
# Feature Importance
# ==========================================================

try:

    feature_names = best_pipeline.named_steps[
        "preprocessor"
    ].get_feature_names_out()

    importance = best_pipeline.named_steps[
        "model"
    ].feature_importances_

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importance
    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    importance_df.to_csv(
        BASE_DIR / "outputs" / "feature_importance.csv",
        index=False
    )

    plt.figure(figsize=(12,8))

    plt.barh(
        importance_df["Feature"][:20],
        importance_df["Importance"][:20]
    )

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.savefig(
        BASE_DIR / "outputs" / "feature_importance.png"
    )

    plt.close()

except Exception as e:

    print("Feature importance skipped:", e)

# ==========================================================
# SHAP Explainability
# ==========================================================

try:

    import shap

    X_train_transformed = best_pipeline.named_steps[
        "preprocessor"
    ].transform(X_train)

    explainer = shap.TreeExplainer(
        best_pipeline.named_steps["model"]
    )

    shap_values = explainer.shap_values(
        X_train_transformed[:200]
    )

    shap.summary_plot(
        shap_values,
        X_train_transformed[:200],
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        BASE_DIR / "outputs" / "shap_summary.png"
    )

    plt.close()

    print("SHAP plot saved.")

except Exception as e:

    print("SHAP skipped:", e)

# ==========================================================
# Completed
# ==========================================================

print("\n" + "=" * 70)
print("Training Completed Successfully")
print("=" * 70)

print("Saved Files")

print(TRAINED_MODEL_DIR / "best_model.pkl")

print(PREPROCESS_DIR / "preprocessor.pkl")

print(METADATA_DIR / "feature_columns.pkl")

print(BASE_DIR / "outputs")