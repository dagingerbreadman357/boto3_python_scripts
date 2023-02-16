import boto3

ec2 = boto3.client('ec2')

response = ec2.terminate_instances(InstanceIds=['i-095be12fde7102e4b', 'i-0be517061946c43b0', 'i-04ebacac145b1dfd9'])

print("EC2 instances Terminate")