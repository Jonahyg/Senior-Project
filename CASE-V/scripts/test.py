from os import environ as env
from openstack import connection
import openstack
import subprocess
import sys
import json

conn = connection.Connection(auth_url=env['OS_AUTH_URL'],
	username=env['OS_USERNAME'],
	password=env['OS_PASSWORD'],
	project_name='demo',
	user_domain_id='default',
	project_domain_id='default')


j = json.loads(sys.argv[1])
print j['email']
#glance_endpoint = keystone.service_catalog.url_for(service_type='image')
#glance = glclient.Client(glance_endpoint, token=keystone.auth_token)
#images = glance.images.list()
#print images
#print list(images)