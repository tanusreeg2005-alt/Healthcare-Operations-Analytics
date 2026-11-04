#importing libraries

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#loading datas

df= pd.read_csv('healthcare_dataset.csv')
print(df)

#inspect data

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe()) #statistical summary

#data cleaning

#removing duplicates
df= df.drop_duplicates()
print(df.duplicated().sum())

#cleaning name and columns
df['Name']=df['Name'].str.strip().str.title()
print(df.head())

#fix negative billing ammount
df.loc[df['Billing Amount']<0,'Billing Amount']=df['Billing Amount'].mean()
print(df.describe())

#converting dates into date nd time format 
df['Date of Admission']=pd.to_datetime(df['Date of Admission'])
df['Discharge Date']=pd.to_datetime(df['Discharge Date'])

print(df.dtypes)

#creating another column of stay days count
df['Length_of_stay']=(df['Discharge Date']-df['Date of Admission']).dt.days
print(df.head())


#final cleaning check
print(df.isnull().sum())
print(df.shape)

#data analysis and data visualization

#q.1-- which medical condition affects the  ost patient across the network
condition_count=df['Medical Condition'].value_counts()
print(condition_count)
#plotiing this all
plt.figure(figsize=(8,5))
plt.bar(condition_count.index,condition_count.values,color='#7833fe')
plt.title('Patients by Medical Condition')
plt.xlabel('Medical Condition')
plt.ylabel('Number of Patients')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

##q.2--how patient age distributed across network
print(df.head())

average_age = df['Age'].mean()
print(average_age)

#histogram
plt.figure(figsize=(8,5))
plt.hist(df['Age'],bins=20,color='red',edgecolor='black')
plt.title('Age Distribution of Patients')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.tight_layout()
plt.show()

#q.3--how has average treatment cost changed over time
average_cost= df['Billing Amount'].mean()
print(average_cost)

#month wise calculation
df['Admission_month']=df['Date of Admission'].dt.to_period('M')
#print(df.head()) for inspection
monthly_avg_cost= df.groupby('Admission_month')['Billing Amount'].mean()
print(monthly_avg_cost)
#line chart
plt.figure(figsize=(10,5))
plt.plot(monthly_avg_cost.index.astype(str), monthly_avg_cost.values, color='#7833FE', marker='o',markersize=3)
plt.title("Average Treatment Cost Overe Time (monthly)")
plt.xlabel('Month')
plt.ylabel('Average Billing Amount')
plt.tight_layout()
plt.xticks(rotation=90)
plt.show()

#q.4-- is there a relationship between patients age and treatment cost
senior_avg_cost= df.loc[df['Age']>=60, 'Billing Amount'].mean()
print(senior_avg_cost)
#scatter plot
sample_df=df.sample(1000,random_state=1)#because we have 55k+ records so we will be using random 1000 records to perform analysation
plt.figure(figsize=(8,5))
plt.scatter(sample_df['Age'],sample_df['Billing Amount'],color='Purple',alpha=0.5,s=15)
plt.title('Age vs Treatment Cost')
plt.xlabel('Age')
plt.ylabel('Billing Amount')
plt.tight_layout()
plt.show()

#q.5--which i9nsurance covers the most patients
insurance_count=df['Insurance Provider'].value_counts()
print(insurance_count)
#piechart
plt.figure(figsize=(7,7))
plt.pie(insurance_count.values,labels=insurance_count.index,autopct='%1.1f%%',colors=['red','green','blue','purple','yellow'])
plt.title('Patient Share by Insurace Provider')
plt.tight_layout()
plt.show()

#ad-hoc question
#AD-HOC QUESTION.1--Emergency Department Capacity Planning
#business scenario 1: the hospital management is planning staffing for emergency cases, they want to know howmany emergency admissions occured in each month
emergency_month=(df.loc[df['Admission Type']=='Emergency'].groupby(df['Date of Admission'].dt.month).size())
print(emergency_month)

#AD-HOC QUESTION.2--Identify High Cost Patient Groups
#business scenario 2: hospital fiance team wants to identify patients who have usually high billing amounts so they can review those cases
high_cost_patients= df.loc[df['Billing Amount']>df['Billing Amount'].quantile(0.90)]
#print(high_cost_patients)
print(high_cost_patients.shape[0])


#AD-HOC QUESTION 3 -- Flagging Emergency Cases wuth Abnormal Result for Review 
#business scenarion 3: hospital management wants to identify emergency patients whose test result are abnormal so these cases can be prioritized for review
priority_cases = df.loc[(df['Admission Type']=='Emergency')&(df['Test Results']=='Abnormal')]
print(priority_cases.shape[0])