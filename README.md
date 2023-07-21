# PS10-LegalX

## Team Members
Mohd. Altaf Khan - VIT Chennai
Kesav Santhosh - VIT Chennai
Harshenee CB - VIT Chennai
A Venkata Vignesh Reddy - VIT Chennai
M Rokithkumar - VIT Chennai

## Overview of our solution
In recent times, the legal landscape has witnessed an unsettling rise in false third-party legal claims, which poses a significant challenge to the justice system and adversely impacts individuals, businesses, and society at large. The insurance company have to make sure that all the policies being true. Creating the final draft is time consuming task as the format is almost similar for all the cases and there are many conditions in which the final verdict is same. Our aim is to develop a solution to prepare the draft so that the insurance company could easily check the draft and verify whether the claim is valid or not. We are using Machine Learning and NLP models to automatically generate case drafts.

## Process Flow
<img src=https://github.com/hackrx40/PS10-LegalX/assets/138132906/ffdc7b5b-406e-46d7-bacd-1d06cc5be706>

## Solution Architecture
<img src=https://github.com/hackrx40/PS10-LegalX/assets/138132906/9316315f-2574-4b6b-9e85-136a68606d21>

## Installation of Libraries
Please enter the following commands to download the required libraries
```
  1. mysql.connector
    >> pip install mysql-connector-python
  2. flask
    >> pip install flask
  3. numpy
    >> pip install nltk
  
```
If any libraries in the App.py is not pre-installed please use "pip install XXXX" here XXXX be the library name in cmd.

## MySQL Configuration
Run the following commands in the MySQL Command Line Client
```
  mysql> create database legalx;
  mysql> use legalx;
  mysql> create table casetable(casetype varchar(50),keyword varchar(255));
```
