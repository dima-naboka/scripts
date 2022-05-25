def do(payload, config, plugin_config, project_key):
    
    #project_key = project_key
    config = config
    plugin_config = plugin_config
    print("plugin config : ", plugin_config)
    print(" p : ", payload, " and pk : ", project_key, " and config : ", config )
    
    
    remote_host = plugin_config.get("host_url", "")
    if remote_host == "":
        raise Exception("destination is required")
    
    api_key = plugin_config.get("admin_api_key", "")
    if api_key == "":
        raise Exception("API key is required")
        
    client = dataikuapi.DSSClient(remote_host, api_key)  
    project = client.get_project(project_key)
        
    bundles_dict = project.list_exported_bundles()
    
    choices = [] 
    
    for bundle in bundles_dict['bundles'][0]:
        
        bun_id = bundle['bundleId']
        print("bundle_id : ",bun_id)
        
        bun_dict = { "value" : bun_id, "label" : bun_id }
        choices.append(bun_dict)       
    
     
    return {"choices": choices}