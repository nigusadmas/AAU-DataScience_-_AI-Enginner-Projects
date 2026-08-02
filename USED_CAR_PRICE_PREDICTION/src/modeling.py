"""
modeling.py
Contains all regression models used in the project.
"""

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    ExtraTreesRegressor,
    AdaBoostRegressor
)
from sklearn.svm import SVR

RANDOM_STATE = 42


def get_models():
    """Return a dictionary of regression models."""

    models = {
        "Linear Regression": LinearRegression(),

        "Ridge Regression": Ridge(random_state=RANDOM_STATE),

        "Lasso Regression": Lasso(random_state=RANDOM_STATE),

        "Decision Tree": DecisionTreeRegressor(
            random_state=RANDOM_STATE
        ),

        "Random Forest": RandomForestRegressor(
            random_state=RANDOM_STATE
        ),

        "Gradient Boosting": GradientBoostingRegressor(
            random_state=RANDOM_STATE
        ),

        "Support Vector Regressor": SVR(),

        # Bonus Models
        "Extra Trees": ExtraTreesRegressor(
            random_state=RANDOM_STATE
        ),

        "AdaBoost": AdaBoostRegressor(
            random_state=RANDOM_STATE
        )
    }

    return models