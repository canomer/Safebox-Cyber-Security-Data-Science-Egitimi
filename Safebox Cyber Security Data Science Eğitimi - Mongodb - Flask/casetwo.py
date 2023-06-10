import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27817/")
db = connection('canomer5306')
UsersCollection = db['Users']

def get_users():
    users = UsersCollection.find()
    for user in users:
        print(user)

def get_users_by_name(name):
    users = UsersCollection.find({'name': name})
    for user in users:
        print(user)

def get_users_gt_20():
    users = UsersCollection.find({'age': {'$gt': 20}})
    for user in users:
        print(user)

def update_users_gt_25():
    UsersCollection.update_many({'age': {'$gt': 25}}, {'$set': {'description': 0}})

def delete_users_by_age(min, max):
    UsersCollection.delete_many({'age': {'$gt': min, '$lt': max_age}})

if __name__ == '__main__':
    print('################### ALL USERS DATA ###################')
    get_users()
    print('################### USER DATA BY NAME ###################')
    get_users_by_name('Ahmet')
    print('################### USERS OLDER THAN 20 YO ###################')
    get_users_gt_20()
    print('################### CHANGE DESCRIPTION OF USERS WHO OLDER THAN 25 ###################')
    update_users_gt_25()
    print('################### DELETE ALL USERS BY AGE BETWEEN 45 & 48 ###################')
    delete_users_by_age(45, 48)
