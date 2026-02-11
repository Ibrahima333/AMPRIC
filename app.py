from flask import Flask ,render_template , request,url_for,redirect,flash
import pymysql
from dotenv import load_dotenv
import os



# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)
#connection a mysql
def mysql():
    return pymysql.connect(
        host= os.getenv("DB_HOST"),
        user= os.getenv("DB_USER"),
        password= os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )
#verification_doublons numero de telephone 
def check_duplicate_number(tel) :
    connexion= mysql()
    cursor = connexion.cursor()
    query = """ select telephone from utilisateurs where telephone = %s"""
    cursor.execute(query,(tel))
    resultat = cursor.fetchone() 
    cursor.close()
    connexion.close()
    if resultat :
        return True
    else :
        return False
    
def check_duplicate_email(email) :
    connexion= mysql()
    cursor = connexion.cursor()
    query = """select email from utilisateurs where email = %s"""
    cursor.execute(query,(email))
    resultat = cursor.fetchone() 
    cursor.close()
    connexion.close()
    if resultat :
        return True
    else :
        return False
    
    
@app.route('/',methods=["POST","GET"])
def home():
    if request.method =='POST' :
        nom = request.form.get("nom")
        prenom = request.form.get("prenom")
        email = request.form.get("email")
        comment =request.form.get("message")
        tel = request.form.get("tel")
        
        if check_duplicate_number(tel) :
            erreur = "Ce numéro est déjà utilisé. Veuillez saisir un autre."
            return render_template("index.html", erreur=erreur)
        
        if check_duplicate_email(email) :
            erreur = "Cet email est déjà utilisé. Veuillez saisir un autre."
            return render_template("index.html", erreur=erreur)
            
        conexion = mysql()
        cursor = conexion.cursor()
        query = """insert into utilisateurs (nom,prenom,telephone,email,comment) values(%s,%s,%s,%s,%s)"""
        cursor.execute(query,(nom,prenom,tel,email,comment))
        conexion.commit()
        cursor.close()
        conexion.close()
        flash("Vos informations ont été enregistrées avec succès. Notre équipe vous contactera dans les plus brefs délais." , "success")
        return redirect(url_for("home"))
    
    else:
        return render_template("index.html")
    
# route pour la page d'objectifs
@app.route('/objectifs')
def objectifs():
    return render_template("objectifs.html")

if __name__ == "__main__":
    app.run(debug=True)