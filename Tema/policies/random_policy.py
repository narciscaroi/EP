import load_balancer as lb
import requests
import concurrent.futures
from random import randrange

def random_policy(number_of_requests):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		futures = []
		for i in range(0, number_of_requests):
			futures.append(executor.submit(requests.get, lb.workers[randrange(5)]))
		