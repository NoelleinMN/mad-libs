"""A madlib game that compliments its users."""

from random import choice

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


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game',)
def show_madlib_form():
    """Goodbye or game"""
    # if value from /hello = no
        # return GOODBYE (and maybe change your mind?)
    player_choice = request.args.get("choice")
        
    if player_choice == "No":
    
        return render_template("goodbye.html")
    # if value from /hello = yes
        # new form asks for madlib entries 
        # text boxes with nouns, verbs, etc.
        # submit to results madlibs page
    else: 
        player_choice == "Yes"

        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Show madlib"""
    # return results of madlib game
    # maybe add a play again option
    madlib_person = request.args.get("person")
    madlib_noun = request.args.get("noun")
    madlib_color = request.args.get("color")
    madlib_adjective = request.args.get("adjective")

    return render_template("madlib.html", person=madlib_person, noun=madlib_noun, color=madlib_color, adjective=madlib_adjective)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
