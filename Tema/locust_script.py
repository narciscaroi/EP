import time
from locust import HttpUser, task, between, constant_pacing


class WorkerTest(HttpUser):
    wait_time = between(1, 4)

    #@task
    #def us_worker(self):
        #self.client.get(url="/work/us/1")

    #@task
    #def asia_worker(self):
        #self.client.get(url="/work/asia/1")

    #@task
    #def emea_worker(self):
       #self.client.get(url="/work/emea/0")

    #@task
    #def us_worker(self):
        #self.client.get(url="/work/us")

    #@task
    #def asia_worker(self):
        #self.client.get(url="/work/asia")

    #@task
    #def emea_worker(self):
        #self.client.get(url="/work/emea")

    
    #heroku
    @task
    def heroku_worker(self):
        self.client.get(url="")
