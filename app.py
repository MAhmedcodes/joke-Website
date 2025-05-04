from flask import Flask, render_template, request, send_from_directory
import requests
import pyjokes


app = Flask(__name__)

def get_joke(joke_type):
    if joke_type == "programming":
        return pyjokes.get_joke(category='neutral')
    elif joke_type == "general":
        url = "https://v2.jokeapi.dev/joke/Miscellaneous,Pun,Spooky,Christmas?type=single&blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
        response = requests.get(url).json()
        return response.get("joke", "No kid-friendly joke available.")
    elif joke_type == "adult":
        url = "https://v2.jokeapi.dev/joke/Any?type=single&contains=sex"
    elif joke_type == "dad":
        url = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers).json()
        return response.get("joke", "No dad joke found right now.")
    else:
        return "Invalid joke type."

    response = requests.get(url).json()
    return response.get("joke", "No joke found at the moment.")

@app.route("/", methods=["GET", "POST"])
def index():
    joke = ""
    if request.method == "POST":
        joke_type = request.form.get("joke_type")
        joke = get_joke(joke_type)
    return render_template("index.html", joke=joke)

if __name__ == "__main__":
    app.run(debug=True)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
