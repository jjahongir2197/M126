from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/sum3", methods=["GET", "POST"])
def sum3():
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        c = int(request.form["c"])

        result = a + b + c

        return render_template("result16.html", result=result)

    return render_template("index16.html")

if __name__ == "__main__":
    app.run(debug=True)
