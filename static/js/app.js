const form = document.getElementById("imc-form");
const btn = document.getElementById("btn-calcular");
const erro = document.getElementById("erro");
const resultadoCard = document.getElementById("resultado-card");
const imcValor = document.getElementById("imc-valor");
const badge = document.getElementById("classificacao-badge");
const barra = document.getElementById("barra-preenchimento");
const iaTitulo = document.getElementById("ia-titulo");
const riscos = document.getElementById("riscos");
const exercicios = document.getElementById("exercicios");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  erro.classList.add("hidden");
  btn.disabled = true;
  btn.textContent = "Analisando...";

  const dados = {
    peso: document.getElementById("peso").value,
    altura: document.getElementById("altura").value,
    idade: document.getElementById("idade").value,
    objetivo: document.getElementById("objetivo").value
  };

  try {
    const resposta = await fetch("/api/calcular", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados)
    });

    const json = await resposta.json();

    if (!resposta.ok) {
      mostrarErro(json.erro || "Não foi possível calcular o IMC.");
      return;
    }

    exibirResultado(json);
  } catch (e) {
    mostrarErro("Erro de conexão. Tente novamente.");
  } finally {
    btn.disabled = false;
    btn.textContent = "Analisar meu IMC";
  }
});

function mostrarErro(mensagem) {
  erro.textContent = mensagem;
  erro.classList.remove("hidden");
}

function exibirResultado(dados) {
  resultadoCard.classList.remove("hidden");

  imcValor.textContent = dados.imc.toFixed(2).replace(".", ",");
  badge.textContent = dados.classificacao.nome;
  badge.className = `badge ${dados.classificacao.cor}`;

  const largura = Math.min(Math.max(((dados.imc - 12) / 28) * 100, 5), 100);
  barra.style.width = `${largura}%`;

  iaTitulo.textContent = dados.titulo;

  riscos.innerHTML = "";
  dados.riscos.forEach(texto => {
    const item = document.createElement("li");
    item.textContent = texto;
    riscos.appendChild(item);
  });

  exercicios.innerHTML = "";
  dados.exercicios.forEach(item => {
    const card = document.createElement("article");
    card.className = "exercicio";
    card.innerHTML = `
      <strong>${item.titulo}</strong>
      <p>${item.descricao}</p>
      <span class="frequencia">${item.frequencia}</span>
    `;
    exercicios.appendChild(card);
  });

  resultadoCard.scrollIntoView({ behavior: "smooth", block: "start" });
}