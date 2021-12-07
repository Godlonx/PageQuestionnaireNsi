from flask import Flask, render_template, request

# Creer l'application :
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/question')
def question():
    return render_template('question.html', nom='Cacaobean')

if __name__ == '__main__':
    application.run(debug=True)