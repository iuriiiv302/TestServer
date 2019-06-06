import math

import requests
from requests.auth import HTTPBasicAuth
import requests


def token(url):
    values = {'username': 'admintestt',
              'password': '123'}

    r = requests.post(url, data=values)
    data = r.json()
    return data["access"]


tok = token('https://tasks.devebs.net/api/users/token/')




# Create Task

def test_add_task(tok):
    print("Creating tasks..")
    import time
    start = time.time()
    for i in range(2):
        payload = {'title': 'TestTitleNew',
                   'description': 'Test1Description',
                   'user_assigned': 10715,
                   }

        r= requests.post("https://tasks.devebs.net/api/task/create/", data=payload,
                      headers={"authorization": "Bearer " + str(tok)})
        print(token)

        if r.status_code == 401:
            tok = token('https://tasks.devebs.net/api/users/token/')
        # print(tok)



test_add = test_add_task(token)
#
#
# def losttask(url):
#     r = requests.get(url).json()
#     last = (r['results'][0]['id'])
#     return last
# last_id = losttask('https://tasks.devebs.net/api/task/?page=1')
# print(last_id)
# #
# #
# def test_add_task(token):
#     print("Changing status..")
#     import time
#     start = time.time()
#     for i in range(2):
#
#         payload = {
#             "id": (last_id-i),
#             "status": "inprocess"
#         }
#
#         requests.put("https://tasks.devebs.net/api/task/update_status/", data=payload,
#                       headers={"authorization": "Bearer " + token})
#
#         payload = {"start_time": "2019-06-06T06:24:14.274Z",
#                    "duration": 10}
#
#         requests.post("https://tasks.devebs.net/api/task/" + str(last_id-i) + "/add_log/", data=payload,
#                       headers={"authorization": "Bearer " + token})
#
#     end = time.time()
#     print("execution time: " + str(end - start))
#
#
# test_change = test_add_task(token)
