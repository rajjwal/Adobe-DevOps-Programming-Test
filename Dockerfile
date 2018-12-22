FROM python:2.7
ADD minimal_network.py network.txt /
CMD ["python", "-u", "./minimal_network.py"]