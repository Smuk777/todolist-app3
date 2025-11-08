# Importação das bibliotecas
from flask import Flask
from tarefa import buscar_tarefas

# Cria o objeto do flask
app = Flask(__name__)

# Criando nossa primeira rota /api
@app.route('/api')
def index():
    return 'Api rodando'

# Criando a rota que retorna as tarefas
@app.route('/api/tarefas')
def get_tarefas():
    tarefas = buscar_tarefas()
    return tarefas

# Identifica que é o arquivo principal
# E liga o servidor executando o Flask 😊
if __name__ == "__main__":
    app.run(debug=True)

  

