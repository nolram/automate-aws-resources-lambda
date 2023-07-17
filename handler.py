import boto3

def turn_off_ec2(event, context):
    # Create EC2 client
    ec2 = boto3.client('ec2')
    
    # Get all EC2 instances
    response = ec2.describe_instances()
    
    instances = []
    
    # Loop through reservations and instances
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)
    
    # Filter instances with 'turnOff=true' tag
    instances_to_turn_off = []
    for instance in instances:
        tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
        if tags.get('turnOff') == 'true':
            instances_to_turn_off.append(instance['InstanceId'])
    
    # Turn off instances
    if instances_to_turn_off:
        ec2.stop_instances(InstanceIds=instances_to_turn_off)
        print(f"Turned off the following instances: {', '.join(instances_to_turn_off)}")
    else:
        print("No instances to turn off.")

def turn_on_ec2(event, context):
    # Create EC2 client
    ec2 = boto3.client('ec2')
    
    # Get all EC2 instances
    response = ec2.describe_instances()
    
    instances = []
    
    # Loop through reservations and instances
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)
    
    # Filter instances with 'turnOff=true' tag
    instances_to_turn_off = []
    for instance in instances:
        tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
        if tags.get('turnOff') == 'true':
            instances_to_turn_off.append(instance['InstanceId'])
    
    # Turn off instances
    if instances_to_turn_off:
        ec2.start_instances(InstanceIds=instances_to_turn_off)
        print(f"Turned on the following instances: {', '.join(instances_to_turn_off)}")
    else:
        print("No instances to turn off.")


def turn_off_rds(event, context):
    # Create RDS client
    rds = boto3.client('rds')
    
    # Get all RDS instances
    response = rds.describe_db_instances()
    
    instances_to_turn_off = []
    
    # Loop through instances
    for instance in response['DBInstances']:
        tags = {tag['Key']: tag['Value'] for tag in instance.get('TagList', [])}
        if tags.get('turnOff') == 'true':
            instances_to_turn_off.append(instance['DBInstanceIdentifier'])
    
    # Turn off instances
    if instances_to_turn_off:
        for i in instances_to_turn_off:
            rds.stop_db_instance(DBInstanceIdentifier=i)
        print(f"Turned off the following RDS instances: {', '.join(instances_to_turn_off)}")
    else:
        print("No RDS instances to turn off.")

def turn_on_rds(event, context):
    # Create RDS client
    rds = boto3.client('rds')
    
    # Get all RDS instances
    response = rds.describe_db_instances()
    
    instances_to_turn_off = []
    
    # Loop through instances
    for instance in response['DBInstances']:
        tags = {tag['Key']: tag['Value'] for tag in instance.get('TagList', [])}
        if tags.get('turnOff') == 'true':
            instances_to_turn_off.append(instance['DBInstanceIdentifier'])
    
    # Turn off instances
    if instances_to_turn_off:
        for i in instances_to_turn_off:
            rds.start_db_instance(DBInstanceIdentifier=i)
        print(f"Turned on the following RDS instances: {', '.join(instances_to_turn_off)}")
    else:
        print("No RDS instances to turn off.")