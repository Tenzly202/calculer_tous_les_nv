from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# =======================
#   COEFFICIENTS COMPLETS
# =======================

coeffs = {

    # ---------- COLLEGE ----------
    "6e": {
        "Anglais": 2,
        "Aplastique/Musique": 1,
        "EDHC": 1,
        "EPS": 1,
        "Français": 3,
        "Histoire/Géo": 2,
        "Mathématiques": 3,
        "Physique-Chimie": 2,
        "SVT": 2,
        "Conduite": 1
    },

    "5e": {
        "Anglais": 2,
        "Aplastique/Musique": 1,
        "EDHC": 1,
        "EPS": 1,
        "Français": 3,
        "Histoire/Géo": 2,
        "Mathématiques": 3,
        "Physique-Chimie": 2,
        "SVT": 2,
        "Conduite": 1
    },

    "4e": {
        "Anglais": 2,
        "Aplastique/Musique": 1,
        "EDHC": 1,
        "EPS": 1,
        "Français": 4,
        "Histoire/Géo": 2,
        "Mathématiques": 3,
        "Physique-Chimie": 2,
        "SVT": 2,
        "Conduite": 1
    },

    "3e": {
        "Anglais": 2,
        "Aplastique/Musique": 1,
        "EDHC": 1,
        "EPS": 1,
        "Français": 4,
        "Histoire/Géo": 2,
        "Mathématiques": 3,
        "Physique-Chimie": 2,
        "SVT": 2,
        "Conduite": 1
    },

    # ---------- SECONDE ----------
    "2nde_A": {
        "Anglais": 3,
        "Aplastique/Musique": 1,
        "EPS": 1,
        "Français": 4,
        "Histoire/Géo": 3,
        "ALL/ESP": 3,
        "Mathématiques": 3,
        "Physique-Chimie": 2,
        "SVT": 2,
        "Conduite": 1
    },

    "2nde_C": {
        "Anglais": 3,
        "Aplastique/Musique": 1,
        "EPS": 1,
        "Français": 3,
        "Histoire/Géo": 2,
        "ALL/ESP": 1,
        "Mathématiques": 5,
        "Physique-Chimie": 4,
        "SVT": 2,
        "Conduite": 1
    },

    # ---------- PREMIERE ----------
    "1e_A1": {
        "Anglais": 4,
        "Aplastique/Musique": 1,
        "EPS": 1,
        "Français": 4,
        "Histoire/Géo": 3,
        "ALL/ESP": 3,
        "Mathématiques": 3,
        "Philosophie": 3,
        "SVT": 1,
        "Conduite": 1
    },

    "1e_A2": {
        "Anglais": 4,
        "Aplastique/Musique": 1,
        "EPS": 1,
        "Français": 4,
        "Histoire/Géo": 3,
        "ALL/ESP": 3,
        "Mathématiques": 2,
        "Philosophie": 3,
        "SVT": 1,
        "Conduite": 1
    },

    "1e_C": {
        "Anglais": 2,
        "Aplastique/Musique": 1,
        "EPS": 1,
        "Français": 3,
        "Histoire/Géo": 2,
        "Mathématiques": 5,
        "Philosophie": 2,
        "Physique-Chimie": 5,
        "SVT": 2,
        "Conduite": 1
    },

    "1e_D": {
        "Anglais": 2,
        "Aplastique/Musique": 1,
        "EPS": 1,
        "Français": 3,
        "Histoire/Géo": 2,
        "Mathématiques": 4,
        "Philosophie": 2,
        "Physique-Chimie": 4,
        "SVT": 4,
        "Conduite": 1
    },

    # ---------- TERMINALE ----------
    "Tle_A1": {
        "Anglais": 4,
        "Aplastique/Musique": 1,
        "EPS": 1,
        "Français": 4,
        "Histoire/Géo": 3,
        "ALL/ESP": 3,
        "Mathématiques": 4,
        "Philosophie": 5,
        "SVT": 2,
        "Conduite": 1
    },

    "Tle_A2": {
        "Anglais": 4,
        "Aplastique/Musique": 1,
        "EPS": 1,
        "Français": 4,
        "Histoire/Géo": 3,
        "ALL/ESP": 3,
        "Mathématiques": 2,
        "Philosophie": 5,
        "SVT": 2,
        "Conduite": 1
    },

    "Tle_C": {
        "Anglais": 1,
        "Aplastique/Musique": 1,
        "EPS": 1,
        "Français": 3,
        "Histoire/Géo": 2,
        "Mathématiques": 5,
        "Philosophie": 2,
        "Physique-Chimie": 5,
        "SVT": 2,
        "Conduite": 1
    },

    "Tle_D": {
        "Anglais": 1,
        "Aplastique/Musique": 1,
        "EPS": 1,
        "Français": 3,
        "Histoire/Géo": 2,
        "Mathématiques": 4,
        "Philosophie": 2,
        "Physique-Chimie": 4,
        "SVT": 4,
        "Conduite": 1
    },
}

# =======================
#   ROUTES FLASK
# =======================

@app.route("/")
def index():
    return render_template("index_modern.html", classes=list(coeffs.keys()))

@app.route("/coeffs/<classe>")
def get_coeffs(classe):
    return jsonify(coeffs[classe])

@app.route("/calcul/<classe>", methods=["POST"])
def calcul(classe):
    notes = request.form
    matieres = coeffs[classe]

    total_points = 0
    total_coeffs = 0

    for matiere, coef in matieres.items():
        note = float(notes.get(matiere, 0))
        total_points += note * coef
        total_coeffs += coef

    moyenne = round(total_points / total_coeffs, 2)

    return jsonify({"moyenne": moyenne})


# =======================
#   LANCEMENT LOCAL
# =======================

if __name__ == "__main__":
    app.run(debug=True)
