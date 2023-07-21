from flask import Flask, render_template, request
import mysql.connector

def mysqlinsert(casetype, keyword):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Rokith@1234",
        database="legalx"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO casetable (casetype, keyword) VALUES (%s, %s)"
    val = (casetype, keyword)
    mycursor.execute(sql, val)
    mydb.commit()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/uploadfiles', methods=['POST'])
def uploadfiles():
    casetype = request.form['caseType']
    mysqlinsert(casetype, "hello")
    return render_template('upload.html', message="Analyzing Files. Please Wait!!")


if __name__ == '__main__':
    app.run(debug=True)
