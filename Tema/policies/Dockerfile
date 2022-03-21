FROM python:3.8.10
ADD load_balancer.py /
ADD random_policy.py /
ADD round_robin_policy.py /
ADD weighted_round_robin_policy.py /
ADD least_connection_policy.py /
ADD fastest_time_policy.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "load_balancer.py"]