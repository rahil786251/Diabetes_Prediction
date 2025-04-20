# Diabetes_Prediction
🩺 How My Diabetes Prediction Project Works
1️⃣ Problem Statement
Predict whether a person is likely to have diabetes based on simple health metrics like:

Age

BMI (Body Mass Index)

Skin Thickness

2️⃣ Input Features
The user will input:

Age (years)

BMI (kg/m²) — body fat measure based on height and weight

Skin Thickness (mm) — a health indicator related to fat percentage

3️⃣ Machine Learning Model
I trained a classification model (like Logistic Regression, Decision Tree, or Random Forest) using a diabetes dataset.

The model learns the relationship between Age, BMI, Skin Thickness, and the likelihood of having diabetes.

4️⃣ Training Process
Data Collection:
Took a diabetes dataset (eg., PIMA Indians Diabetes Database).

Data Cleaning:

Removed or imputed missing values.

Normalized features if needed.

Feature Selection:
Only selected Age, BMI, Skin Thickness to keep it simple.

Model Training:
Trained using a supervised learning algorithm (Logistic Regression is simple and interpretable).

Evaluation:
Used accuracy, confusion matrix, and ROC curve to check model performance.

5️⃣ Prediction Process (Working Flow)
User Inputs their Age, BMI, and Skin Thickness.

Model Processes these inputs through the trained algorithm.

Model Outputs either:

0 → Not likely diabetic

1 → Likely diabetic

Result is Displayed to the user immediately.
