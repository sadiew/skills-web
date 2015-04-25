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
	firstname = request.args.form("firstname")
	lastname = request.args.form("lastname")
	salary = request.args.form("salary")
	position = request.args.form("position")

	return render_template('application.html', firstname=firstname, lastname=lastname, salary=salary, position=position)

if __name__ == "__main__":
    app.run(debug=True)