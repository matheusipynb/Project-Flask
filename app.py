from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return {
            "nome": "Abaixo do peso",
            "cor": "azul",
            "nivel": 1
        }
    elif imc < 25:
        return {
            "nome": "Peso saudável",
            "cor": "verde",
            "nivel": 2
        }
    elif imc < 30:
        return {
            "nome": "Sobrepeso",
            "cor": "amarelo",
            "nivel": 3
        }
    elif imc < 35:
        return {
            "nome": "Obesidade grau I",
            "cor": "laranja",
            "nivel": 4
        }
    elif imc < 40:
        return {
            "nome": "Obesidade grau II",
            "cor": "vermelho",
            "nivel": 5
        }
    else:
        return {
            "nome": "Obesidade grau III",
            "cor": "vermelho",
            "nivel": 6
        }


def analisar_riscos(imc, idade, objetivo):
    analise = []

    if imc < 18.5:
        analise.append(
            "Um IMC abaixo de 18,5 pode estar associado a menor reserva energética, "
            "fadiga, queda de imunidade e perda de massa muscular."
        )
        analise.append(
            "O foco deve ser aumentar a ingestão calórica de forma saudável, priorizando "
            "proteínas, carboidratos complexos, gorduras boas e acompanhamento profissional."
        )

    elif imc < 25:
        analise.append(
            "Seu IMC está na faixa considerada saudável para a maioria dos adultos."
        )
        analise.append(
            "Manter uma rotina ativa, dormir bem e ter uma alimentação equilibrada ajuda a "
            "preservar a saúde cardiovascular e a composição corporal."
        )

    elif imc < 30:
        analise.append(
            "O sobrepeso pode aumentar gradualmente a carga sobre articulações e estar "
            "associado a maior risco de pressão alta, resistência à insulina e alterações "
            "no colesterol."
        )
        analise.append(
            "Pequenas mudanças consistentes, como caminhadas regulares, redução de ultraprocessados "
            "e melhor qualidade do sono, costumam ser mais sustentáveis do que dietas extremas."
        )

    else:
        analise.append(
            "IMC a partir de 30 está associado a maior risco cardiometabólico, incluindo "
            "hipertensão, diabetes tipo 2, apneia do sono e problemas articulares."
        )
        analise.append(
            "Neste caso, o ideal é buscar acompanhamento de um médico e, se possível, de um "
            "nutricionista e educador físico antes de iniciar treinos mais intensos."
        )

    if idade >= 45:
        analise.append(
            "A partir dos 45 anos, vale dar atenção extra à saúde cardiovascular, força muscular, "
            "mobilidade e densidade óssea."
        )

    if objetivo == "perder_peso":
        analise.append(
            "Para perda de peso, priorize um déficit calórico moderado, alimentos mais nutritivos "
            "e exercícios que você consiga manter por semanas, não apenas por alguns dias."
        )
    elif objetivo == "ganhar_massa":
        analise.append(
            "Para ganho de massa, combine treino de força progressivo com ingestão adequada de "
            "proteínas, carboidratos e calorias suficientes."
        )
    elif objetivo == "saude":
        analise.append(
            "Para saúde geral, o objetivo mais importante é criar constância: movimente-se regularmente, "
            "fortaleça o corpo e evite longos períodos sentado."
        )

    return analise


