# Laptop Service

from flask import Flask, request, redirect, url_for, render_template, make_response, jsonify
from flask_restful import Resource, Api
import os
import flask
from pymongo import MongoClient
import password, testToken

# Instantiate the app
app = Flask(__name__)
api = Api(app)

client = MongoClient('db', 27017)
db = client.tododb
db_user = client.user


##########################################
############ P R O J E C T 6 #############
##########################################
class listAll(Resource):
    def get(self):
        top = request.args.get("top")
        _items = db.tododb.find()
        items = [item for item in _items]
        all_list = []
        for time in items:
            all_list.append(time['open'])
            all_list.append(time['close'])
        all_list.sort()
        if(top == None):
            return {
                'result': all_list
            }
        elif(not top.isdigit()):
            return 'please input key as interger'
        elif(int(top) > len(items)):
            return 'key value is too large'
        else:   
            l = len(items) 
            new_list = []
            for i in range(int(top)):
                new_list.append(all_list[i])
                new_list.append(all_list[i+l])
            return {
                'result': new_list
            }

class listOpenOnly(Resource):
    def get(self):
        top = request.args.get("top")
        _items = db.tododb.find()
        items = [item for item in _items]
        open_list = []
        for time in items:
            open_list.append(time['open'])
        open_list.sort()
        if(top == None):
            return {
                'result': open_list
            }
        elif(not top.isdigit()):
            return 'please input key as interger'
        elif(int(top) > len(items)):
            return 'key value is too large'
        else:
            new_list2 = []
            for i in range(int(top)):
                new_list2.append(open_list[i])
            return {
                'result': new_list2
            }

class listCloseOnly(Resource):
    def get(self):
        top = request.args.get("top")
        _items = db.tododb.find()
        items = [item for item in _items]
        close_list = []
        for time in items:
            close_list.append(time['close'])

        close_list.sort()
        if(top == None):
            return {
                'result': close_list
            }
        elif(not top.isdigit()):
            return 'please input key as interger'
        elif(int(top) > len(items)):
            return 'key value is too large'
        else:
            new_list3 = []
            for i in range(int(top)):
                new_list3.append(close_list[i])
            return {
                'result': new_list3
            }

class listAll_json(Resource):
    def get(self):
        top = request.args.get("top")
        _items = db.tododb.find()
        items = [item for item in _items]
        all_list2 = []
        for time in items:
            all_list2.append(time['open'])
            all_list2.append(time['close'])
        
        all_list2.sort()
        if(top == None):
            return {
                'result': all_list2
            }
        elif(not top.isdigit()):
            return 'please input key as interger'
        elif(int(top) > len(items)):
            return 'key value is too large'
        else:
            l = len(items) 
            new_list4 = []
            for i in range(int(top)):
                new_list4.append(all_list2[i])
                new_list4.append(all_list2[i+l])

            return {
                'result': new_list4
            }


class listOpenOnly_json(Resource):
    def get(self):
        top = request.args.get("top")
        _items = db.tododb.find()
        items = [item for item in _items]
        open_list2 = []
        for time in items:
            open_list2.append(time['open'])
        
        open_list2.sort()
        if(top == None):
            return {
                'result': open_list2
            }
        elif(not top.isdigit()):
            return 'please input key as interger'
        elif(int(top) > len(items)):
            return 'key value is too large'
        else:
            new_list5 = []
            for i in range(int(top)):
                new_list5.append(open_list2[i])
            return {
                'result': new_list5
            }

class listCloseOnly_json(Resource):
    def get(self):
        top = request.args.get("top")
        _items = db.tododb.find()
        items = [item for item in _items]
        close_list2 = []
        for time in items:
            close_list2.append(time['close'])
        
        close_list2.sort()
        if(top == None):
            return {
                'result': close_list2
            }
        elif(not top.isdigit()):
            return 'please input key as interger'
        elif(int(top) > len(items)):
            return 'key value is too large'
        else:
            new_list6 = []
            for i in range(int(top)):
                new_list6.append(close_list2[i])
            return {
                'result': new_list6
            }


class listAll_csv(Resource):
    def get(self):
        top = request.args.get("top")
        _items = db.tododb.find()
        items = [item for item in _items]
        all_list3 = []
        for time in items:
            all_list3.append(time['open'])
            all_list3.append(time['close'])
        all_list3.sort()
        all_string = ''
        
        if(top == None):
            for time in all_list3:
                all_string += str(time) + ','
            all_string = all_string[0:-1]
            return all_string
        
        elif (not top.isdigit()):
            return 'please input key as interger'

        elif(int(top) > len(items)):
            return 'key value is too large'
        else:
            for i in range(int(top)*2):
                all_string += str(all_list3[i]) + ','
            all_string = all_string[0:-1]
            return all_string
        


