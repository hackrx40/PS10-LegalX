# PS10-LegalX : Fraud & Legal - Third Party Legal Claims

## About
In recent times, the legal landscape has witnessed an unsettling rise in false third-party legal claims, which poses a significant challenge to the justice system and adversely impacts individuals, businesses, and society at large. The insurance company have to make sure that all the policies being true. Creating the final draft is time consuming task as the format is almost similar for all the cases and there are many conditions in which the final verdict is same. Our aim is to develop a solution to prepare the draft so that the insurance company could easily check the draft and verify whether the claim is valid or not. We are using Machine Learning and NLP models to automatically generate case drafts.

## Team Members
```
1. Mohd. Altaf Khan           VIT Chennai
2. Kesav Santhosh             VIT Chennai
3. Harshenee CB               VIT Chennai
4. A Venkata Vignesh Reddy    VIT Chennai
5. M Rokithkumar              VIT Chennai
```

## Features
* OCR to Convert Scanned Images of Reports and Documents into Text Format
* Automated Written Statement Generator
* Can refer Multiple Case Reports
* Database to Store Keywords 
* GUI for Users to Upload Case Reports


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
  4. python-docx
    >> pip install python-docx
  5. PyMuPDF
    >> pip install PyMuPDF
  6. pillow
    >> pip install pillow
  7. reportLab
    >>pip install reportLab
  8. pytesseract
    >>pip install pytesseract
    If any error persists then [(https://github.com/UB-Mannheim/tesseract/wiki)](https://github.com/UB-Mannheim/tesseract/wiki) use this       link and download pytesseract and then copy pytesseract.exe path link from your folder to use pyteserract
  9. openai
    >>pip install openai
```
If any libraries in the App.py is not pre-installed please use "pip install XXXX" here XXXX be the library name in cmd.

## MySQL Configuration
Run the following commands in the MySQL Command Line Client
```
  mysql> create database legalx;
  mysql> use legalx;
  mysql> create table casetable(casetype varchar(50),keyword varchar(255));
```

## How to Run the Program
1. Install App Folder
2. Open Compiler
3. Say if you are using Visual Code Studio, then open the above installed Folder.
4. Now execute App.py file.
5. If there is no error in your installation, in the terminal you may find the following:
```
 * Serving Flask app 'App' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX
```
6. Use CTRL + Click the http://127.0.0.1:5000 this will open a brower or manually enter URL- http://127.0.0.1:5000/ in any of your browsers.
7. There you go, You have the Cover page of the LegalX Web Application in Front of you.


## GUI
### INDEX
![Index](https://github.com/hackrx40/PS10-LegalX/assets/75007002/de5395fe-86c2-47ea-8747-4ab7f7ae245f)
### INPUT
![Input](https://github.com/hackrx40/PS10-LegalX/assets/75007002/cf4ba8a8-2d9b-428f-89f4-fa75b1a03c97)
### UPLOAD
![Upload](https://github.com/hackrx40/PS10-LegalX/assets/75007002/cfc68977-8a74-4aa1-8d29-7f531ff7b36e)
### ABOUT
![About](https://github.com/hackrx40/PS10-LegalX/assets/75007002/5e68066e-8fda-43aa-b92b-f5c9a0c64336)




