from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/fortune', methods = ["GET", "POST"])
def fortune():
    if request.method == "POST":

        username = request.form.get("username")
        color = request.form.get("color")
        number = request.form.get("number")

        if color == 'red':
            if number == '1':
                return render_template("fortuner1.html", username=username, color=color, number=number)
            elif number == '2':
                return render_template("fortuner2.html", username=username, color=color, number=number)
            elif number == '3':
                return render_template("fortuner3.html", username=username, color=color, number=number)
            elif number == '4':
                return render_template("fortuner4.html", username=username, color=color, number=number)
        
        elif color == 'yellow':
            if number == '1':
                return render_template("fortuney1.html", username=username, color=color, number=number)
            elif number == '2':
                return render_template("fortuney2.html", username=username, color=color, number=number)
            elif number == '3':
                return render_template("fortuney3.html", username=username, color=color, number=number)
            elif number == '4':
                return render_template("fortuney3.html", username=username, color=color, number=number)

        elif color == 'green':
            if number == '1':
                return render_template("fortuneg1.html", username=username, color=color, number=number)
            elif number == '2':
                return render_template("fortuneg2.html", username=username, color=color, number=number)
            elif number == '3':
                return render_template("fortuneg3.html", username=username, color=color, number=number)
            elif number == '4':
                return render_template("fortuneg4.html", username=username, color=color, number=number)

        elif color == 'blue':
            if number == '1':
                return render_template("fortuneb1.html", username=username, color=color, number=number)
            elif number == '2':
                return render_template("fortuneb2.html", username=username, color=color, number=number)
            elif number == '3':
                return render_template("fortuneb3.html", username=username, color=color, number=number)
            elif number == '4':
                return render_template("fortuneb4.html", username=username, color=color, number=number)

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)