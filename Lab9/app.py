from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список для зберігання покупок (в оперативній пам'яті)
# Кожна покупка — це словник з id, назвою (name) та статусом покупки (bought)
items = []
item_id_counter = 0

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    global item_id_counter
    item_name = request.form.get('name')
    if item_name:
        item_id_counter += 1
        new_item = {'id': item_id_counter, 'name': item_name, 'bought': False}
        items.append(new_item)
    return redirect(url_for('index'))

@app.route('/bought/<int:item_id>')
def bought(item_id):
    for item in items:
        if item['id'] == item_id:
            item['bought'] = True
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)