from cgitb import html
from flask import Flask, render_template, request
from sqlite3 import *
from random import *

# pseudo = nom de la personne qui fait le quizz, ce que l'on envoi a la BDD.
id_vrep = []
info_personne = {"pseudo":None, "id":None, "theme":None, "id_theme":None, "score":None, "temps":None}
# Creer l'application :
application = Flask(__name__)

## Affiche la page du début

@application.route('/')
def index():
    return render_template('connexion.html')

## Permet la récupération du speudo entré par l'utilisateur

@application.route('/', methods=['POST'])
def recup_name():
    text = request.form['text']
    info_personne["pseudo"] = str(text)
    add_personne(info_personne["pseudo"])
    return questionnaire()

## Informe sur quel questionnaire est l'utilisateur

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

## Affiche le questionnaire

@application.route('/question')
def question(id):
    vals = [(ordre_random(1+i+20*(id-1)),f'Image_Questionnaire/{1+i+20*(id-1)}.png', recup_db(f"SELECT enonce FROM question Where id ={1+i+20*(id-1)}"), i+1) for i in range(21)]
    return render_template('question.html', nom=info_personne["theme"], reponse=vals)

## Affiche la liste des questionnaires avec les leaderboards

@application.route('/questionnaire')
def questionnaire():
    lead1 = leaderboard(1)
    lead2 = leaderboard(2)
    lead3 = leaderboard(3)
    return render_template('questionnaires.html', val1=lead1, val2=lead2, val3=lead3)


## Permet de compter le nombre de bonne réponse pour chaque thèmes


@application.route('/question1', methods=['POST'])
def check_rep1():
    valide = 0
    info_personne["temps"] = request.form['temps']
    for i in range(0, 20):
        rep = request.form[f'{i+1}']
        if rep == str(id_vrep[i]):
            valide += 1
    info_personne["score"] = valide
    add_score(info_personne["id"], info_personne["id_theme"], info_personne["score"], info_personne["temps"])
    return questionnaire()


@application.route('/question2', methods=['POST'])
def check_rep2():
    valide = 0
    info_personne["temps"] = request.form['temps']
    for i in range(0, 20):
        rep = request.form[f'{i+1}']
        if rep == str(id_vrep[i]):
            valide += 1
    info_personne["score"] = valide
    add_score(info_personne["id"], info_personne["id_theme"], info_personne["score"], info_personne["temps"])
    return questionnaire()


@application.route('/question3', methods=['POST'])
def check_rep3():
    valide = 0
    info_personne["temps"] = request.form['temps']
    for i in range(0, 20):
        rep = request.form[f'{i+1}']
        if rep == str(id_vrep[i]):
            valide += 1
    info_personne["score"] = valide
    add_score(info_personne["id"], info_personne["id_theme"], info_personne["score"], info_personne["temps"])
    return questionnaire()

## Fonction utile

def ordre_random(idq: int): # Permet de renvoyer le tableau des bonnes réponses
    sqliteConnection = connect('documents/siteweb.db')
    cursor = sqliteConnection.cursor()
    req = randompos()
    cursor.execute(req,(idq,))
    val = cursor.fetchone()
    sqliteConnection.commit()
    cursor.close()
    return val


def randompos(): # Permet de faire en sorte que les réponses soit aléatoire
    req1 = """SELECT bonne, fausse1, fausse2, fausse3 FROM Question WHERE id = (?);"""
    req2 = """SELECT fausse1, bonne, fausse2, fausse3 FROM Question WHERE id = (?);"""
    req3 = """SELECT fausse1, fausse2, bonne, fausse3 FROM Question WHERE id = (?);"""
    req4 = """SELECT fausse1, fausse2, fausse3, bonne FROM Question WHERE id = (?);"""
    reqn = [req1, req2, req3, req4]
    idb = randint(0,3)
    id_vrep.append(idb+1)
    req = reqn[idb]
    return (req)


def interact_bdd(request, val): # fonction pour modifier la base de donnée
    sqliteConnection = connect('documents/siteweb.db')
    cursor = sqliteConnection.cursor()
    cursor.execute(request, val)
    sqliteConnection.commit()
    cursor.close()


def recup_db(req): # fonction pour récuperer une information depuis la base de donnée
    sqliteConnection = connect('documents/siteweb.db')
    cursor = sqliteConnection.cursor()
    cursor.execute(req)
    val = cursor.fetchall()
    sqliteConnection.commit()
    cursor.close()
    return val


def add_score(personne, theme, score, temps): #Ajoute les valeurs dans la base de donnée selon 4 variables
    a = recup_db("""SELECT personne, theme From Bilan""")
    val = (personne, theme, score, temps)
    present = False
    for i in a:
        if (personne, theme) == i:
            present = True
    if present == False:
        interact_bdd("""INSERT INTO Bilan VALUES (?,?,?,?);""", val)
        return 1
    b = recup_db(f"""SELECT score, temps FROM Bilan WHERE personne={personne} and theme={theme}""")
    if (personne, theme) in a:
        if b[0][0] <= score:
            if b[0][0] < score or (b[0][0] == score and b[1][0] > temps):
                recup_db(f"""DELETE FROM Bilan WHERE personne = {personne};""")
                interact_bdd("""INSERT INTO Bilan(personne,theme,score,temps) VALUES (?,?,?,?);""", val)
    else:
        interact_bdd("""INSERT INTO Bilan VALUES (?,?,?,?);""", val)


def add_personne(personne): #Ajoute un utilisateur dans la base de donnée
    present = False
    a = recup_db("""SELECT id, pseudo FROM Personne """)
    for i in a:
        if personne in i:
            info_personne["id"] = i[0]
            present = True
    if present == False:
        info_personne["id"] = len(a)+1
        interact_bdd("""Insert into Personne(id, pseudo) Values(?, ?)""", (len(a)+1, personne))


def leaderboard(theme): #Récuperer le tableau pour faire le leaderboard
    cb = 5
    info = []
    suivant = recup_db(f"""SELECT P.pseudo, B.score, B.temps FROM Bilan as B inner Join Personne as P on P.id = B.personne WHERE theme = {theme} ORDER BY score DESC LIMIT 5""")
    for j in range(5):
        ms = suivant[j][2]
        s = (ms // 1000)%60
        m = (ms // 1000) // 60
        ms %= 1000
        temps = str(m) + "min, " + str(s) + "s, " +str(ms) + "ms"
        info.append((suivant[j][0],str(suivant[j][1])+"/20", temps))
    return info





if __name__ == '__main__':
    application.run(debug=True)