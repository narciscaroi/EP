import load_balancer as lb
import concurrent.futures
import requests
import sys

def get_fastest_time(workers):
	minim_time = int(sys.maxsize)
	index = -1
	for i in range(0, len(workers)):
		response = requests.get(workers[i])
		if minim_time > response.json()['response_time']:
			minim_time = response.json()['response_time']
			index = i
	return index
		

def fastest_time_policy(number_of_requests):
	index = get_fastest_time(lb.workers)

	with concurrent.futures.ThreadPoolExecutor() as executor:
		futures = []
		for i in range(0, number_of_requests):
			futures.append(executor.submit(requests.get, lb.workers[index]))