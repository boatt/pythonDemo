#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from bean.DBHelp import DBHelp

dbhelp = DBHelp()
# dbhelp.insertData()
data = dbhelp.getData("13072176245", 12346)
jsonData = {"code": data.code, "message": data.message, "data": data.data}
jsonStr = json.dumps(jsonData)
print(jsonStr)
