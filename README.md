# 💰 AWS Cloud Service Cost Calculator

A **Streamlit-based web application** that estimates **AWS Cloud Service Costs** before usage. This tool helps users **pre-calculate expenses** for EC2, S3, Lambda, and RDS services.

## 🚨 Problem Statement

### **❌ Lack of Cost Transparency in AWS Services**
Many users, especially **startups, developers, and students**, struggle with **unexpected AWS bills** because AWS does not **clearly display pricing before usage**. Services like **EC2, S3, Lambda, and RDS** have complex pricing structures, making cost estimation **difficult and unpredictable**.  

## ✅ Solution: AWS Cost Calculator

This **Streamlit-based tool** allows users to:  
✔ **Estimate AWS Costs Before Usage** – Avoid unexpected charges.  
✔ **Get INR Pricing** – Convert AWS costs from USD to INR for better understanding.  
✔ **Plan Cloud Budgets** – Helps developers and businesses **plan cloud expenses**.  
✔ **Quick & Interactive UI** – Users can easily enter **instance details, storage size, execution time, and requests** to get real-time cost estimates.  

### **🎯 Example Use Cases**
🔹 A **student** using AWS Free Tier **wants to ensure their EC2 instance won’t exceed free limits**.  
🔹 A **startup** needs to budget its **AWS Lambda costs** before deploying a serverless application.  
🔹 A **developer** wants to compare **S3 storage pricing** across different storage classes.  

---

## 🚀 Features

✅ **EC2 Cost Estimation** – Calculate monthly costs based on instance type and usage hours.  
✅ **S3 Storage Estimation** – Estimate costs based on storage size and class.  
✅ **Lambda Function Estimation** – Predict costs based on execution time, memory usage, and invocations.  
✅ **RDS Database Estimation** – Compute monthly expenses for different database engines.  
✅ **INR Currency Support** – Prices are converted from USD to INR using a fixed exchange rate (1 USD = ₹83).  
✅ **Modern UI** – Sidebar navigation, intuitive input fields, and interactive sliders.  

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/aws-cost-calculator.git
cd aws-cost-calculator
pip install -r requirements.txt
