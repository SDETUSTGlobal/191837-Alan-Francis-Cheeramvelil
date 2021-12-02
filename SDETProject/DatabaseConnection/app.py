import mysql
from flask import Flask, render_template,request
from flask_mysqldb import MySQL
app = Flask(__name__) # Creates the Flask application object that contains methods on how

app.config['MYSQL_HOST'] = 'localhost' #config object allows us to assign values to configuration variables, which can be accessed throughout our application.
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Alan2702'
app.config['MYSQL_DB'] = 'Project'

mysql = MySQL(app) #creates an instance which will provide us DB access.


@app.route('/', methods=['GET', 'POST']) # map the specific URL with the associated function that is intended to perform some task.
def login():
    if request.method == "POST":
        display= request.form   # used to collect values in a form with method="post".
        Name = display['Name']  #fetching values from the form
        ID = display['UID']
        Company=display['CName']
        Email = display['cemail']
        a = request.form['Name']
        b = request.form['UID']
        c = request.form['CName']
        d=  request.form['cemail']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Employee(Name,ID,Company,Email) VALUES (%s, %s,%s,%s)", (Name,ID,Company,Email))
        mysql.connection.commit()
        cur.close()

        return render_template('SDETProjectDisplay.html',aid=a,bid=b,cid=c,did=d)
    return render_template('SDETProjectLogin.html')
    # used to generate output from a template file



if __name__ == '__main__':
    app.run()