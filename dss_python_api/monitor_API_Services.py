
# coding: utf-8

# In[1]:


import dataiku
import json
import time


# In[2]:


client = dataiku.api_client()
deployer = client.get_apideployer()


# In[18]:


for service in deployer.list_services():
    service_raw =service.get_status().get_raw()
    if service_raw['deployments']:        
        print('+++')
        print 'iterating over {} API Service'.format(service_raw['serviceBasicInfo']['id'])
        print('+++')
        for index in range(len(service_raw['deployments'])):
#             service_raw['deployments'][index]['infraId']
            deployment = deployer.get_deployment(service_raw['deployments'][index]['id'])
            if deployment.get_status().get_health() != 'HEALTHY':
                print '{} status is {}'.format(service_raw['deployments'][index]['id'],deployment.get_status().get_health())
#             print json.dumps(service_raw['deployments'][index],indent=2)
#             print service_raw['infras']
                print('===')
#     break


# In[ ]:


service_raw


# In[ ]:


# deployment = deployer.get_deployment('new_service-on-api_node_ubuntuVM')
# deployment = deployer.get_deployment('predict-on-vagrant_box_api1') -- loading forever
# deployment = deployer.get_deployment('r32-on-api_node_ubuntuVM')
# d_stat = deployment.get_status()
# d_stat.get_health()


# In[ ]:


# looks like not required when get_health() is available 
import requests
r =requests.get('http://api-vm-dss.localhost.com:45200/monitoring/api/r32/isAliveSimple')
r.status_code


# In[ ]:


r =requests.get('http://api-vm-dss.localhost.com:45200/monitoring/api/py_func/isAliveSimple')
r.status_code

