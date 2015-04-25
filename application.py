from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/application-form")
def display_application():
	return render_template('application-form.html')

@app.route("/application")
def get_application_input():
	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	salary = request.form.get("salary")
	position = request.form.get("position")

	return render_template('application.html', firstname=firstname, lastname=lastname, salary=salary, position=position)

if __name__ == "__main__":
    app.run(debug=True)