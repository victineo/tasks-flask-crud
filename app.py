from flask import Flask, request, jsonify
from models.task import Task

# __name__ = "__main__"
app = Flask(__name__)

tasks = []
task_id_control = 1

# Rota para criar tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ''))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({'message': 'Nova tarefa criada com sucesso.', 'id': new_task.id})

# Rota para exibir todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
            "tasks": task_list,
            "total_tasks": len(task_list)
            }
    return jsonify(output)

# Rota para exibir uma tarefa específica
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({'message:': 'Não foi possível encontrar a atividade.'}), 404

# Rota para atualizar uma tarefa
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({'message': 'Não foi possível encontrar a atividade.'}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    return jsonify({'message': 'Tarefa atualizada com sucesso.'})

# Rota para deletar uma tarefa
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({'message': 'Não foi possível encontrar a atividade.'}), 404
    
    tasks.remove(task)
    return jsonify({'message': 'Tarefa deletada com sucesso.'})

if __name__ == "__main__":
    app.run(debug=True)