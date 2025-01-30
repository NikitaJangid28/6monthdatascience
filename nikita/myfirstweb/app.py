from flask import Flask , render_template , url_for , request 
import mysql.connector as mc 
conn = mc.connect(user='root',password="Radhey254875",host="localhost",database='radhey')
app = Flask(__name__)


@app.route("/")   # ip:port/
def home():
    # return "Hey welcome to you in flask application"
    return render_template('index.html')


@app.route("/about")  # ip:port_no/about
def about():
    # return "Hey you are at about page url" 
    return render_template('about.html')

@app.route('/userdata')
def userdata():
    return render_template("fill_the_data.html")

# @app.route("/submitdata",methods=['GET','POST'])
# def submitdata():
#     if request.method == 'POST':
#         user_data = request.form   #{k:v}
#         name = user_data['name']
#         return name  


@app.route("/submitdata",methods=['GET','POST'])
def submitdata():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form['email']
        contact = request.form["contact"]
        password = request.form['password']

        query = """
        INSERT INTO userdata (name ,gmail, contact ,password)
        VALUES (%s,%s,%s,%s)
        """
        mycursor = conn.cursor()
        user_data = (name,email,contact,password)
        mycursor.execute(query,user_data)
        conn.commit()
        
        mycursor.close()
        conn.close()

        return "Your data is sent to the database 😊!"


# ip:port_no/contact
@app.route('/contact') 
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')


if __name__ == "__main__":
    app.run(debug=True)

    