import configuration
import requests

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

def get_order(number_track):
    path  = configuration.URL_SERVICE+configuration.GET_ORDER_PATH+"?t="+str(number_track)
    response = requests.get(path)
    return response