class listOpenOnly_csv(Resource):
    def get(self):
        top = request.args.get("top")
        _items = db.tododb.find()
        items = [item for item in _items]
        open_list3 = []
        for time in items:
            open_list3.append(time['open'])
        open_list3.sort()
        open_string = ''
        if(top == None):
            for time in open_list3:
                open_string += str(time) + ','
            open_string = open_string[0:-1]
            return open_string
        elif(not top.isdigit()):
            return 'please input key as interger'
        elif(int(top) > len(items)):
            return 'key value is too large'
        else:
            for i in range(int(top)):
                open_string += str(open_list3[i]) + ','
            open_string = open_string[0:-1]
            return open_string

        

class listCloseOnly_csv(Resource):
    def get(self):
        top = request.args.get("top")
        _items = db.tododb.find()
        items = [item for item in _items]
        close_list3 = []
        for time in items:
            close_list3.append(time['open'])
        close_list3.sort()
        close_string = ''
        if(top == None):
            for time in close_list3:
                close_string += str(time) + ','
            close_string = close_string[0:-1]
            return close_string
        elif(not top.isdigit()):
            return 'please input key as interger'
        elif(int(top) > len(items)):
            return 'key value is too large'
        else:
            for i in range(int(top)):
                close_string += str(close_list3[i]) + ','
            close_string = close_string[0:-1]
            return close_string
   


api.add_resource(listAll,'/listAll')
api.add_resource(listOpenOnly,'/listOpenOnly')
api.add_resource(listCloseOnly,'/listCloseOnly')
api.add_resource(listAll_json,'/listAll/json')
api.add_resource(listOpenOnly_json,'/listOpenOnly/json')
api.add_resource(listCloseOnly_json,'/listCloseOnly/json')
api.add_resource(listAll_csv,'/listAll/csv')
api.add_resource(listOpenOnly_csv,'/listOpenOnly/csv')
api.add_resource(listCloseOnly_csv,'/listCloseOnly/csv')

##########################################
############ P R O J E C T 6 #############
##########################################




'''
@app.route("/")
def index():

    return render_template('web.html')

@app.route("/_register", methods = ['POST'])
def _register():

    user = request.form['username']
    passw = request.form['password']

    _items = db_user.user.find({"user": user})
    items = [item for item in _items]

    if(user == None or passw == None or items != []):
        return str(user)+str(passw)+str(items)#flask.abort(400)
    else:
        _items2 = db_user.user.find()
        items2 = [item for item in _items2]

        pwd = password.hash_password(passw)
        values = {"_id": len(items2),"user":user, "password": pwd}
        db_user.user.insert_one(values)
        return 'sucess'

'''
##########################################
############ P R O J E C T 7 #############
##########################################
class index(Resource):
    def get(self):
        return make_response(render_template("web.html"))

class register(Resource):
    def post(self):
        user = request.form['username']
        passw = request.form['password']

        _items = db_user.user.find({"user": user})
        items = [item for item in _items]

        if(user == '' or passw == ''):
            return "Wrong user or password", 400
        elif(items != []):
            return "username already exist", 400
        else:
            _items2 = db_user.user.find()
            items2 = [item for item in _items2]
            pwd = password.hash_password(passw)
            values = {"location": len(items2),"user":user, "password": pwd}
            db_user.user.insert_one(values)
            return 'register success'

class token(Resource):
    def get(self):
        username = request.args.get("username")
        passw = request.args.get("password")
        data = db_user.user.find_one({"user": username})
        if username == None or passw == None:
            return "username or password wrong", 400
        elif data is None:
            return "no such username.", 401
        else:
            user_correct = password.verify_password(passw, data["password"])
            if(user_correct): 
                result = testToken.generate_auth_token(data["location"]).decode()
                return {"token" : result, "duration" : 600}, 201
            else:
                return "bad password.", 401


class usersss(Resource):
    def get(self, token):
        
        if(testToken.verify_auth_token(token)):
            _items = db.tododb.find()
            items = [item for item in _items]
            all_list4 = []
            for time in items:
                all_list4.append(time['open'])
                all_list4.append(time['close'])
            all_list4.sort()
            all_string = ''
            for i in all_list4:
                all_string += str(i) + ','
            all_string = all_string[0:-1]
            return all_string
        else:
            return "Wrong", 401

            
        


api.add_resource(index,'/api/register')
api.add_resource(register,'/api/register/method')
api.add_resource(token,'/api/token')
api.add_resource(usersss, '/user/<string:token>')


##########################################
############ P R O J E C T 7 #############
##########################################



# Run the application


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
