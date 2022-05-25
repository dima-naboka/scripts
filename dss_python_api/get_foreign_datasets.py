
# coding: utf-8

# In[1]:


import dataiku
import json
# print json.dumps(dataset,indent=2)
client = dataiku.api_client()
# current_project_1 = dataiku.api_client().get_project(dataiku.get_custom_variables()["projectKey"])
# all_datasets = current_project.list_datasets()
projects = client.list_projects()


# In[4]:


for project in projects:
#     print json.dumps(project,indent=2)
#     break
    current_project = dataiku.api_client().get_project(project['projectKey'])
#     print json.dumps(project['projectKey'],indent=2)
    settings = current_project.get_settings()
    exposed_objects = settings.get_raw()['exposedObjects']['objects']
#     print json.dumps(exposed_objects,indent=2)
    if exposed_objects:
        print('=== {} exposed objects ==='.format(project['projectKey']))
        for index in range(len(exposed_objects)):
            ds_nm = exposed_objects[index]['localName']
            trg_prj = exposed_objects[index]['rules']
#             print json.dumps(exposed_objects[index],indent=2)
            trg_prj_names = []
            for index in range(len(trg_prj)):
                trg_prj_names.append(trg_prj[index]['targetProject'])
            print("Dataset %s is exposed in %s project(s)" % (ds_nm,', '.join(trg_prj_names)))
        print('\n')


# In[ ]:


current_project


# In[ ]:


current_project_1


# In[ ]:


for dataset in all_datasets:
    if dataset['name'] == 'heatmap_manual':
        print json.dumps(dataset,indent=2)


# In[ ]:


settings = current_project.get_settings()


# In[ ]:


settings.get_raw()['exposedObjects']['objects'][0]


# In[ ]:


settings_TEST = dataiku.api_client().get_project('SOME_ETL_BASICS').get_settings()
# all_datasets = current_project.list_datasets()
settings_TEST.get_raw()['exposedObjects']['objects'][0]


# In[ ]:


settings = current_project_1.get_settings()
exposed_objects = settings.get_raw()['exposedObjects']['objects']
#     print json.dumps(exposed_objects,indent=2)
if len(exposed_objects):
    print('not 0')
    print('=== {} exposed objects ==='.format(dataiku.get_custom_variables()["projectKey"])
#     for index in range(len(exposed_objects)):
#         ds_nm = exposed_objects[index]['localName']
#         trg_prj = exposed_objects[index]['rules']
# #             print json.dumps(exposed_objects[index],indent=2)
#         trg_prj_names = []
#         for index in range(len(trg_prj)):
#             trg_prj_names.append(trg_prj[index]['targetProject'])
#         print("Dataset %s is exposed in %s project(s)" % (ds_nm,', '.join(trg_prj_names)))
#     print('\n')


# In[ ]:


exposed_objects
# if len(exposed_objects):
#     print('not 0')
#     a + Bq
# else:
#     print('is 0')

