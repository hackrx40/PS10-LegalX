# PS10-LegalX
## Team Members
1. Mohd. Altaf Khan           VIT Chennai
2. Kesav Santhosh             VIT Chennai
3. Harshenee CB               VIT Chennai
4. A Venkata Vignesh Reddy    VIT Chennai
5. M Rokithkumar              VIT Chennai

## Features
* OCR to Convert Scanned Images of Reports and Documents into Text Format
* Automated Written Statement Generator
* Can refer Multiple Case Reports
* Database to Store Keywords 
* GUI for Users to Upload Case Reports
  
## Overview of our solution
In recent times, the legal landscape has witnessed an unsettling rise in false third-party legal claims, which poses a significant challenge to the justice system and adversely impacts individuals, businesses, and society at large. The insurance company have to make sure that all the policies being true. Creating the final draft is time consuming task as the format is almost similar for all the cases and there are many conditions in which the final verdict is same. Our aim is to develop a solution to prepare the draft so that the insurance company could easily check the draft and verify whether the claim is valid or not. We are using Machine Learning and NLP models to automatically generate case drafts.

## Process Flow
<img src=https://github.com/hackrx40/PS10-LegalX/assets/138132906/ffdc7b5b-406e-46d7-bacd-1d06cc5be706>

## Solution Architecture
<img src=https://github.com/hackrx40/PS10-LegalX/assets/138132906/9316315f-2574-4b6b-9e85-136a68606d21>

## Supported Platforms
* Windows
* Linux
* macOS

## Requirements
* Compiler (Recommended: Visual Studio Code)
* MySQL Community Server 8.0.24
* Python 3.9
  
## Installation of Requirements
1. Python 3.9
   * Install Python from this [Link](https://www.python.org/downloads/release/python-396/)
2. MySQL
   * Download Windows (x86, 32-bit), MSI Installer from [here](https://downloads.mysql.com/archives/installer/)
   * Then Run the above installed Installer and then please make note of the password.
   
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
