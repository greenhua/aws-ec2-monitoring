import boto3
import json
import sys



def main():
    regions = []
    args = sys.argv
    args.pop(0)
    regions = args
    if len(regions) == 0 :
	regions = ['eu-west-1']

    print(regions)
    
    hosts = {'list':[]}
    for region in regions:
        client = boto3.client('ec2', region_name=region)
	f = open("hosts","w+")
        
	response = client.describe_instances(DryRun=False, Filters = [{ 'Name':'instance-state-code', 'Values': ['16']}])
        for i in response['Reservations']:
    	    name = getTag(i['Instances'][0]['Tags'], "Name")
    	    ip = i['Instances'][0]['PublicIpAddress']
    	    instanceid=i['Instances'][0]['InstanceId']
        
            #hosts['list'].append( {'name':name, 'ip':ip, 'instanceId':instanceid})
	    f.write("#" + name + "\n")
    	    f.write(ip + " ansible_ssh_user=ec2-user istanceId=" + instanceid + " region=" + region + "\n\n")




def getTag(tags, key):
    for tag in tags:
	if tag['Key'] == key:
	    return tag['Value']
    return false
    
    
main()