import os
from flask import Flask, request

app = Flask(__name__)

users = {
    1: 'Karol Libardi',
    2: 'John Smith',
    3: 'Karol Marx',
}


@app.route('/')
def index():
    return "Hello from Remote Server - I was deployed from Circle CI"


operations = {
    'add': lambda x1, x2: x1 + x2,
    'subtract': lambda x1, x2: x1 - x2,
    'multiply': lambda x1, x2: x1 * x2,
    'divide': lambda x1, x2: x1 / x2
}


@app.route('/calc/add/', methods=['POST'])
def calc():
    return {"result": sum(request.json)}


@app.route('/calc/pow/', methods=['POST'])
def power():
    result = 1
    for x in range(0, request.json):
        result *= x + 1
    return {"result": result}


@app.route('/reverse', methods=['POST'])
def flipText():
    reversedText = request.json.split(' ')
    return ' '.join(reversed(reversedText))


@app.route('/users/<int:user_id>')
def page(user_id):
    try:
        return find_user_by_id(users, user_id)
    except KeyError:
        return "User not found...", 404


def find_user_by_id(users_dict, user_id):
    return users_dict[user_id]


@app.route('/users/<user_name>')
def page2(user_name):
    results = []
    for name in users.values():
        if user_name in name.lower():
            results.append(name)
    if results:
        return ", ".join(results)
    else:
        return "User not found by name...", 404


@app.errorhandler(404)
def not_found(e):
    return "Not found"


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 8080)),
            debug=True)
