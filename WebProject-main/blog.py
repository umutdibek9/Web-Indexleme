from flask import Flask, render_template,request,flash
import geturl as g_u

webapp = Flask(__name__)

@webapp.route("/")
def index():
    return render_template("index.html")

@webapp.route("/frekans")
def frekans():
    
    return render_template("frekans.html",ctrl=False)



@webapp.route("/frekans",methods=['POST'])
def getvalue():
    url = request.form['text-url']
    

    if (len(url) == 0):
        flash("Hatalı giriş yaptınız.","danger")
        return render_template("frekans.html",ctrl=False)

    dict_d = g_u.wordfreq(url)   
    return render_template("frekans.html",ctrl=True,dict_d= dict_d)


@webapp.route("/anahtar")
def anahtar():
    return render_template("anahtar.html", ctrl=False)


@webapp.route('/anahtar', methods=['POST'])
def getValuekey():
    url1 = request.form['url1']
    url2 = request.form['url2']

    if (len(url1) == 0 or len(url2) == 0):
        flash("Hatalı giriş yaptınız.", "danger")
        return render_template("anahtar.html", ctrl=False)

    dict1 = g_u.key_word(g_u.wordfreq(url1), url1)
    dict2 = g_u.key_word(g_u.wordfreq(url2), url2)


    return render_template("anahtar.html", ctrl=True, dict1=dict1, dict2=dict2)


@webapp.route("/benzerlik")
def like():
    return render_template("benzerlik.html", ctrl=False)


@webapp.route('/benzerlik', methods=['POST'])
def getValuekeyLike():
    url1 = request.form['url1']
    url2 = request.form['url2']

    if (len(url1) == 0 or len(url2) == 0):
        flash("Hatalı giriş yaptınız.", "danger")
        return render_template("benzerlilk.html", ctrl=False)

    dict1 = g_u.key_word(g_u.wordfreq(url1), url1)
    dict2 = g_u.key_word(g_u.wordfreq(url2), url2)

    rate = round(g_u.likeRate(dict1, dict2), 2)

    return render_template("benzerlik.html", ctrl=True, dict1=dict1, dict2=dict2,rate=rate)

@webapp.route("/indexleme")
def indeks():
    return render_template("indexleme.html",ctrl=False)

@webapp.route("/indexleme",methods=['POST'])
def findurl():
    url1 = request.form['url1']
    url2 = request.form['url2']

    if (len(url1) == 0 or len(url2) == 0):
        flash("Hatalı giriş yaptınız.","danger")
        return render_template("indexleme.html",ctrl=False)
  


    return render_template("indexleme.html",ctrl=True)
    

@webapp.route("/semantik")
def analiz():
    return render_template("semantik.html")                     
    

if __name__=="__main__":
    webapp.run(debug=True)#web sunucusu çalıştırma


