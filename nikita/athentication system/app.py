from flask import Flask,render_template,url_for,request,redirect 
import mysql.connector as mc 

app  = Flask(__name__) 

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signupdata',methods=['GET','POST'])
def signupdata():
    if request.method == 'POST':
        user_name = request.form['name'] 
        user_email = request.form["email"]
        user_password = request.form['password']

        conn = mc.connect(user="root",host="localhost",database='radhey',password="Radhey254875")
        mycursor = conn.cursor()
        query = 'insert into sign (name,email,password) values(%s,%s,%s)'

        user_data = (user_name,user_email,user_password)
        mycursor.execute(query,user_data)
        conn.commit()
        mycursor.close()
        conn.close()

        return f"Hey {user_name} sigun done"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logindata',methods=['GET','POST'])
def logindata():
    if request.method== 'POST':
        user_name = request.form['name']
        user_email = request.form['email']
        user_password = request.form['password']


        ## compare with sign-up data 
        conn = mc.connect(user="root",host="localhost",database='radhey',password="Radhey254875")
        mycursor = conn.cursor()
        query = "select * from sign"
        mycursor.execute(query)
        user_data = mycursor.fetchall()
        for row in user_data:
            # if (user_email in row) and (user_password in row) and (user_name in row):
                    # return redirect("profile")  
            if user_email in row:
                if user_password in row:
                    return redirect(url_for("profile",name=user_name))

        return "your id and password is not matched"


# dynamic  url (url + input )
@app.route('/profile/<name>')  # ip:host/profile/ranjit
def profile(name):
    return f"Hey {name} you have successfully login"

if __name__ == "__main__":
    app.run(debug=True)