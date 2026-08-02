    # 🚗 Used Car Price Prediction System
    
    A complete end-to-end Machine Learning Regression project developed for the **Intelligent AI and Data Engineering** course at **Addis Ababa University (AAU)**.
    
    The application predicts the **selling price of used cars** using multiple regression algorithms and provides an interactive web interface built with **Streamlit**.
    
    ---
    
    # 📌 Project Overview
    
    Buying or selling a used car can be challenging because determining a fair market price depends on many factors such as the vehicle's brand, manufacturing year, mileage, fuel type, transmission, engine, accident history, and more.
    
    This project applies the complete Machine Learning workflow to build an accurate regression model capable of predicting the selling price of used cars.
    
    ---
    
    # 🎯 Project Objectives
    
    - Understand the business problem
    - Explore and analyze the dataset
    - Clean and preprocess the data
    - Train multiple regression algorithms
    - Compare model performance
    - Perform hyperparameter tuning
    - Select the best model
    - Build a prediction web application
    - Deploy the application
    
    ---
    
    # 📂 Project Structure
    
    ```text
    USED_CAR_PRICE_PREDICTION/
    │
    ├── app/
    │   ├── app.py
    │   ├── components/
    │   ├── pages/
    │   ├── assets/
    │   ├── config.py
    │   └── utils.py
    │
    ├── data/
    │   ├── raw/
    │   └── processed/
    │
    ├── models/
    │   ├── best_model.pkl
    │   └── preprocessing/
    │
    ├── notebooks/
    │
    ├── outputs/
    │   ├── figures/
    │   ├── tables/
    │   └── reports/
    │
    ├── presentation/
    ├── report/
    ├── src/
    │
    ├── requirements.txt
    ├── README.md
    └── .gitignore
    ```
    
    ---
    
    # 📊 Dataset
    
    **Project:** Used Car Price Prediction
    
    **Target Variable:**
    
    - Selling Price
    
    Example features include:
    
    - Brand
    - Model
    - Model Year
    - Mileage
    - Fuel Type
    - Engine
    - Transmission
    - Exterior Color
    - Interior Color
    - Accident History
    - Clean Title
    
    ---
    
    # 🧹 Data Preprocessing
    
    The following preprocessing steps were performed:
    
    - Missing value handling
    - Duplicate removal
    - Outlier analysis
    - Data type correction
    - Categorical encoding
    - Feature scaling (where required)
    - Feature engineering
    - Train/Test split
    
    ---
    
    # 📈 Exploratory Data Analysis
    
    The project includes:
    
    - Histograms
    - Boxplots
    - Scatter plots
    - Correlation heatmap
    - Distribution plots
    - Brand analysis
    - Price distribution
    - Fuel type analysis
    - Transmission analysis
    
    ---
    
    # 🤖 Machine Learning Models
    
    The following regression algorithms were trained and compared:
    
    - Linear Regression
    - Ridge Regression
    - Lasso Regression
    - Decision Tree Regressor
    - Random Forest Regressor
    - Gradient Boosting Regressor
    - Support Vector Regressor (SVR)
    - Extra Trees Regressor (Bonus)
    - AdaBoost Regressor (Bonus)
    
    ---
    
    # ⚙ Hyperparameter Tuning
    
    The project includes:
    
    - GridSearchCV
    - RandomizedSearchCV
    - 5-Fold Cross Validation
    
    ---
    
    # 📉 Model Evaluation
    
    Models were evaluated using:
    
    - Mean Absolute Error (MAE)
    - Mean Squared Error (MSE)
    - Root Mean Squared Error (RMSE)
    - R² Score
    
    Additional analysis:
    
    - Learning Curves
    - Residual Error Analysis
    - Feature Importance
    - SHAP Explainability
    
    ---
    
    # 🏆 Best Model
    
    The best-performing regression model was selected based on:
    
    - Highest R² Score
    - Lowest RMSE
    - Lowest MAE
    - Cross-validation performance
    
    The trained model is saved as:
    
    ```text
    models/best_model.pkl
    ```
    
    ---
    
    # 🌐 Web Application
    
    The application was built using **Streamlit** and includes the following pages:
    
    - 🏠 Home
    - 📊 Dataset Information
    - 📈 Exploratory Data Analysis
    - 🤖 Model Comparison
    - 🚗 Prediction
    - 📋 Project Information
    - 👥 About Team
    
    ---
    
    # 🛠 Technology Stack
    
    Programming Language
    
    - Python
    
    Machine Learning
    
    - Scikit-Learn
    - SHAP
    
    Data Analysis
    
    - Pandas
    - NumPy
    
    Visualization
    
    - Plotly
    - Matplotlib
    - Seaborn
    
    Web Framework
    
    - Streamlit
    
    Model Persistence
    
    - Joblib
    
    ---
    
    # 🚀 Installation
    
    ## Clone the Repository
    
    ```bash
    git clone https://github.com/your-username/used-car-price-prediction.git
    ```
    
    ---
    
    ## Navigate to the Project
    
    ```bash
    cd USED_CAR_PRICE_PREDICTION
    ```
    
    ---
    
    ## Create Virtual Environment
    
    Windows
    
    ```bash
    python -m venv venv
    ```
    
    Activate
    
    ```bash
    venv\Scripts\activate
    ```
    
    ---
    
    ## Install Dependencies
    
    ```bash
    pip install -r requirements.txt
    ```
    
    ---
    
    ## Run the Application
    
    ```bash
    streamlit run app/app.py
    ```
    
    ---
    
    # 📸 Screenshots
    
    Add screenshots of:
    
    - Home Page
    - Dataset Page
    - EDA Dashboard
    - Model Comparison
    - Prediction Page
    
    Example:
    
    ```text
    screenshots/
        home.png
        prediction.png
        eda.png
    ```
    
    ---
    
    # 📈 Future Improvements
    
    - Deep Learning models
    - Docker deployment
    - User authentication
    - Database integration
    - Cloud deployment
    - REST API
    - Mobile application
    - VIN decoder integration
    
    ---
    
    # 👥 Team
    
    **Course**
    
    Intelligent AI and Data Engineering
    
    **University**
    
    Addis Ababa University
    
    **Project**
    
    Used Car Price Prediction
    
    ---
    
    # 📜 License
    
    This project was developed for academic purposes as part of the Intelligent AI and Data Engineering course.
    
    ---
    
    # 🙏 Acknowledgements
    
    Special thanks to:
    
    - Addis Ababa University
    - Course Instructor
    - Scikit-Learn Community
    - Streamlit Community
    - Open Source Contributors
    
    ---
    
    # ⭐ If you like this project
    
    Please consider giving it a ⭐ on GitHub.