from cgitb import html
from flask import Flask, render_template, request
from sqlite3 import *
from random import *

# pseudo = nom de la personne qui fait le quizz, ce que l'on envoi a la BDD.
id_vrep = []
info_personne = {"pseudo":None, "theme":None, "score":None, "temps":None}
# Creer l'application :
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('default.html')

@application.route('/', methods=['POST'])
def recup_name():
    text = request.form['text']
    pseudo = text.upper()
    info_personne["pseudo"] = pseudo
    interact_bdd("""INSERT INTO Personne(pseudo) VALUES(?)""", pseudo)
    return questionnaire()

@application.route('/question1')
def question1():
    info_personne["theme"] = "Film"
    info_personne["id_theme"] = 1
    return question(1)

@application.route('/question2')
def question2():
    info_personne["theme"] = "Série"
    info_personne["id_theme"] = 2
    return question(2)

@application.route('/question3')
def question3():
    info_personne["theme"] = "Géographie"
    info_personne["id_theme"] = 3
    return question(3)

@application.route('/question')
def question(id):
    vals = [(ordre_random(1+i+20*(id-1)),f'Image_Questionnaire/{1+i+20*(id-1)}.png', recup_db(f"SELECT enonce FROM question Where id ={1+i+20*(id-1)}"), i+1) for i in range(21)]
    return render_template('question.html', nom=info_personne["theme"], reponse=vals)

@application.route('/questionnaire')
def questionnaire():
    return render_template('questionnaires.html')

@application.route('/question1', methods=['POST'])
def check_rep1():
    valide = 0
    for i in range(0, 20):
        rep = request.form[f'{i+1}']
        if rep == str(id_vrep[i]):
            valide += 1

    return fin()

@application.route('/question2', methods=['POST'])
def check_rep2():
    valide = 0
    for i in range(0, 20):
        rep = request.form[f'{i+1}']
        if rep == str(id_vrep[i]):
            valide += 1

    return fin()
@application.route('/question3', methods=['POST'])
def check_rep3():
    valide = 0
    for i in range(0, 20):
        rep = request.form[f'{i+1}']
        if rep == str(id_vrep[i]):
            valide += 1

    return fin()

@application.route('/fin', methods=['POST'])
def fin():
    return render_template('fin.html', pseudo=info_personne["pseudo"])


@application.route('/test')
def test():
    return render_template('test.html', img_id=f'Image_Questionnaire/{randint(1,60)}.png')

def ordre_random(idq: int):
    sqliteConnection = connect('documents/siteweb.db')
    cursor = sqliteConnection.cursor()
    req = randompos()
    cursor.execute(req,(idq,))
    val = cursor.fetchone()
    sqliteConnection.commit()
    cursor.close()
    return val

def randompos():
    req1 = """SELECT bonne, fausse1, fausse2, fausse3 FROM Question WHERE id = (?);"""
    req2 = """SELECT fausse1, bonne, fausse2, fausse3 FROM Question WHERE id = (?);"""
    req3 = """SELECT fausse1, fausse2, bonne, fausse3 FROM Question WHERE id = (?);"""
    req4 = """SELECT fausse1, fausse2, fausse3, bonne FROM Question WHERE id = (?);"""
    reqn = [req1, req2, req3, req4]
    idb = randint(0,3)
    id_vrep.append(idb)
    req = reqn[idb]
    return (req)

def interact_bdd(request, val):
    sqliteConnection = connect('documents/siteweb.db')
    cursor = sqliteConnection.cursor()
    sqliteConnection.commit()
    cursor.close()

def recup_db(req):
    sqliteConnection = connect('documents/siteweb.db')
    cursor = sqliteConnection.cursor()
    result = cursor.execute(req)
    val = cursor.fetchone()
    sqliteConnection.commit()
    cursor.close()
    return val

def add_score(personne, theme, score, temps):
    a = recup_db(f"""SELECT score, temps FROM Bilan Where personne = {personne} and theme = {theme}""")
    if a == None or a[0] <= score:
        if a == None or a[1] > temps:
            val = (personne, theme, score, temps)
            recup_db(f"""DELETE FROM Bilan WHERE personne = {personne};""")
            interact_bdd(f"""INSERT INTO Bilan VALUES (?,?,?,?);""", val)
    else:
        return 1


def leaderboard(theme,cb=5): #personne, theme, score, temps
    top = []
    for i in range(cb):
        next = recup_db(f"""SELECT * FROM (SELECT * FROM Bilan WHERE theme = {theme} ORDER BY temps ASC) ORDER BY score DESC LIMIT {i},1""")
        top.append(next)
    for j in range(len(top)):
        reste = top[j][3]
        minu = 0
        s = 0
        ms = 0
        while reste > 0:
            if reste > 60000:
                reste = reste - 60000
                minu = minu + 1
            elif reste > 1000:
                reste = reste - 1000
                s = s + 1
            else:
                ms = reste
                reste = 0
        top[j] = (top[j][0],top[j][1],top[j][2], str(minu) + "min, " + str(s) + "s, " +str(ms) + "ms" )
    return top






if __name__ == '__main__':
    application.run(debug=True)










