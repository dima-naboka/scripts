import dataiku
import json
#set_remote_dss() is required for scipting i.e. run from shell
dataiku.set_remote_dss("http://localhost:12000/", "T3N4PB79T7IB7KEMQYSCMTZPAH5YX210")
client = dataiku.api_client()

eng_params = {
 'aclSynchronizationMode': 'NONE',
 'clearMode': 'DSS_USER',
 'customPropertiesProviderParams': [],
 'dkuProperties': [],
 'extraConf': [],
 'hiveSynchronizationMode': 'KEEP_IN_SYNC',
 'namingRule': {'hdfsPathDatasetNamePrefix': '${projectKey}/',
  'hiveDatabaseName': 'eng_db',
  'tableNameDatasetNamePrefix': '${projectKey}_',
  'uploadsPathPrefix': 'uploads'},
 'overridePreCreateManagedDatasetFolderBeforeMetastoreSyncForRecipes': False,
 'root': '/data/eng'
}

datateam_params = {
 'aclSynchronizationMode': 'NONE',
 'clearMode': 'DSS_USER',
 'customPropertiesProviderParams': [],
 'dkuProperties': [],
 'extraConf': [],
 'hiveSynchronizationMode': 'KEEP_IN_SYNC',
 'namingRule': {'hdfsPathDatasetNamePrefix': '${projectKey}/',
  'hiveDatabaseName': 'data_team_db',
  'tableNameDatasetNamePrefix': '${projectKey}_',
  'uploadsPathPrefix': 'uploads'},
 'overridePreCreateManagedDatasetFolderBeforeMetastoreSyncForRecipes': False,
 'root': '/data/data_team'
}

eng_connection_def = {
 'allowManagedDatasets': True,
 'allowManagedFolders': True,
 'allowWrite': True,
 'allowedGroups': ['engineers'],
 'credentialsMode': 'GLOBAL',
 'customBasicConnectionCredentialProviderParams': [],
 'customFields': {},
 'detailsReadability': {'allowedGroups': ['engineers'],
  'readableBy': 'ALLOWED'},
 'indexingSettings': {'indexForeignKeys': False,
  'indexIndices': False,
  'indexSystemTables': False},
 'maxActivities': 0,
 'name': 'hdfs_engineers',
 'params': {'aclSynchronizationMode': 'NONE',
  'clearMode': 'DSS_USER',
  'customPropertiesProviderParams': [],
  'dkuProperties': [],
  'extraConf': [],
  'hiveSynchronizationMode': 'KEEP_IN_SYNC',
  'namingRule': {'hdfsPathDatasetNamePrefix': '${projectKey}/',
   'hiveDatabaseName': 'eng_db',
   'tableNameDatasetNamePrefix': '${projectKey}_',
   'uploadsPathPrefix': 'uploads'},
  'overridePreCreateManagedDatasetFolderBeforeMetastoreSyncForRecipes': False,
  'root': '/data/eng'},
 'type': 'HDFS',
 'usableBy': 'ALLOWED',
 'useGlobalProxy': False
}

datateam_connection_def = {
 'allowManagedDatasets': True,
 'allowManagedFolders': True,
 'allowWrite': True,
 'allowedGroups': ['data_team'],
 'credentialsMode': 'GLOBAL',
 'customBasicConnectionCredentialProviderParams': [],
 'customFields': {},
 'detailsReadability': {'allowedGroups': ['data_team'],
  'readableBy': 'ALLOWED'},
 'indexingSettings': {'indexForeignKeys': False,
  'indexIndices': False,
  'indexSystemTables': False},
 'maxActivities': 0,
 'name': 'hdfs_data_team',
 'params': {'aclSynchronizationMode': 'NONE',
  'clearMode': 'DSS_USER',
  'customPropertiesProviderParams': [],
  'dkuProperties': [],
  'extraConf': [],
  'hiveSynchronizationMode': 'KEEP_IN_SYNC',
  'namingRule': {'hdfsPathDatasetNamePrefix': '${projectKey}/',
   'hiveDatabaseName': 'data_team_db',
   'tableNameDatasetNamePrefix': '${projectKey}_',
   'uploadsPathPrefix': 'uploads'},
  'overridePreCreateManagedDatasetFolderBeforeMetastoreSyncForRecipes': False,
  'root': '/data/data_team'},
 'type': 'HDFS',
 'usableBy': 'ALLOWED',
 'useGlobalProxy': False
}

eng_connection = client.create_connection('hdfs_engineers', type='HDFS', params=eng_params, usable_by='ALLOWED', allowed_groups=['engineers'])
eng_connection.set_definition(eng_connection_def)
datateam_connection = client.create_connection('hdfs_data_team', type='HDFS', params=datateam_params, usable_by='ALLOWED', allowed_groups=['data_team'])
datateam_connection.set_definition(datateam_connection_def)
