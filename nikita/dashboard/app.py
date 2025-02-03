from flask import Flask , render_template 
import mysql.connector as mc 
app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/dashboard")
def dashboard():
    # return render_template('dashboard.html',username="Mohit",password="dlkfd",contanct=9759194985)
    conn = mc.connect(user="root",host="localhost",database='radhey',password="Radhey254875")

    mycursor = conn.cursor()

    query = "select * from userdata"
    mycursor.execute(query)
    data = mycursor.fetchall()  # [(),(),()]
    mycursor.close()
    conn.close()
    
    return render_template('dashboard.html',userdetails=data)


if __name__ == "__main__":
    app.run(debug=True)