# Medidor de IMC

Aplicação web simples feita em **Python + Flask** para calcular o **Índice de Massa Corporal (IMC)** a partir do peso e da altura informados pelo usuário.

🔗 **Acesse o projeto online:** [https://projectimc.vercel.app/](https://projectimc.vercel.app/)

## Sobre o projeto

O usuário informa o peso em quilogramas e a altura em metros. A aplicação calcula o IMC e exibe a classificação correspondente.

A fórmula utilizada é:

[
IMC = \frac{peso}{altura^2}
]

## Funcionalidades

- Cálculo automático do IMC
- Classificação por faixa de IMC
- Aceita vírgula ou ponto como separador decimal
- Validação básica dos dados informados
- Interface responsiva para celular e computador
- Publicado na Vercel

## Classificação do IMC

| IMC | Classificação |
|---:|---|
| Menor que 18,5 | Abaixo do peso |
| 18,5 a 24,9 | Peso normal |
| 25,0 a 29,9 | Sobrepeso |
| 30,0 a 34,9 | Obesidade grau I |
| 35,0 a 39,9 | Obesidade grau II |
| 40,0 ou mais | Obesidade grau III |

## Tecnologias

- Python
- Flask
- HTML
- CSS
- Jinja2
- Vercel

## Estrutura do projeto

```text
medidor-imc/
├── app.py
├── requirements.txt
├── vercel.json
├── .gitignore
├── README.md
└── templates/
    └── index.html