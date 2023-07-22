from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

def new_game():
    return randint(0, 5)

game_data = {
    "target_number": new_game(),
    "attempts": 0,
    "message": "Escolha um número entre 0 e 5.",
    "success": False,
    "color": "black"
}

max_attempts = 3

@app.route("/", methods=["GET", "POST"])
def game():
    global game_data

    if request.method == "POST":
        if game_data["success"]:
            return render_template("index.html", data=game_data, max_attempts=max_attempts)

        guess = request.form.get("guess")
        if guess is not None and guess.isdigit():
            guess = int(guess)
            if 0 <= guess <= 5:
                game_data["attempts"] += 1

                if guess == game_data["target_number"]:
                    game_data["message"] = f"Parabéns! Você adivinhou corretamente em {game_data['attempts']} tentativas."
                    game_data["success"] = True
                    game_data["color"] = "green"
                elif guess < game_data["target_number"]:
                    game_data["message"] = "Está longe... Tente novamente."
                    game_data["color"] = "blue"
                else:
                    game_data["message"] = "Está próximo, vá vamos lá... Tente novamente."
                    game_data["color"] = "red"
            else:
                game_data["message"] = "Por favor, escolha um número entre 0 e 5."

        if game_data["attempts"] >= max_attempts and not game_data["success"]:
            game_data["message"] = f"Você excedeu o número máximo de tentativas. O número correto era {game_data['target_number']}. Tente novamente."
            game_data["color"] = "red"
            game_data["success"] = True

    return render_template("index.html", data=game_data, max_attempts=max_attempts)

if __name__ == "__main__":
    app.run(debug=True)
