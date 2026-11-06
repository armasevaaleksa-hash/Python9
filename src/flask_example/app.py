from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_id_counter = 0

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    global task_id_counter
    task_content = request.form['content']
    if task_content:
        task_id_counter += 1
        new_task = {'id': task_id_counter, 'content': task_content, 'done': False}
        tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/done/<int:id>')
def done(id):
    for task in tasks:
        if task['id'] == id:
            task['done'] = True
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)