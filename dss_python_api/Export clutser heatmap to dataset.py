
# coding: utf-8

# In[ ]:


import dataiku
import pandas as pd


# In[ ]:


client = dataiku.api_client()
project = client.get_default_project()


# In[3]:


saved_model = project.get_saved_model('DgZA2bNG')


# In[17]:


# saved_model.get_settings()
version = saved_model.get_version_details(saved_model.get_active_version()['id'])
ht_dict = version.get_raw()['heatmap']


# In[18]:


# pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))
df = pd.DataFrame.from_dict(dict([ (k,pd.Series(v)) for k,v in ht_dict.items()]))


# In[31]:


print(json.dumps(version.get_raw()['heatmap'],indent=1))

