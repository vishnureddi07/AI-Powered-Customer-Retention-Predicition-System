import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import seaborn as sns
import sys
import os
import warnings
warnings.filterwarnings('ignore')



class churnprediction:
    def __init__(self,path):
        try:
            self.path = path
            self.data = pd.read_csv(path)
            print(self.data.sample(10))

        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            print(f'ERROR IN line no : {error_line.tb_lineno}: due to{error_msg}')
    def visualization(self):
        try:
            self.data=self.data.drop(columns=['customerID'],axis=1)
            print(self.data.sample(10))
            self.data['SeniorCitizen']=self.data['SeniorCitizen'].map({1:'Yes',0:'No'})
            print(self.data.sample(10))
            print(self.data.info())
            # Replaces non-numeric strings (like empty spaces) with NaN and converts to float
            self.data['TotalCharges'] = pd.to_numeric(self.data['TotalCharges'], errors='coerce')
            print(self.data.info())
            # visualization for churn counts
            #================================================
            churn_count=self.data['Churn'].value_counts()
            plt.figure(figsize = (5,3))
            ax=churn_count.plot(kind='bar', color=['r', 'black'])
            ax.bar_label(ax.containers[0])

            plt.xlabel('churn')
            plt.ylabel('count')
            plt.title('distribution of churn')
           # plt.show()

            # visualization for gender
            gender_count=self.data['gender'].value_counts()
            plt.figure(figsize = (5,3))
            ax=gender_count.plot(kind='bar', color=['r', 'black'])
            ax.bar_label(ax.containers[0])
            plt.xlabel('gender')
            plt.ylabel('count')
            plt.title('distribution of gender')
            plt.show()

            #================= distrubution between grender and churn
            gender_churn = pd.crosstab(self.data['gender'], self.data['Churn'])

            ax = gender_churn.plot(kind='bar', figsize=(5, 3))

            # add labels to BOTH containers
            for container in ax.containers:
                ax.bar_label(container)

            plt.xlabel('Gender')
            plt.ylabel('Count')
            plt.title('Gender vs Churn')
            plt.show()

            # distribution for senior citizn
            plt.figure(figsize=(8, 8))
            senior_count = self.data['SeniorCitizen'].value_counts()

            plt.subplot(1,2,1)
            ax = senior_count.plot(kind='bar', color=['r', 'black'])
            ax.bar_label(ax.containers[0])
            plt.title('distribution of gender')
            plt.xlabel('senior citizen')
            plt.ylabel('count')


            #============ distribution between senior citizen and charn
            senior_citizen_churn = pd.crosstab(self.data['SeniorCitizen'], self.data['Churn'])
            plt.subplot(1,2,2)


            ax=senior_citizen_churn.plot(kind='bar')
            ax.bar_label(ax.containers[0])

            plt.xlabel('Senior Citizen')
            plt.ylabel('Count')
            plt.title('Senior Citizen vs Churn')
            plt.show()

            #====distribution dependent and churn
            dependent_churn=pd.crosstab(self.data['Dependents'],self.data['Churn'])
            plt.figure(figsize=(5, 3))
            ax = dependent_churn.plot(kind='bar',color=['r','g'])
            ax.bar_label(ax.containers[0])

            plt.xlabel('dependent')
            plt.ylabel('Count')
            plt.title('dependent vs Churn')
            plt.show()

           #=================























        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            print(f'ERROR IN line no : {error_line.tb_lineno}: due to{error_msg}')

if __name__ == "__main__":
    try:
        obj=churnprediction('C:\\Users\\PC\\OneDrive\\Attachments\\Desktop\\intership\\project-01\\Telco_Data_With_Tax_Gateway_Updated.csv')
        obj.visualization()
    except Exception as e:
        error_type,error_msg,error_line=sys.exc_info()
        print(f'ERROR IN line no : {error_line.tb_lineno}: due to{error_msg}')

