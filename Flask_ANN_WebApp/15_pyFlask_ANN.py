#Flask: Micro Web Applicaion Framework in Python
#Based on werkzueg(request, response, get, post), wsgi(web-server gateway interface) toolkit
#No abstraction, data base handling, validating layers. But can be added to it
from flask import Flask, redirect, url_for

app = Flask(__name__) #__name__ takes current module as ragument

#The route function works as decorator. It will tell which url the application should be associated with
#app.route(rules, options)
#The rule option represent url/html pages the app shud be associated with
@app.route("/admin/<name>") 
#by using / , when app runs the below function shud be executed
#Now when app runs, in browser type localhost:5000 to open the website which returns hello - app.route("/")
#Now when app runs, in browser type localhost:5000/admin to open the website which returns hello - app.route("/admin")
#Now when app runs, in browser type localhost:5000/admin/pop to open the website which returns hello pop - app.route("/admin/<name>")
def hello_admin(name):
    return "hello %s"%name

@app.route("/guest/<guest>")

def hello_guest(guest):
    return "hello guest %s"%guest

@app.route("/user/<user>")

def hello_user(user):
    if user == "vaish":
        return redirect(url_for("hello_admin",name=user)) #redirecting url based on name provided
    else:
        return redirect(url_for("hello_guest", guest = user))


if __name__ == "__main__":
    app.run(debug=True)







