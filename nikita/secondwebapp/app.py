from flask  import Flask , render_template,url_for,request,session,redirect

app = Flask(__name__) 
app.secret_key = "djfdhfks35435"

@app.route('/')
def home():
    # return "Hey this my web page" 
    return render_template("home.html")

@app.route('/contact')
def contact():
    # return "hey this is about page"
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/submitdata",methods=['GET','POST'])
def submitdata():
    if request.method == "POST":

        # session = {}
        # data = request.form 
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        session["Name"] = name
        session['email'] = email 
        session['message'] = message 
        user_data = [name,email,message]
        return redirect('userdata')


@app.route('/userdata')
def userdata():
    print("Hii this userdata route")
    print()
    name = session["Name"]
    email = session['email']

    age = 25 
    branch = 'cse' 
    college = "jaipur"
    return f"Hey this is {name} and my email is {email}"

# route another 

# user_data = {"email":['a@gmail.com','b@gmail.com'],"password":['a123','b123']}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="2520",debug=True)

# 127.0.0.1   ==>   localhost 
# 0.0.0.0     ==>   anywhere ip 