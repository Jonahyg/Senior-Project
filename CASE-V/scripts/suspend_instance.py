from os import environ as env
from openstack import connection
import openstack
import subprocess
import sys
import json
import time


user = json.loads(sys.argv[1])
user_name = user["username"]
project_name = user["projectname"]
pwd = user["pwd"]
projectid = user["projectid"]
server = sys.argv[2]

conn = connection.Connection(
    region_name=env['OS_REGION_NAME'],
	auth=dict(
		auth_url=env['OS_AUTH_URL'],
	    username=user_name,
	    password=pwd,
	    project_id=projectid,
	    user_domain_id=env['OS_PROJECT_DOMAIN_ID']),
	compute_api_version=2,
	identity_interface=env['OS_INTERFACE'])


for instance in conn.compute.servers():
	if instance.name == server:
		if instance.status ==  'ACTIVE':
			conn.compute.suspend_server(instance.id)
			time.sleep(7)
		else:
			conn.compute.resume_server(instance.id)
			time.sleep(5)
			#print server.status
		print "Done"