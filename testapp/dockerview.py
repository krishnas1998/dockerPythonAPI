import os
import docker
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class GetProvisionID(APIView):
    def get(self, request, cpu_cores, memory, login_method, format=None):
        client = docker.from_env()
        container = client.containers.run('ubuntu', detach=True, cpu_count=cpu_cores, mem_limit=memory )
        #print(container.id)
        print(container)
        # print(output.Container)
        return Response({'provision_id':container.id})

class GetProvisionStatus(APIView):
    def get(self, request, provision_id, format=None):
        client = docker.from_env()
        container = client.containers.get(provision_id)  
        return Response({'provision_status':container.status})
