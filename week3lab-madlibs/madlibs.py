"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")

#With post added instead of get
@app.route('/greet', methods=['POST'])
def greet_person():
    """Greet user with compliment."""

    player = request.form.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    opt_play = request.args.get("play")

    if opt_play == 'yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    input_color = request.args.get("color")
    input_noun = request.args.get("noun")
    input_person = request.args.get("person")
    input_adjective = request.args.get("adjective")
    check_place = request.args.getlist("place") #getlist**********
    select_command = request.args.get("command")

    selected_place = sample(check_place, 1) #had to import sample from random********
    string_place = selected_place[0]

    return render_template("madlib.html",
                            color=input_color,
                            noun=input_noun,
                            person=input_person,
                            adjective=input_adjective,
                            place=string_place,
                            command=select_command)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
