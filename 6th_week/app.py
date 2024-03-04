from flask import Flask, render_template, request, redirect


app = Flask(__name__)

todos_list = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = request.form
        print(form_data)
        todos_list.append(form_data["todo"])
        print(todos_list)
        return redirect("/")

    return render_template("index.html", todos=todos_list)


app.run(debug=True, port=5001)
