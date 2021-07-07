from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://rinaldomeneses:cmluYWxkb21l''@jobs.visie.com.br/rinaldomeneses'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class pessoas(db.Model):
    id_pessoa = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    rg = db.Column(db.String(100))
    cpf = db.Column(db.String(100))
    funcao = db.Column(db.String(100))
    data_admissao = db.Column(db.DateTime)
    data_nascimento = db.Column(db.DateTime)



    def __init__(self, nome, rg, cpf, funcao, data_nascimento, data_admissao):

        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.funcao = funcao
        self.data_nascimento = data_nascimento
        self.data_admissao = data_admissao





@app.route('/')
def Index():
    all_pessoas = pessoas.query.all()

    return render_template("index.html", pessoas = all_pessoas)



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        nome = request.form['nome']
        rg = request.form['rg']
        cpf = request.form['cpf']
        funcao = request.form['funcao']
        data_admissao = request.form['data_admissao']
        data_nascimento = request.form['data_nascimento']




        my_pessoas = pessoas(nome, rg, cpf,funcao, data_nascimento, data_admissao)
        db.session.add(my_pessoas)
        db.session.commit()

        flash("Perfil adicionado")

        return redirect(url_for('Index'))




@app.route('/delete/<id_pessoa>/', methods = ['GET', 'POST'])
def delete(id_pessoa):
    my_pessoas = pessoas.query.get(id_pessoa)
    db.session.delete(my_pessoas)
    db.session.commit()
    flash("Perfil deletado")

    return redirect(url_for('Index'))






if __name__ == "__main__":
    app.run(debug=True)