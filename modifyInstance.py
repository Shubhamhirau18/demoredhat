import boto3
ec2 = boto3.client('ec2', region_name='ap-south-1')

# Comment below function if this code isn't being used in a lambda function.
def lambda_handler(event, context):
    myinstance = ec2.describe_instances(Filters=[{'Name': 'tag:Event', 'Values': ['Castkom']}])
    for pythonins in myinstance['Reservations']:
      for Ids in pythonins['Instances']:
        list = Ids['InstanceId']
        print("==============================")
        # Stop the instance
        ec2.stop_instances(InstanceIds=[list])
        waiter=ec2.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[list])
        print(f"Stopped {list}")
        # Change the instance type
        ec2.modify_instance_attribute(InstanceId=list, Attribute='instanceType', Value='t2.small')
        print(f"Upgraded {list}")
        # Start the instance
        ec2.start_instances(InstanceIds=[list])
        print(f"Started {list}")
