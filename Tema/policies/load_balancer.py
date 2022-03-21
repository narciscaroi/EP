import sys
import datetime
import multiprocessing
import random_policy as RandomPolicy
import round_robin_policy as RoundRobinPolicy
import weighted_round_robin_policy as WeightedRoundRobinPolicy
import least_connection_policy as LeastConnection
import fastest_time_policy as FastestTimePolicy

asia0 = 'http://localhost:5000/work/asia/0'
asia1 = 'http://localhost:5000/work/asia/1'
us0 = 'http://localhost:5000/work/us/0'
us1 = 'http://localhost:5000/work/us/1'
emea = 'http://localhost:5000/work/emea/0'
workers = [asia0, asia1, us0, us1, emea]

policies = ['random', 'roundRobin', 'weightedRoundRobin', 'leastConnection', 'fastestTime']
number_of_requests= 1
chosen_policy = ''

def parsing_arguments():
	if len(sys.argv) < 5:
		print("Some of the arguments were not intorduced. Please use -n <Number of requests> -p <policy name>")
		exit()


	if str(sys.argv[1]) != "-n" or not str(sys.argv[2]):
		print("Second argument incorrect. Please yse -n <number of requests> for the first argument")
		exit()

	if str(sys.argv[3]) != "-p" or not str(sys.argv[4]):
		print("Second argument incorrect. Please yse -p <name of the policy> for the first argument")
		exit()

	if str(sys.argv[4]) not in policies:
		print("Policy is invalid. Please use one of the following: " + str(policies))
		exit()

	global number_of_requests
	number_of_requests = int(str(sys.argv[2]))

	global chosen_policy
	chosen_policy = str(sys.argv[4])

if __name__ == "__main__":
	parsing_arguments();

	start_time = datetime.datetime.now()

	if chosen_policy == 'random':
		RandomPolicy.random_policy(number_of_requests)

	elif chosen_policy == 'roundRobin':
		RoundRobinPolicy.round_robin_policy(number_of_requests)

	elif chosen_policy == 'weightedRoundRobin':
		WeightedRoundRobinPolicy.weighted_round_robin_policy(number_of_requests)

	elif chosen_policy == 'leastConnection':
		LeastConnection.least_connection_policy(number_of_requests)

	elif chosen_policy == 'fastestTime':
		FastestTimePolicy.fastest_time_policy(number_of_requests)

	stop_time = datetime.datetime.now()
	interval = stop_time - start_time
	print("time for " + str(chosen_policy) + " is " + str(interval.total_seconds()))