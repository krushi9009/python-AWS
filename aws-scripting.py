import boto3
ec2=boto3.resource('ec2')
instance=ec2.create_instances(
imageid='ami-054e49cb26c2fd312',
mincount=1,
maxcount=1,
instancetype='t2.micro')
print(instance[0].id)
