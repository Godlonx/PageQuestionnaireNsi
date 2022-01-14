from flask import Flask, render_template, request
from sqlite3 import *
from random import *

# Creer l'application :
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('default.html')

@application.route('/question')
def question():
    val1 = ordre_random(1)
    return render_template('question.html', nom='Cacao', rep11=val1[0], rep12=val1[1])

@application.route('/questionnaire')
def questionnaire():
    return render_template('questionnaires.html')


def ordre_random(idq: int):
    sqliteConnection = connect('documents/siteweb.db')
    cursor = sqliteConnection.cursor()
    req = randompos()
    cursor.execute(req,str(idq))
    val = cursor.fetchone()
    sqliteConnection.commit()
    cursor.close()
    return val


def randompos():
    req1 = """SELECT bonne, fausse1, fausse2, fausse3 FROM Question WHERE id = ?;"""
    req2 = """SELECT fausse1, bonne, fausse2, fausse3 FROM Question WHERE id = ?;"""
    req3 = """SELECT fausse1, fausse2, bonne, fausse3 FROM Question WHERE id = ?;"""
    req4 = """SELECT fausse1, fausse2, fausse3, bonne FROM Question WHERE id = ?;"""
    reqn = [req1, req2, req3, req4]
    idb = randint(0,3)
    req = reqn[idb]

    return (req)

if __name__ == '__main__':
    application.run(debug=True)






