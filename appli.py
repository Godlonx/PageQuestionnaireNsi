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
    val2 = ordre_random(2)
    val3 = ordre_random(3)
    val4 = ordre_random(4)
    val5 = ordre_random(5)
    val6 = ordre_random(6)
    val7 = ordre_random(7)
    val8 = ordre_random(8)
    val9 = ordre_random(9)
    val10 = ordre_random(10)
    val11 = ordre_random(11)
    val12 = ordre_random(12)
    val13 = ordre_random(13)
    val14 = ordre_random(14)
    val15 = ordre_random(15)
    val16 = ordre_random(16)
    val17 = ordre_random(17)
    val18 = ordre_random(18)
    val19 = ordre_random(19)
    val20 = ordre_random(20)
    return render_template('question.html', nom='Cacao', rep11=val1[0], rep12=val1[1], rep13=val1[2], rep14=val1[3], rep21=val2[0], rep22=val2[1], rep23=val2[2], rep24=val2[3], rep31=val3[0], rep32=val3[1], rep33=val3[2], rep34=val3[3], rep41=val4[0], rep42=val4[1], rep43=val4[2], rep44=val4[3], rep51=val5[0], rep52=val5[1], rep53=val5[2], rep54=val5[3], rep61=val6[0], rep62=val6[1], rep63=val6[2], rep64=val6[3], rep71=val7[0], rep72=val7[1], rep73=val7[2], rep74=val7[3], rep81=val8[0], rep82=val8[1], rep83=val8[2], rep84=val8[3], rep91=val9[0], rep49=val9[1], rep93=val9[2], rep94=val9[3], rep101=val10[0], rep102=val10[1], rep103=val10[2], rep104=val10[3], rep111=val11[0], rep112=val11[1], rep113=val11[2], rep114=val11[3], rep121=val12[0], rep122=val12[1], rep123=val12[2], rep124=val12[3], rep131=val13[0], rep132=val13[1], rep133=val13[2], rep134=val13[3], rep141=val14[0], rep142=val14[1], rep143=val14[2], rep144=val14[3], rep151=val15[0], rep152=val15[1], rep153=val15[2], rep154=val5[3], rep161=val16[0], rep162=val16[1], rep163=val16[2], rep164=val16[3], rep171=val17[0], rep172=val17[1], rep173=val17[2], rep174=val17[3], rep181=val18[0], rep182=val18[1], rep183=val18[2], rep184=val8[3], rep191=val19[0], rep192=val19[1], rep193=val19[2], rep194=val19[3], rep201=val20[0], rep202=val20[1], rep203=val20[2], rep204=val20[3])
@application.route('/questionnaire')
def questionnaire():
    return render_template('questionnaires.html')


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
    req = reqn[idb]

    return (req)

if __name__ == '__main__':
    application.run(debug=True)






