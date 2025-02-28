# Medical Cost Prediction
![](https://miro.medium.com/v2/resize:fit:1400/0*ssbGU5VIxtVB6NrF)
## Project Overview
This data science project aims to predict individual medical costs using a dataset containing various attributes related to health insurance. The project focuses on analyzing features such as age, gender, BMI, number of children, smoking status, region, and predicting the corresponding medical costs.

## Live Demo
Check out the live application here: [Medical Insurance Predictor App](https://medical-insurance-predictor-tool.streamlit.app)

## Data Dictionary
The dataset used in this project provides information about health insurance beneficiaries and their medical costs. It includes the following columns:

| Variable | Description |
| --- | --- |
| age | Age of primary beneficiary |
| sex | Gender of the beneficiary (male/female) |
|bmi | Body Mass Index |
|children | Number of children covered by health insurance |
|smoker | Whether the person smokes (yes/no) |
|region | The beneficiary's residential area in the US |
|charges(Target) | Individual medical costs billed by health insurance |

## Technologies Used
- Python (Programming language)
- Pandas & NumPy (Data Preprocessing & manipulation)
- Matplotlib & Seaborn (Data visualization)
- Scikit-learn (for machine learning)
- Joblib (Model saving/loading)
- Streamlit (For web-based model deployment)

## Folder Structure
```
Medical-Insurance-Predictor/
|-- .gitignore
│-- Medical_Cost_Prediction.ipynb    
|-- README.md           
│-- app.py        
│-- insurance.csv    
│-- medical_insurance_predictor.pkl  
│-- requirements.txt         
```

## Model Training Process
1. Data Preprocessing
  - Encoded Categorical Features
  - Performed feature scaling
2. Model Selection and Training
  - Trained multiple regression models
    - Linear Regression
    - K-Nearest Neighbors (KNN)
    - Decision Tree
    - Random Forest
  - Evaluated performance using MAE, MSE, RMSE and R² Score.
  - Selected the best-performing model on accuracy and generalization ability
3. Model Deployment
  - Tuned hyperparameters to enhance accuracy.
  - Saved the trained model using Joblib.
  - Built a Streamlit web application for real-time predictions

## Installation & Usage
### Prerequisites
Ensure you have Python installed along with the required dependencies.

### Install Dependencies
```
pip install -r requirements.txt
```

### Run the application
```
streamlit run app.py
```

 ## Example Prediction
Example user input:
```
Age: 19
Sex: Female
BMI: 27.90
Number of Children: 0
Smoker: Yes
Region: Southwest
```
Output:
```
Expected Insurance cost: $17608.67
```

## Important Disclaimer
This project is created for learning and demonstration purposes only. It is not meant for academic submissions or professional use. If using this for academic work, ensure adherence to your institution's integrity policies. This project serves as a portfolio demonstration of data science skills and should not be used for medical or financial decisions.

## Future Improvements
- Improve model accuracy with advanced feature engineering by including additional helath metrics
- Deploy the application online
- Enhance user experience with better UI in Streamlit
