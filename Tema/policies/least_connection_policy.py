import load_balancer as lb
import concurrent.futures
import requests

times_recorder = {}
minim_counter = 0

def init_recorder():
	global times_recorder
	times_recorder = {lb.workers[0] : 0,
		lb.workers[1] : 0,
		lb.workers[2] : 0,
		lb.workers[3] : 0,
		lb.workers[4] : 0
	}

def min_counter():
	minim = min(times_recorder, key=times_recorder.get)
	times_recorder[minim] += 1
	return minim

def least_connection_policy(number_of_requests):
	init_recorder()

	with concurrent.futures.ThreadPoolExecutor() as executor:
		futures = []
		for i in range(0, number_of_requests):
			futures.append(executor.submit(requests.get, min_counter()))