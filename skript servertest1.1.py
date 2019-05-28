import math

import requests
from requests.auth import HTTPBasicAuth
import requests


def token(url):
    values = {'username': 'admintest',
              'password': '123'}

    r = requests.post(url, data=values)
    data = r.json()
    return data["access"]


token = token('https://tasks.devebs.net/users/token/')


#Create Task

def test_add_task(token):
    print("Creating tasks..")
    import time
    start = time.time()
    for i in range(35):
        payload = {'title': 'TestTitle',
                   'description': 'Test1Description',
                   'status': 'created',
                   'user_assigned': 1,
                   'date_create_task': "2019-05-24T12:34:56.139Z"}

        r = requests.post("https://tasks.devebs.net/task/create/", data=payload, headers={"authorization": "Bearer " + token})
    end = time.time()
    print("execution time: "+str(end-start))
rezoult_create = test_add_task(token)


## View List Task

# def test_list(token):
#     while True:
#         r = requests.get("https://tasks.devebs.net/task/?page=1",
#                          headers={'content-type': 'application/json', "authorization": "Bearer " + token})
#         print(r.json())
#
# rezoul_test_list =test_list(token)


## DELETE TASK

# def losttask(url):
#     r = requests.get(url).json()
#     last = (r['results'][0]['id'])
#     return last
#
#
# def firsttask(url):
#     r = requests.get(url).json()
#
#     alltask = (r['count'])
#     last_page = math.ceil(alltask / 10)
#     r = requests.get('https://tasks.devebs.net/task/?page=' + str(last_page)).json()
#     for result in r['results']:
#         firstid = (result['id'])
#     return firstid
#
#
# def test_delete_task(token, last, firstid):
#     print("Deleting tasks..")
#     import time
#     start = time.time()
#     for i in range(firstid, last + 1):
#         r = requests.delete("https://tasks.devebs.net/task/delete_task/" + str(i) + "/",
#                             headers={"authorization": "Bearer " + token})
#     end = time.time()
#     print("execution time: " + str(end - start))
#
#
# rezoult_create = test_delete_task(token, losttask('https://tasks.devebs.net/task/?page=1'),
#                                firsttask('https://tasks.devebs.net/task/?page=1'))
