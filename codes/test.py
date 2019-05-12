from rest_framework.test import APIRequestFactory
import pdb, sys

lines = sys.stdin.readlines()
sys.stdin = open('/dev/tty')

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'})

pdb.set_trace()
