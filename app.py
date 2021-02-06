from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home(): 
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form["valor1"] != "" and request.form["valor2"] != ""):
            valor1 = request.form["valor1"]
            valor2 = request.form["valor2"]

            if (request.form["opc"] == "soma"):
                soma = int(valor1) + int(valor2)
                return str(soma)

            elif (request.form["opc"] == "subt"):
                subt = int(valor1) - int(valor2)
                return str(subt)

            elif (request.form["opc"] == "mult"):
                mult = int(valor1) * int(valor2)
                return str(mult)

            else:
                divi = int(valor1) // int(valor2)
                return str(divi)

        else:
            return "Informe um valor válido!"

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

app.run(port=8080, debug=True)