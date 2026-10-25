import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Prediction")

st.title("Customer Churn Prediction")
st.write("Enter customer details to predict churn.")

model = joblib.load("customer_churn_model.pkl")

tenure = st.slider("Tenure (months)", 0, 72, 12)

monthly_charges = st.number_input(
    "Monthly Charges", min_value=0.0, value=70.0
)

total_charges = st.number_input(
    "Total Charges", min_value=0.0, value=840.0
)

contract = st.selectbox(
    "Contract", ["Month-to-month", "One year", "Two year"]
)

internet = st.selectbox(
    "Internet Service", ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security", ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support", ["Yes", "No", "No internet service"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

if st.button("Predict Churn"):

    customer = pd.DataFrame([{
        "tenure": tenure,
        "TotalCharges": total_charges,
        "Contract_Two year": int(contract == "Two year"),
        "MonthlyCharges": monthly_charges,
        "InternetService_Fiber optic": int(internet == "Fiber optic"),
        "PaymentMethod_Electronic check": int(
            payment == "Electronic check"
        ),
        "Contract_One year": int(contract == "One year"),
        "TechSupport_No internet service": int(
            tech_support == "No internet service"
        ),
        "OnlineSecurity_Yes": int(online_security == "Yes"),
        "TechSupport_Yes": int(tech_support == "Yes"),
        "OnlineSecurity_No internet service": int(
            online_security == "No internet service")
    }])

    try:
        # Ensure columns match the model's training order
        customer = customer[model.feature_names_in_]

        prediction = model.predict(customer)[0]
        probability = model.predict_proba(customer)[0]

        st.write("Stay probability:", round(probability[0] * 100, 2), "%")
        st.write("Churn probability:", round(probability[1] * 100, 2), "%")

        if prediction == 1:
            st.error("Prediction: Customer may churn.")
        else:
            st.success("Prediction: Customer is likely to stay.")

    except Exception as e:
        st.error(f"Prediction error: {e}")