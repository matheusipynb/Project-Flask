from flask import Flask, render_template, request

app = Flask(__name__)


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"


@app.route("/", methods=["GET", "POST"])
def index():
    imc = None
    classificacao = None
    erro = None

    if request.method == "POST":
        try:
            peso = float(request.form.get("peso", "").replace(",", "."))
            altura = float(request.form.get("altura", "").replace(",", "."))

            if peso <= 0 or altura <= 0:
                erro = "Informe valores maiores que zero."
            elif altura > 2.5:
                erro = "A altura deve estar em metros. Exemplo: 1.75"
            else:
                imc = calcular_imc(peso, altura)
                classificacao = classificar_imc(imc)

        except ValueError:
            erro = "Digite apenas números válidos."

    return render_template(
        "index.html",
        imc=imc,
        classificacao=classificacao,
        erro=erro
    )


if __name__ == "__main__":
    app.run(debug=True)