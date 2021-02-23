from fastapi import status
from fastapi.responses  import JSONResponse
from functools import wraps

import json

def formate_response(code,data,in_message=None):
    return JSONResponse(
        content         = {
            'code'      : code,
            'message'   : in_message,
            'data'      : data,
        }
    )

def formate_pandas(pd_data):
    _json_data = pd_data.to_json(orient ="records")
    return _json_data


async def formate_response_decorator(input_function):
    @wraps(input_function)
    async def wrapTheFunction(*args, **kwargs):
        r = await input_function(*args, **kwargs)
        print(r)
        r = list(r)
        return formate_response(r[0],r[1],r[2])	   
    return wrapTheFunction