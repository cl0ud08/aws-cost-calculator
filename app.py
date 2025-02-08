import streamlit as st
import requests
import pandas as pd

# Conversion Rate (Example: 1 USD = 83 INR)
usd_to_inr = 83

# Function to fetch EC2 pricing
def get_aws_ec2_pricing():
    url = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/index.json"
    response = requests.get(url)
    data = response.json()
    instances = []
    
    for sku, details in data["products"].items():
        if "attributes" in details and "instanceType" in details["attributes"]:
            instances.append({
                "Instance Type": details["attributes"]["instanceType"],
                "Region": details["attributes"].get("location", "N/A"),
                "Price Per Hour": data["terms"]["OnDemand"].get(sku, {}).get("priceDimensions", {}).get("pricePerUnit", "N/A")
            })
    
    return pd.DataFrame(instances)

# Streamlit UI
st.set_page_config(page_title="AWS Cost Calculator", layout="wide")
st.title("💰 AWS Cloud Service Cost Calculator")
st.markdown("Estimate your cloud costs before usage! Select a service and enter details.")
st.sidebar.header("⚙️ Configuration")

service = st.sidebar.selectbox("Choose AWS Service", ["EC2", "S3", "Lambda", "RDS"])

if service == "EC2":
    st.subheader("EC2 Instance Cost Estimator")
    instance = st.text_input("Enter EC2 Instance Type", "t3.micro")
    hours = st.slider("Usage Hours per Month", 0, 720, 100)
    if st.button("💡 Estimate EC2 Cost"):
        cost_per_hour = 0.0116  # Example for t3.micro
        total_cost = cost_per_hour * hours * usd_to_inr
        st.success(f"Estimated Monthly Cost: ₹{total_cost:.2f}")

if service == "S3":
    st.subheader("S3 Storage Cost Estimator")
    storage_size = st.number_input("Enter Storage Size (GB)", min_value=1)
    storage_class = st.selectbox("Select Storage Class", ["Standard", "Infrequent Access", "Glacier"])
    if st.button("💾 Estimate S3 Cost"):
        s3_cost_per_gb = 0.023  # Example for Standard
        total_s3_cost = s3_cost_per_gb * storage_size * usd_to_inr
        st.success(f"Estimated S3 Cost: ₹{total_s3_cost:.2f}")

if service == "Lambda":
    st.subheader("Lambda Function Cost Estimator")
    execution_time = st.number_input("Execution Time (ms)", min_value=1)
    memory = st.number_input("Memory (MB)", min_value=128, step=128)
    requests = st.number_input("Number of Requests", min_value=1)
    if st.button("⚡ Estimate Lambda Cost"):
        price_per_request = 0.0000002  # Example price per invocation
        price_per_gb_second = 0.00001667  # Example price per GB-sec
        total_cost = ((requests * price_per_request) + ((memory / 1024) * (execution_time / 1000) * price_per_gb_second * requests)) * usd_to_inr
        st.success(f"Estimated Lambda Cost: ₹{total_cost:.2f}")

if service == "RDS":
    st.subheader("RDS Database Cost Estimator")
    db_engine = st.selectbox("Select Database Engine", ["MySQL", "PostgreSQL", "MongoDB"])
    instance_type = st.text_input("Enter RDS Instance Type", "db.t3.micro")
    storage_size = st.number_input("Storage Size (GB)", min_value=5)
    if st.button("🛢️ Estimate RDS Cost"):
        rds_cost_per_hour = 0.017  # Example price for db.t3.micro
        total_rds_cost = rds_cost_per_hour * 730 * usd_to_inr  # Assuming 24/7 usage
        st.success(f"Estimated RDS Monthly Cost: ₹{total_rds_cost:.2f}")