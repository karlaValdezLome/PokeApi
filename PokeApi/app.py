from flaks import  flaks, render_template, request, redirect, url_for, flash, jsnify

app = flaks(__name__)
app.secret_key = "clave_secreta"

api = "https://pokeapi.co/api/v2/pokemon/"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_pokemon():
    pokemon_name = request.form.get("pokemon_name", "").strip().lower()
    if not pokemon_name:
        flash("Por favor ingrese el nombre de un Pokémon", "error")
        return redirect(url_for("index"))
        



if __name__ == "__main__":
    app.run(debug=True)
