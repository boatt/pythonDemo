#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseResult(object):
    code = 200
    message = "成功"
    data = {}

    def __init__(self):
        pass

    def __obj_2_json__(obj):
        return {
            "code": obj.code,
            "message": obj.message,
            # "data": self.data
        }
