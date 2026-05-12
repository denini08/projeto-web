const API = "http://localhost:8000";

function avisar_deletado() {
  alert("Tarefa deletada com sucesso!");
}

function carregar() {
  $.get(`${API}/tarefas`, function (lista) {
    var html = "";

    for (var i = 0; i < lista.length; i++) {
      var t = lista[i];
      var classe = "";

      if (t.concluida) {
        classe = "riscado";
      }

      html +=
        '<li class="list-group-item d-flex justify-content-between align-items-center">';
      html += "<div>";
      html += '<div class="' + classe + '">' + t.titulo + "</div>";
      html +=
        '<small class="text-muted ' + classe + '">' + t.descricao + "</small>";
      html += "</div>";
      html += '<div class="d-flex gap-2">';
      html +=
        '<a href="editar/index.html?id=' +
        t.id +
        '" class="btn btn-sm btn-outline-secondary">Editar</a>';
      html +=
        '<button class="btn btn-sm btn-danger btn-deletar" data-id="' +
        t.id +
        '">Deletar</button>';
      html += "</div>";
      html += "</li>";
    }

    if (html === "") {
      html = '<li class="list-group-item text-muted">Nenhuma tarefa.</li>';
    }

    $("#lista").html(html);
  });
}

$(document).on("click", ".btn-deletar", function () {
  // confirmar antes de deletar
  if (!confirm("Tem certeza que deseja deletar esta tarefa?")) {
    return;
  }
  $.ajax({
    url: `${API}/tarefas/${$(this).data("id")}`,
    method: "DELETE",
    success: function () {
      avisar_deletado();
      carregar();
    },
  });
});

carregar();
