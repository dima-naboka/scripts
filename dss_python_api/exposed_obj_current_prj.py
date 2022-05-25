
# coding: utf-8

# In[1]:


import dataiku
import json
# print json.dumps(dataset,indent=2)
client = dataiku.api_client()
current_project_1 = dataiku.api_client().get_project(dataiku.get_custom_variables()["projectKey"])


# In[2]:


settings = current_project_1.get_settings()
exposed_objects = settings.get_raw()['exposedObjects']['objects']
#     print json.dumps(exposed_objects,indent=2)
if len(exposed_objects):
#     print('not 0')
    print('=== {} exposed objects ==='.format(dataiku.get_custom_variables()["projectKey"]))
    for index in range(len(exposed_objects)):
        ds_nm = exposed_objects[index]['localName']
        trg_prj = exposed_objects[index]['rules']
#             print json.dumps(exposed_objects[index],indent=2)
        trg_prj_names = []
        for index in range(len(trg_prj)):
            trg_prj_names.append(trg_prj[index]['targetProject'])
        print("Dataset %s is exposed in %s project(s)" % (ds_nm,', '.join(trg_prj_names)))
    print('\n')

