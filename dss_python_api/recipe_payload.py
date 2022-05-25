
# coding: utf-8

# In[1]:


import dataiku
import json
#print(json.dumps(job,indent=4))

client = dataiku.api_client()
current_project = client.get_project(dataiku.get_custom_variables()["projectKey"])


# In[3]:


recipes_cl = current_project.list_recipes()
for recipe_cl in recipes_cl:
    if recipe_cl["type"] == "python":
        payload = current_project.get_recipe(recipe_cl["name"]).get_settings().get_payload()
        print(payload)
        print('===')


# In[ ]:


recipes = current_project.list_recipes()
for recipe in recipes:
    if recipe['name'] == 'compute_df_prepared':
#         print(json.dumps(recipe,indent=4))
        recipe_handle = current_project.get_recipe(recipe['name'])
        settings = recipe_handle.get_settings()
        print("Recipe \'%s\' payload is \n %s" % (recipe['name'],settings.get_payload()))


# In[ ]:


# def test_coding_recipes_complexity(params):
#     client = dataikuapi.DSSClient(params["host"], params["api"])
#     client._session.verify = False
#     project = client.get_project(params["project"])

#             print(type(payload))

