from cgitb import html
from flask import Flask, render_template, request
from sqlite3 import *
from random import *

# pseudo = nom de la personne qui fait le quizz, ce que l'on envoi a la BDD.
id_vrep = []
info_personne = []
# Creer l'application :
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('default.html')

@application.route('/', methods=['POST'])
def recup_name():
    text = request.form['text']
    pseudo = text.upper()
    interact_bdd("""INSERT INTO Personne(pseudo) VALUES(?)""", pseudo)
    return questionnaire()

@application.route('/question1')
def question1():
    return question(1)

@application.route('/question2')
def question2():
    return question(2)

@application.route('/question3')
def question3():
    return question(3)

@application.route('/question')
def question(id):
    val1 = ordre_random(1 + 20*(id-1))
    val2 = ordre_random(2 + 20*(id-1))
    val3 = ordre_random(3 + 20*(id-1))
    val4 = ordre_random(4 + 20*(id-1))
    val5 = ordre_random(5 + 20*(id-1))
    val6 = ordre_random(6 + 20*(id-1))
    val7 = ordre_random(7 + 20*(id-1))
    val8 = ordre_random(8 + 20*(id-1))
    val9 = ordre_random(9 + 20*(id-1))
    val10 = ordre_random(10 + 20*(id-1))
    val11 = ordre_random(11 + 20*(id-1))
    val12 = ordre_random(12 + 20*(id-1))
    val13 = ordre_random(13 + 20*(id-1))
    val14 = ordre_random(14 + 20*(id-1))
    val15 = ordre_random(15 + 20*(id-1))
    val16 = ordre_random(16 + 20*(id-1))
    val17 = ordre_random(17 + 20*(id-1))
    val18 = ordre_random(18 + 20*(id-1))
    val19 = ordre_random(19 + 20*(id-1))
    val20 = ordre_random(20 + 20*(id-1))
    valque1 = [interact_bdd("""SELECT enonce FROM Question WHERE id = (?);""", i + 20*(id-1)) for i in range(1, 21)]

    return render_template(f'question{id}.html',
rep11=val1[0], rep12=val1[1], rep13=val1[2], rep14=val1[3], rep21=val2[0], rep22=val2[1], rep23=val2[2], rep24=val2[3], rep31=val3[0], rep32=val3[1], rep33=val3[2], rep34=val3[3], rep41=val4[0], rep42=val4[1], rep43=val4[2], rep44=val4[3], rep51=val5[0], rep52=val5[1], rep53=val5[2], rep54=val5[3], rep61=val6[0], rep62=val6[1], rep63=val6[2], rep64=val6[3], rep71=val7[0], rep72=val7[1], rep73=val7[2], rep74=val7[3], rep81=val8[0], rep82=val8[1], rep83=val8[2], rep84=val8[3], rep91=val9[0], rep92=val9[1], rep93=val9[2], rep94=val9[3], rep101=val10[0], rep102=val10[1], rep103=val10[2], rep104=val10[3], rep111=val11[0], rep112=val11[1], rep113=val11[2], rep114=val11[3], rep121=val12[0], rep122=val12[1], rep123=val12[2], rep124=val12[3], rep131=val13[0], rep132=val13[1], rep133=val13[2], rep134=val13[3], rep141=val14[0], rep142=val14[1], rep143=val14[2], rep144=val14[3], rep151=val15[0], rep152=val15[1], rep153=val15[2], rep154=val15[3], rep161=val16[0], rep162=val16[1], rep163=val16[2], rep164=val16[3], rep171=val17[0], rep172=val17[1], rep173=val17[2], rep174=val17[3], rep181=val18[0], rep182=val18[1], rep183=val18[2], rep184=val18[3], rep191=val19[0], rep192=val19[1], rep193=val19[2], rep194=val19[3], rep201=val20[0], rep202=val20[1], rep203=val20[2], rep204=val20[3], que1=valque1[0],que2=valque1[1],que3=valque1[2],que4=valque1[3],que5=valque1[4],que6=valque1[5],que7=valque1[6],que8=valque1[7],que9=valque1[8],que10=valque1[9],que11=valque1[10],que12=valque1[11],que13=valque1[12],que14=valque1[13],que15=valque1[14],que16=valque1[15],que17=valque1[16],que18=valque1[17],que19=valque1[18],que20=valque1[19])
@application.route('/questionnaire')
def questionnaire():
    return render_template('questionnaires.html')

@application.route('/question1', methods=['POST'])
def check_rep1():
    valide = 0
    for i in range(0, 20):
        rep = request.form[f'repQ{i+1}']
        if rep == str(id_vrep[i]):
            valide += 1
    return questionnaire()

@application.route('/question2', methods=['POST'])
def check_rep2():
    valide = 0
    for i in range(0, 20):
        rep = request.form[f'repQ{i+1}']
        if rep == str(id_vrep[i]):
            valide += 1
    return questionnaire()

@application.route('/question3', methods=['POST'])
def check_rep3():
    valide = 0
    for i in range(0, 20):
        rep = request.form[f'repQ{i+1}']
        if rep == str(id_vrep[i]):
            valide += 1
    return questionnaire()



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
    cursor.execute(request,(val,))
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
        top[j] = (top[j][0],top[j][1],top[j][2], "Min: " + str(minu) + ", S: " + str(s) + ", Ms: " +str(ms) )
    return top










if __name__ == '__main__':
    application.run(debug=True)









