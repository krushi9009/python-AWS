import boto3
ec2=boto3.resource('ec2')
Instance=ec2.create_instances(
ImageId='ami-01e78c5619c5e68b4',
MinCount=1,
MaxCount=1,
InstanceType='t2.micro')
print(Instance[0].id);