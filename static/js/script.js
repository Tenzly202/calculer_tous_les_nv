async function loadFields() {
    const classe = document.getElementById("classe").value;
    const form = document.getElementById("notesForm");
    form.innerHTML = "";

    if (!classe) return;

    const response = await fetch(`/coeffs/${classe}`);
    const data = await response.json();

    for (const [matiere, coef] of Object.entries(data)) {
        form.innerHTML += `
            <label>${matiere} (coef ${coef})</label>
            <input type="number" step="0.01" min="0" max="20" name="${matiere}">
        `;
    }

    form.innerHTML += `<button type="submit">Calculer</button>`;
}

async function calculer() {
    const classe = document.getElementById("classe").value;
    const form = document.getElementById("notesForm");
    const formData = new FormData(form);

    const response = await fetch(`/calcul/${classe}`, {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    const box = document.getElementById("resultat");
    box.style.display = "block";
    box.innerHTML = `
        <h3>Moyenne : ${data.moyenne}</h3>
    `;
}
