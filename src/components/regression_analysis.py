import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from scipy import stats

def perform_regression(df, dependent_var, independent_vars):
    if dependent_var not in df.columns or any(var not in df.columns for var in independent_vars):
        st.error("Selected variables must be in the uploaded data.")
        return

    X = df[independent_vars]
    y = df[dependent_var]

    model = LinearRegression()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)
    coefficients = dict(zip(independent_vars, model.coef_))
    intercept = model.intercept_
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.subheader("Model Evaluation")
    st.write(f"Mean Squared Error (MSE): {mse:.2f}")
    st.write(f"R^2 Score: {r2:.3f}")
    st.subheader("Regression Results")
    st.write(f"Intercept: {intercept}")
    st.write("Coefficients:")
    for var, coef in coefficients.items():
        st.write(f"{var}: {coef}")

    # Plotting the results
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_test, y=y_pred)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel('Actual Value')
    plt.ylabel('Predicted Value')
    plt.title('Testing: Actual vs Predicted')
    st.pyplot(plt)

    # Residuals
    residuals = y_test - y_pred

    # Residuals plot
    plt.figure(figsize=(8, 6))
    sns.histplot(residuals, kde=True)
    plt.title('Histogram of Residuals')
    plt.xlabel('Residuals')
    st.pyplot(plt)