from fastapi import status
from fastapi.responses  import JSONResponse
from functools import wraps

def formate_response(code,data,in_message=None):
    return JSONResponse(
        content         = {
            'code'      : code,
            'message'   : in_message,
            'data'      : data,
        }
    )

# def formate_response_decorator(input_function):
#     print(111)
#     @wraps(input_function)
#     def wrapTheFunction(*args, **kwargs):
#         r = input_function(*args, **kwargs)
#         r = list(r)
#         yield formate_response(r[0],r[1],r[2])	   
#     return wrapTheFunction