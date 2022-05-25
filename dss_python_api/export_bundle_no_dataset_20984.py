
# coding: utf-8

# In[1]:


import dataiku
from datetime import datetime


# In[2]:


client = dataiku.api_client()
current_project = dataiku.api_client().get_project(dataiku.get_custom_variables()["projectKey"])


# In[3]:


bundle_name = datetime.now().strftime('%Y%m%d_%H%M%S')
# datasets_to_add = ['new_table','test_table','trucks']
datasets_to_add = ['new_table','trucks']
included_datasets = list()

for dataset in datasets_to_add:
    dataset_settings = current_project.get_dataset(dataset).get_settings()
#     dataset_settings = dataset
#     included_datasets.pop
#     a=[(value,dataset_settings.get_raw()[value]) for value in ['name','type'] if value in dataset_settings.get_raw()]
#     print (a)
#     b = list()
#     b={(value,dataset_settings.get_raw()[value]) for value in ['name','type'] if value in dataset_settings.get_raw()}
            
#     print ('--',b)
#     print('--',{**b})
    

#     included_datasets.append(b)
#     print (included_datasets)
    included_datasets.append({value:dataset_settings.get_raw()[value] for value in ['name','type'] if value in dataset_settings.get_raw()})    


# In[4]:


project_settings = current_project.get_settings()
# project_settings.settings.get('bundleExporterSettings').get('exportOptions')['includedDatasetsData'] = \
# [{u'name': u'test_table', u'type': u'PostgreSQL'},{u'name': u'new_table', u'type': u'PostgreSQL'}]
project_settings.settings.get('bundleExporterSettings').get('exportOptions')['includedDatasetsData'] = included_datasets
project_settings.save()


# In[5]:


current_project.export_bundle(bundle_name)

