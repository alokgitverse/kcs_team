from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def index():
    return "API Successful"

@app.route("/user_input",methods=['GET','POST'])
def user_input():
    return render_template('one.html')



if __name__=="__main__":
    app.run(debug=True)