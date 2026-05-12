const API = "http://localhost:8000";
const id = new URLSearchParams(window.location.search).get("id");

$.get(`${API}/tarefas/${id}`, function (t) {
  $("#titulo").val(t.titulo);
  $("#descricao").val(t.descricao);
  $("#concluida").prop("checked", t.concluida);
});

$("#form-editar").on("submit", function (e) {
  e.preventDefault();

  $.ajax({
    url: `${API}/tarefas/${id}`,
    method: "PATCH",
    contentType: "application/json",
    data: JSON.stringify({
      titulo: $("#titulo").val(),
      descricao: $("#descricao").val(),
      concluida: $("#concluida").is(":checked"),
    }),
    success() {
      window.location.href = "../index.html";
    },
  });
});
