import load_balancer as lb
import concurrent.futures
import requests

# us -> 2x us0, 2x us1 = 4
# asia -> 1x asia1, 1x asia2 = 2
# emea -> 3x emea0 = 3

def weighted_round_robin_policy(number_of_requests):
	workers_aux = [lb.emea, lb.us0, lb.us1, lb.asia0, lb.asia1, lb.emea, lb.us0, lb.us1, lb.emea]
	with concurrent.futures.ThreadPoolExecutor() as executor:
		futures = []
		for i in range(0, int(number_of_requests)):
			futures.append(executor.submit(requests.get, workers_aux[i % len(workers_aux)]))