# Students Test Score Prediction - Mayank Sharma

## Introduction About the Data :
The goal is to predict test score of Students (Regression Analysis).

There are 7 independent variables :

**Dataset information**

gender : sex of students -> (Male/female)
race/ethnicity : ethnicity of students -> (Group A, B,C, D,E)
parental level of education : parents' final education ->(bachelor's degree,some college,master's degree,associate's degree,high school)
lunch : having lunch before (standard or free/reduced)
preparation course : complete or not complete before test
reading score
writing score

**Target variable:**

math score : score in math test.

Dataset Source is csv file which is given in github notbook/data.

## Approach for the project

**Data Ingestion :**
In Data Ingestion phase the data is first read as csv.
Then the data is split into training and testing and saved as csv file.

**Data Transformation :**
In this phase a ColumnTransformer Pipeline is created.
for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
for Categorical Variables SimpleImputer is applied with most frequent strategy, then one hot encoding performed , after this data is scaled with Standard Scaler.
This preprocessor is saved as pickle file.

**Model Training :**
In this phase base model is tested. 
After this hyperparameter tuning is performed and best model found was Logistic Regression.
This model is saved as pickle file.

**Prediction Pipeline :**
This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

**Flask App creation :**
Flask app is created with User Interface to predict the Student math score inside a Web Application.

**Deployment Using Docker :**
1. Created Dockerfile.
2. Created github/workflow -main.yaml file using github actions for CICD deployment in AWS EC2.
3. Using docker desktop created image then run container using that image.
4. Pushed app-image to docker hub.
5. Login to Amazon console.
6. created ECR repository for image building.
7. Created IAM user and configured AmazonEC2ContainerRegistryFullaceess and AmazonEC2 permissions along with security groups there.
8. creating access key and downloading those to use in gitub.
9. Launcehd EC2 instance and connected that instance to docker using docker commands.
10. Connecting EC2 to Github runner using github runner commands from github Actions tab.
11. Naming runner as self-hosted and adding security keys in secrets and variable tab.
12. Deployment is ready, as we update anything in github code same thing will be pushed to AWS EC2 instance.

## Scrrenshot of Github and EC2 Connection :

![Screenshot (30)](https://github.com/mayank00927/Students_Test_Score_Prediction/assets/96683686/b9d4d934-24d0-4ce6-8725-ed044c71f600)
