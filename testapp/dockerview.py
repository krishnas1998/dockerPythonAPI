import os
import docker #imports dockers sdk
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

#-----------------------------------------------------------------------------------------------
# Create a new ubuntu container and returns the provision id/ container id
# cpu_cores -> Number of usable CPUs (Windows only)
# mem_limit -> (int or str): Memory limit. Accepts float values
#                (which represent the memory limit of the created container in
#                bytes) or a string with a units identification char
#                (``100000b``, ``1000k``, ``128m``, ``1g``). If a string is
#                specified without a units character, bytes are assumed as an
#                intended unit.
# login_method -> SSH login method either with a password or a private key (not used for now)
#-----------------------------------------------------------------------------------------------
class GetProvisionID(APIView):
    def get(self, request, cpu_cores, memory, login_method, format=None):
        client = docker.from_env()
        image_name = "ubuntu"
        container = client.containers.run(image_name, detach=True, cpu_count=cpu_cores, mem_limit=memory )
        return Response({'provision_id':container.id})

#-----------------------------------------------------------------------------------------------
# Returns the provision status of the container of passed provision id
# If the container is running then it also returns the instance ip address and ssh port
# Parameters:
# provision_id - It is the container id of the container
#-----------------------------------------------------------------------------------------------
class GetProvisionStatus(APIView):
    def get(self, request, provision_id, format=None):
        client = docker.from_env()
        container = client.containers.get(provision_id)  
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        host_port = container.ports
        if container.status == 'running':
            response = {'provision_status':container.status, 'instance_ip': ip_add, 'ssh_port': host_port}
        else:
            response = {'provision_status':container.status}
        return Response(response)
