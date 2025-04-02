from flask import Flask,render_template
# from flask_mysqldb import MySQL

app=Flask(__name__)
 
# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_PORT']=3306
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']='1423'
# app.config['MYSQL_DB']='flask_db'
 
# mysql=MySQL(app)
 


@app.route("/signup")
def home():
    return  render_template("signup.html")

@app.route("/login")
def login():
      return render_template("login.html")
@app.route('/')
def index():
       return render_template('index.html')
@app.route('/home')
def home5():
      return render_template('home.html')
@app.route('/campus')
def campus():
      return render_template('campus.html')
@app.route('/placements')
def placements():
      return render_template("placements.html")
@app.route('/branches')
def branches():
      return render_template("branches.html")
@app.route('/cse')
def cse():
      return render_template("cse.html")
@app.route('/ece')
def ece():
      return render_template("ece.html")
@app.route('/mech')
def mech():
      return render_template("mech.html")
@app.route('/civil')
def civil():
      return render_template("civil.html")
@app.route('/eee')
def eee():
      return render_template("eee.html")

@app.route('/exam')
def exam():
      return render_template("exam.html")

@app.route('/contact')
def contact():
      return render_template("contact.html")
@app.route('/view')
def view():
      return render_template("view.html")
@app.route('/submit')
def submit():
      return render_template("submit.html")
@app.route('/student')
def student():
      return render_template("student.html")

if __name__=="__main__":
       app.run(debug=True)