def sugerir_exercicios(imc, nivel, objetivo):
    if imc < 18.5:
        return [
            {
                "titulo": "Treino de força básico",
                "descricao": "Agachamento assistido, flexão de braço no joelho, remada com elástico e elevação de panturrilha.",
                "frequencia": "2 a 3 vezes por semana"
            },
            {
                "titulo": "Caminhada leve",
                "descricao": "20 a 30 minutos em ritmo confortável, sem exagerar no gasto calórico.",
                "frequencia": "3 a 5 vezes por semana"
            },
            {
                "titulo": "Mobilidade",
                "descricao": "Alongamentos suaves para quadril, ombros, coluna e posterior de coxa.",
                "frequencia": "Diariamente ou após os treinos"
            }
        ]

    if imc < 25:
        return [
            {
                "titulo": "Treino funcional",
                "descricao": "Agachamento, prancha, afundo, remada e elevações, adaptando a intensidade ao seu nível.",
                "frequencia": "2 a 3 vezes por semana"
            },
            {
                "titulo": "Cardio moderado",
                "descricao": "Caminhada rápida, bicicleta, natação ou corrida leve.",
                "frequencia": "150 minutos por semana"
            },
            {
                "titulo": "Mobilidade e core",
                "descricao": "Prancha, ponte de glúteos, alongamento dinâmico e exercícios de equilíbrio.",
                "frequencia": "2 a 3 vezes por semana"
            }
        ]

    if objetivo == "ganhar_massa":
        return [
            {
                "titulo": "Musculação para iniciantes",
                "descricao": "Agachamento, leg press, puxada, remada, desenvolvimento e rosca direta.",
                "frequencia": "3 vezes por semana"
            },
            {
                "titulo": "Caminhada leve",
                "descricao": "Caminhadas curtas ajudam na recuperação sem comprometer o ganho de massa.",
                "frequencia": "2 a 3 vezes por semana"
            },
            {
                "titulo": "Mobilidade",
                "descricao": "Alongamento e mobilidade de quadril, tornozelo e ombros antes e depois do treino.",
                "frequencia": "Diariamente"
            }
        ]

    return [
        {
            "titulo": "Caminhada progressiva",
            "descricao": "Comece com 20 a 30 minutos em ritmo confortável e aumente gradualmente o tempo.",
            "frequencia": "5 vezes por semana"
        },
        {
            "titulo": "Treino de força adaptado",
            "descricao": "Agachamento na cadeira, remada com elástico, elevação de panturrilha e exercícios de core.",
            "frequencia": "2 a 3 vezes por semana"
        },
        {
            "titulo": "Atividades de baixo impacto",
            "descricao": "Bicicleta, natação, hidroginástica ou elíptico reduzem o impacto nas articulações.",
            "frequencia": "2 a 3 vezes por semana"
        }
    ]


def gerar_recomendacao_ia(imc, idade, objetivo):
    classificacao = classificar_imc(imc)
    riscos = analisar_riscos(imc, idade, objetivo)
    exercicios = sugerir_exercicios(imc, classificacao["nivel"], objetivo)

    if classificacao["nome"] == "Peso saudável":
        titulo = "Seu IMC está em uma faixa saudável"
    elif classificacao["nome"] == "Abaixo do peso":
        titulo = "Seu IMC indica necessidade de ganho de peso saudável"
    elif classificacao["nome"] == "Sobrepeso":
        titulo = "Seu IMC indica sobrepeso"
    else:
        titulo = "Seu IMC indica obesidade"

    return {
        "titulo": titulo,
        "classificacao": classificacao,
        "riscos": riscos,
        "exercicios": exercicios
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/calcular", methods=["POST"])
def api_calcular():
    dados = request.get_json(silent=True) or {}

    try:
        peso = float(str(dados.get("peso", "")).replace(",", "."))
        altura = float(str(dados.get("altura", "")).replace(",", "."))
        idade = int(dados.get("idade") or 0)
        objetivo = dados.get("objetivo", "saude")
    except (ValueError, TypeError):
        return jsonify({"erro": "Informe peso, altura e idade válidos."}), 400

    if peso <= 0 or altura <= 0:
        return jsonify({"erro": "Peso e altura devem ser maiores que zero."}), 400

    if altura > 2.5:
        return jsonify({"erro": "A altura deve ser informada em metros. Exemplo: 1.75"}), 400

    if idade < 10 or idade > 120:
        return jsonify({"erro": "Informe uma idade entre 10 e 120 anos."}), 400

    imc = calcular_imc(peso, altura)
    resultado = gerar_recomendacao_ia(imc, idade, objetivo)

    return jsonify({
        "imc": round(imc, 2),
        "peso": peso,
        "altura": altura,
        "idade": idade,
        "objetivo": objetivo,
        **resultado
    })


if __name__ == "__main__":
    app.run(debug=True)