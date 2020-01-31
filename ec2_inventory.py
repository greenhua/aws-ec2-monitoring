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
        
	response = client.describe_instances(DryRun=False) #, Filters = [{ 'Name':'instance-state-code', 'Values': ['16']}])
        for i2 in response['Reservations']:
    	    for i in i2['Instances']:
    		#print(i)
    		tags = getTags(i['Tags'])
    		name = getTag(i['Tags'], "Name")
    		print(name + "\n")
    		ip = i['PublicIpAddress']
    		instanceid=i['InstanceId']
        
        	#hosts['list'].append( {'name':name, 'ip':ip, 'instanceId':instanceid})
		f.write("#" + name + "\n")
    		f.write(ip + " ansible_ssh_user=ec2-user istanceId=" + instanceid + " region=" + region + " tags=" + tags +"\n\n")




def getTag(tags, key):
    for tag in tags:
	if tag['Key'] == key:
	    return tag['Value']
    return false
    
def getTags(tags):
    tags_list = []
    for tag in tags:
	tags_list.append(tag['Key'])
    
    return ",".join(tags_list)   
    
        
main()