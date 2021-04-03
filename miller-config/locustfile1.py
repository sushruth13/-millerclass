import base64

from locust import HttpUser, TaskSet, task
from random import randint, choice


class WebTasks(TaskSet):

    @task
    def load(self):
        # username="\n"
        # password=''
        # user_bytes=username.encode('ascii')
        # pass_bytes=password.encode('ascii')
        # base64user = base64.encodebytes(user_bytes)
        # base64password = base64.encodebytes(pass_bytes)

        # catalogue = self.client.get("/catalogue").json()
        # #print(catalogue)
        # category_item = choice(catalogue)
        # #print(category_item)
        # item_id = category_item["id"]
        # print(item_id)

        self.client.get("/")
        #self.client.get("/login",auth=(base64user,base64password))
        # self.client.get("/category.html")
        # self.client.get("/detail.html?id={}".format(item_id))
        # self.client.delete("/cart")
        # self.client.post("/cart", json={"id": item_id, "quantity": 1})
        # self.client.get("/basket.html")
        #self.client.post("/orders")


class Web(HttpUser):
    tasks = [WebTasks]
    min_wait = 0
    max_wait = 0
