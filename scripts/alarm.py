import boto3
import json
import sys



sns_compass = 'arn:aws:sns:ap-southeast-1:518778911925:Disk_Space_Alarm'
alarm_name = 'my_test_alarm'
client = boto3.client('cloudwatch', region_name="ap-southeast-1")

instance_id = sys.argv[1]
instance_name = sys.argv[2]


alarm = client.put_metric_alarm(AlarmName=instance_name + " DiskSpace",
        AlarmDescription=instance_name + " DiskSpace",
        MetricName='DiskSpaceUtilization',
        Namespace='System/Linux',
        Dimensions=[{
                'Name' : 'MountPath',
                'Value': "/"
            },{
        	'Name' : 'InstanceId',
        	'Value': instance_id
            
            },{
        	'Name' : 'Filesystem',
        	'Value': '/dev/xvda1'
            
            }
            ],
        Statistic='Average',
        ComparisonOperator='GreaterThanThreshold',
        Threshold=75,
        Period=300,
        EvaluationPeriods=5,
        ActionsEnabled=True,
        AlarmActions=[sns_compass],
        OKActions=[sns_compass],
        TreatMissingData='ignore')
