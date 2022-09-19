from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def first_page():
   return render_template("login_pass.html")
@app.route("/login_pass.html")
def login_pass():
   return render_template("login_pass.html")
@app.route("/main.html")
def main_page():
   return render_template("main.html")
@app.route("/auto.html")
def auto_page():
   return render_template("auto.html")
@app.route("/contacts.html")
def contacts_page():
   return render_template("contacts.html")
@app.route("/log", methods=["POST"])
def log():
   login = request.form["login"]
   password = request.form["password"]
   if (login == "Daniil") and (password == "2022"):
       return render_template("main.html")
   else:
       return "Вы ввели неверный логин или пароль"
if __name__ == "__main__":
     app.run(debug=True)
