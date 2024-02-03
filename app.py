from flask import Flask , request , render_template





app = Flask(__name__)
lista_nomes = list()


#Rotas App
@app.route("/")
def index():
    nome = request.form.get("home")
    lista_nomes.append(nome)
    
    return"""
    <script>
        alert('cadastro feito com sucesso')
        window.location.href = "/";
    </script>
    """
    


@app.route("/secondPage")
def secondPage():
    
    return render_template("add.html" , lista_nomes=lista_nomes)
    




if __name__ =="__main__":
    app.run(debug=True)
