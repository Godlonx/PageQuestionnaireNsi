from flask import Flask, render_template, request

# Creer l'application :
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('default.html')

@application.route('/question')
def question():
    return render_template('question.html', nom='Cacaobean')

@application.route('/questionnaire')
def questionnaire():
    return render_template('questionnaires.html')

if __name__ == '__main__':
    application.run(debug=True)