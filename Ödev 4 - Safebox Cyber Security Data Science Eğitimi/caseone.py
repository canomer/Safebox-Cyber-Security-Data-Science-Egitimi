from flask import Flask, request
from pymongo

app = Flask(__name__)

connection = pymongo.MongoClient("mongodb://localhost:27817/")
db = connection('canomer5306')
UsersCollection = db['Users']

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    age = request.form['age']
    job = request.form['job']
    description = request.form('description', '1')
    
    user = {
        'name': name,
        'age': age,
        'job': job,
        'description': description
    }
    
    UsersCollection.insert_one(user)
    return {'message':"Basarili bir sekilde kullanici eklenmistir"}

if __name__ == '__main__':
    app.run(host = '127.0.1.1', port = 2005, debug = True)
