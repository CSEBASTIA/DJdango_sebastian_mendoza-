document.addEventListener("DOMContentLoaded", () => {
  const lista = document.getElementById("lista-experiencias");
  const btnAgregar = document.getElementById("btn-agregar");

  if (!lista || !btnAgregar) return;

  btnAgregar.addEventListener("click", () => {
    const div = document.createElement("div");
    div.className = "experiencia";

    div.innerHTML = `
      <h3>Nueva Experiencia</h3>
      <p class="empresa">Empresa · Año</p>
      <p>Descripción de la experiencia.</p>
      <button class="btn-eliminar">Eliminar</button>
    `;

    lista.appendChild(div);
  });

  lista.addEventListener("click", (e) => {
    if (e.target.classList.contains("btn-eliminar")) {
      e.target.closest(".experiencia").remove();
    }
  });
});
