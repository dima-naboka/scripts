import boto3
import logging
from botocore.exceptions import ClientError

def terminate_clusters(cluster_ids, emr_client):
    """
    Terminates a cluster. This terminates all instances in the cluster and cannot
    be undone. Any data not saved elsewhere, such as in an Amazon S3 bucket, is lost.

    :param cluster_id: The ID of the cluster to terminate.
    :param emr_client: The Boto3 EMR client object.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    try:
        for cluster_id in cluster_ids:
            emr_client.terminate_job_flows(JobFlowIds=[cluster_id])
            logger.info("Terminating cluster %s.", cluster_id)
    except ClientError:
        logger.exception("Couldn't terminate cluster %s.", cluster_id)
        raise


def get_long_running_clusters(emr_hours, emr_cluster_name, emr_client):
    """
    Helper to filter EMR clusters before termination
    
    :param emr_hours:'NormalizedInstanceHours' 
    :param emr_cluster_name:'Name'
    """
    clusters = emr_client.list_clusters(ClusterStates=['STARTING','BOOTSTRAPPING','RUNNING','WAITING'])
    list_of_long_running_clusters = []
    
    for cluster in clusters['Clusters']:
        if cluster['NormalizedInstanceHours'] >= emr_hours:
            if cluster['Name'] == emr_cluster_name:
                list_of_long_running_clusters.append(cluster['Id']) 
    return list_of_long_running_clusters
    
def lambda_handler(event, context):
    emr_client = boto3.client('emr')
    
    dss_cluster_ids = ['emr_with_s3','emr_hive_dima','njm-emr']
    nrmlz_inst_hrs = 48
    
    clusters = [get_long_running_clusters(nrmlz_inst_hrs,'DSS cluster id={} name={}'.format(dss_cluster_id,dss_cluster_id), emr_client) for dss_cluster_id in dss_cluster_ids]
    for cl in clusters:
        terminate_clusters(cl, emr_client)  
    
    # clusters = get_long_running_clusters(48,'DSS cluster id=emr_with_s3 name=emr_with_s3', emr_client)
    # terminate_clusters(clusters, emr_client)
    
