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



from sqlite3 import *
from random import *


def ordre_random(idq):
    sqliteConnection = connect('siteweb.db')
    cursor = sqliteConnection.cursor()
    req = randompos()
    val = cursor.execute(req[0],idq)

    sqliteConnection.commit()
    cursor.close()

    return (val, req[1])


def randompos():
    req1 = """SELECT bonne, fausse1, fausse2, fausse3 FROM Question WHERE id = ?;"""
    req2 = """SELECT fausse1, bonne, fausse2, fausse3 FROM Question WHERE id = ?;"""
    req3 = """SELECT fausse1, fausse2, bonne, fausse3 FROM Question WHERE id = ?;"""
    req4 = """SELECT fausse1, fausse2, fausse3, bonne FROM Question WHERE id = ?;"""
    reqn = [req1, req2, req3, req4]
    idb = randint(0,3)
    req = reqn[idb]

    return (req, idb)