# Streamlit Data Analysis Application

This project is a Streamlit application designed for analyzing Excel data. It provides functionalities for uploading data, performing Principal Component Analysis (PCA), and conducting linear regression analysis.

## Project Structure

```
streamlit-data-analysis-app
├── src
│   ├── app.py                     # Main entry point of the Streamlit application
│   ├── components
│   │   ├── file_upload.py         # Handles file uploads and data processing
│   │   ├── pca_analysis.py        # Implements PCA analysis and visualization
│   │   └── regression_analysis.py  # Performs linear regression analysis
│   └── utils
│       └── data_processing.py     # Utility functions for data processing tasks
├── requirements.txt               # Lists project dependencies
└── README.md                      # Documentation for the project
```

## Features

- **File Upload**: Users can upload Excel files containing their data.
- **PCA Analysis**: Perform PCA on the uploaded data and visualize the results.
- **Linear Regression**: Fit a linear regression model to the data and display coefficients and intercept.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-data-analysis-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run src/app.py
   ```

## Usage Guidelines

- Upload an Excel file using the provided interface.
- Select the dependent and independent variables for regression analysis.
- View the results of PCA and regression analysis directly in the application.

## Acknowledgments

This project utilizes several libraries, including Streamlit, pandas, and scikit-learn, to provide a seamless data analysis experience.