#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request

from bean.DBHelp import DBHelp
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Flask!'


@app.route('/testLogin', methods=['GET', 'POST'])
def testLogin():
    phone = request.args.get('phone')  # 荐股列表类型 all=全部；current=进行中；history=历史
    password = request.args.get('password')
    dbhelp = DBHelp()
    # dbhelp.insertData()
    data = dbhelp.getData(phone,password)
    jsonData = {"code": data.code, "message": data.message, "data": data.data}
    jsonStr = json.dumps(jsonData)
    # print(jsonStr)
    return jsonStr


@app.route('/login')
def home():
    dbhelp = DBHelp()
    # dbhelp.insertData()
    data = dbhelp.getData()
    jsonData = {"code": data.code, "message": data.message, "data": data.data}
    jsonStr = json.dumps(jsonData)
    # print(jsonStr)
    return jsonStr


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5001, debug=True)
