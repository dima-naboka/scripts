
# coding: utf-8

# In[1]:


import dataiku
import requests
import json


# In[5]:


client = dataiku.api_client()
dss_projects = client.list_project_keys()
hostname = "http://localhost:11200"
design_api_key = "TsYgTg7xAhIi7RSwCAp3uv5jioNvzaZo"

for project_key in dss_projects:
    get_webapps = "{}/public/api/projects/{}/webapps/".format(hostname,project_key)
    r = requests.get(get_webapps, auth=(design_api_key, ''))
    if r.json():        
        print('!checking if '+project_key+' has running webapps')

        for wb in r.json():
            get_webapp_id = "{}/public/api/projects/{}/webapps/{}".format(hostname,project_key,wb['id'])
            stop_webapp = "{}/public/api/projects/{}/webapps/{}/backend/actions/stop".format(hostname,project_key,wb['id'])
            r_stp = requests.get(get_webapp_id, auth=(design_api_key, ''))
            if wb['backendRunning']:
                requests.put(stop_webapp,auth=(design_api_key, ''))
                print('stopped '+ wb['projectKey'] + ':' + wb['name'] + ':' + wb['id'] + ' webapp')

#     else:
#         raise SystemExit
    
#     for wid in prj_id_webapp:
    #         print(project_key)
#         get_webapp_state = "http://{}/public/api/projects/{}/webapps/{}/backend/state".format(hostname,project_key,wid)
#         stop_webapp = "http://{}/public/api/projects/{}/webapps/{}/backend/actions/stop".format(hostname,project_key,wid)
#         r_id = requests.get(get_webapp_state, auth=(design_api_key, ''))
    #         print('---backend state----')
#         if r_id.status_code == 200:
#             for wba in r.json():
#                 if wba['backendRunning']:
#     #                     requests.put(stop_webapp, auth=(design_api_key, ''))
#                     print('stopped '+ wba['projectKey'] + ':' + wba['name'] + ':' + wba['id'] + ' webapp')

