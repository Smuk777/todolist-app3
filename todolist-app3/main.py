# Importação das bibliotecas
from flask import Flask, request
from tarefa import buscar_tarefas, buscar_tarefa, apagar_tarefa, criar_tarefa, atualizar_tarefa

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

@app.route('/api/tarefa/<int:tarefa_id>')
def get_tarefa(tarefa_id):
    tarefa = buscar_tarefa(tarefa_id)
    return tarefa

@app.route('/api/tarefa/<int:tarefa_id>', methods=['DELETE'])
def delete_tarefa(tarefa_id):
    apagar_tarefa(tarefa_id)
    return{
        'message': 'Tarefa apagada com sucesso'
    }

@app.route('/api/tarefa', methods=['POST'])
def create_tarefa():
    corpo = request.get_json()
    nome = corpo.get('nome')
    descricao = corpo.get('descricao')
    criar_tarefa(nome, descricao)
    return{
        'message': 'Tarefa cadastrada com sucesso!'
    }

@app.route('/api/tarefa/<int:tarefa_id>', methods=['PUT'])
def update_tarefa(tarefa_id):
    corpo = request.get_json()
    nome = corpo.get('nome')
    descricao = corpo.get('descricao')
    atualizar_tarefa(nome, descricao, tarefa_id)
    return{
        'message': 'Tarefa atualizada com sucesso'
    }

# Identifica que é o arquivo principal
# E liga o servidor executando o Flask 😊
if __name__ == "__main__":
    app.run(debug=True)

  

