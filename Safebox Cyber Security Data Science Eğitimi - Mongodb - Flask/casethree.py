from flask import Flask, jsonify, request
from pymongo

app = Flask(__name__)

connection = pymongo.MongoClient("mongodb://localhost:27817/")
db = connection('canomer5306')
UsersCollection = db['Users']

@app.route('/adduser', methods=['POST'])
def add_user():
    user_data = request.get_json()
    UsersCollection.insert_one(user_data)
    return {'message':"Basarili bir sekilde kullanici eklenmistir"}

@app.route('/25', methods=['GET'])
def get_users_over_25():
    users = UsersCollection.find({'age': {'$gt': 25}})
    user_list = []
    for user in users:
        user_list.append(user)
    return user_list

@app.route('/', methods=['GET'])
def get_all_users():
    users = UsersCollection.find()
    user_list = []
    for user in users:
        user_list.append(user)
    return user_list

@app.route('/deleteuser', methods=['POST', 'DELETE'])
def delete_user():
    user_id = request.args.get('id')
    UsersCollection.delete_one({'_id': user_id})
    return {'message':"Basarili bir sekilde kullanici silinmistir"}

if __name__ == '__main__':
    app.run()
