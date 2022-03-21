import load_balancer as lb
import concurrent.futures
import requests

def round_robin_policy(number_of_requests):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		futures = []
		for i in range(0, number_of_requests):
			futures.append(executor.submit(requests.get, lb.workers[i%5]))
