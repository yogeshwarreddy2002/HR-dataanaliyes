import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\hr_attrion_dataanalyes_project\\HR-Employee-Attrition.csv")
st.title("HR Attrition Analysis")
st.write("This application analyzes employee attrition data to identify key factors contributing to employee turnover.")
sidebar=st.sidebar.radio("📂Complete Employee Attrition Dataset",("Upload Dataset","Data Cleaning","Statistical Analysis","Visualization","Ages of employees leaving"))
if sidebar=="Upload Dataset":
  st.header("Upload HR Employee Attrition Dataset") 
  st.dataframe(df) 
elif sidebar=="Data Cleaning": 
  st.subheader("data Cleaning")
  st.write("Checking for missing values in the dataset:")
  null=df.isnull().sum()
  st.write(null)
  st.write("Data Types of each column:")
  datatypes=df.dtypes
  st.write(datatypes)
elif sidebar=="Statistical Analysis":
    st.subheader("Statistical Analysis")
    desc=df.describe()
    st.write(desc)
elif sidebar=="Visualization":
    col1, col2 = st.columns(2)
    with col1:
     st.subheader("Total employees👥")
     total_count=df['Attrition'].value_counts()
     col1.metric("Total Employees", total_count.sum())
     st.subheader("Attrition Rate 📉")
     attrition_rate=(total_count['Yes']/total_count.sum())*100
     col1.metric("Attrition Rate (%)", f"{attrition_rate:.2f}%")
     st.subheader("Data Visualization")
     st.write("Attrition by Department")
    #  plt.figure(figsize=(5,3))
     dept=df.groupby("Department").agg({"Attrition":"value_counts"}).unstack()
     dept.plot(kind="bar", color=['orange', 'purple', 'cyan'])
     plt.title("Attrition by Department")
     plt.xlabel("Department")
     plt.ylabel("Number of Employees")
     st.pyplot(plt)
     st.write("Attrition by Job Role")
     job=df.groupby("JobRole")["Attrition"].value_counts().unstack()
     job.plot(kind="barh", stacked=True, color=['green', 'red'])
     plt.title("Attrition by Job Role")
     plt.xlabel("Job Role")
     plt.ylabel("Number of Employees")
     st.pyplot(plt)
   
    with col2:
     st.subheader("Attrition Count ❌")
     attrition_count=df['Attrition'].value_counts()
     col2.metric("Attrition Count", attrition_count['Yes'])
     st.subheader("Avg Salary 💰")
     avg_salary=df['MonthlyIncome'].mean()
     col2.metric("Average Salary", f"₹{avg_salary:.2f}")
     st.subheader("Data Visualization")
     st.write("Attrition vs OverTime")
     overtime=df.groupby("OverTime")["Attrition"].value_counts().unstack()
     plt.figure(figsize=(3,3))
     overtime.plot(kind="pie",y='Yes',autopct='%1.1f%%',colors=['lightblue','lightgreen'])
     plt.title("Attrition vs OverTime")
     st.pyplot(plt)
     st.write("Attrition by Monthly Income")
     income=df.groupby("MonthlyIncome")["Attrition"].value_counts().unstack()
     plt.figure(figsize=(3,3))
     income.plot(kind="line")
     plt.title("Attrition by Monthly Income")
     plt.xlabel("Monthly Income")
     plt.ylabel("Number of Employees")
     st.pyplot(plt)
elif sidebar=="Ages of employees leaving":
    st.subheader("Ages of Employees Leaving")
    option = st.selectbox("Select ages",("oldest ages","youngest ages"))
    if option=="oldest ages":
        st.write("Top 10 Oldest Ages of Employees Leaving")
        ages=df[["Age","Attrition"]]
        ages.sort_values(by='Age',ascending=False,inplace=True)
        top_10_ages = ages[['Age', 'Attrition']].head(10)
        st.markdown("### Top 10 Oldest Ages of Employees Leaving")
        st.dataframe(top_10_ages)
    elif option=="youngest ages":
        st.write("Top 10 Youngest Ages of Employees Leaving")
        ages=df[["Age","Attrition"]]
        ages.sort_values(by='Age',ascending=True,inplace=True)
        top_10_ages = ages[['Age', 'Attrition']].head(10)
        st.markdown("### Top 10 Youngest Ages of Employees Leaving")
        st.dataframe(top_10_ages)




