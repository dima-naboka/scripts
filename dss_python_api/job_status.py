
# coding: utf-8

# In[1]:


import dataiku
import json
#print(json.dumps(job,indent=4))

client = dataiku.api_client()
current_project = client.get_project(dataiku.get_custom_variables()["projectKey"])


# In[2]:


import datetime 
from datetime import time
midnight = datetime.datetime.combine(datetime.datetime.today(), time.min)
midnight_as_timestamp = (midnight - datetime.datetime(1970,1,1)).total_seconds() * 1000
midnight_as_timestamp

# failed_jobs = [job for job in current_project.list_jobs() if job['state'] == 'FAILED']
# for jb in failed_jobs:
#     print(jb['def']['id'])


# In[ ]:


for job in current_project.list_jobs():
    if job['state'] == 'FAILED' and job['def']['initiationTimestamp'] >= midnight_as_timestamp:
        print (job)
#     if job['state'] == 'FAILED':
#         print(json.dumps(job['def']['initiationTimestamp'],indent=4))
#     print(json.dumps(job['state'],indent=4))
#     print(json.dumps(job,indent=4))
#     break


# In[5]:


print('printing jobs that failed since {}').format(midnight)
for project_name in client.list_project_keys():
    for job in client.get_project(project_name).list_jobs():
        if job['state'] == 'FAILED' and job['def']['initiationTimestamp'] >= midnight_as_timestamp:
            print('===')
            print('project name: {}').format(project_name)
            print('job name: {}').format(job['def']['name'])

