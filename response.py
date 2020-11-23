from rest_framework.response import Response


def responseHandler(params):
    res2={
            "status":1,
            "responseData":params
        }
    return Response(res2)    




def errorHandler(params):
    res2={
            "status":0,
            "responseData":params
        }
    return Response(res2)        