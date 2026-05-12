const API = "http://localhost:8000";

$("#form-criar").on("submit", function (e) {
  e.preventDefault();

  if (!$("#titulo").val() || !$("#descricao").val()) {
    alert("Preencha todos os campos!");
    return;
  }

  $.ajax({
    url: `${API}/tarefas`,
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      titulo: $("#titulo").val(),
      descricao: $("#descricao").val(),
    }),
    success() {
      window.location.href = "../index.html";
    },
    error() {
      alert("Erro ao criar tarefa!");
    },
  });
});
