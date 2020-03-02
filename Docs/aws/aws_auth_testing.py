import boto3

region = 'us-west-2'
client = boto3.client('ec2',region_name='us-west-2', 
                        aws_access_key_id='AKIAID4B3YQIGVXGCP3Q',
                        aws_secret_access_key='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'
    )

images = client.describe_images(Owners=['self'])
print(images['Images'][0]['ImageId'])

s3 = boto3.client('s3', region_name='us-west-2', 
                        aws_access_key_id='AKIAID4B3YQIGVXGCP3Q',
                        aws_secret_access_key='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'
    )
s3r = boto3.resource('s3', region_name='us-west-2', 
                        aws_access_key_id='AKIAID4B3YQIGVXGCP3Q',
                        aws_secret_access_key='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'
    )
bucket_name = 'testbucket1293248523850923853'
location = {'LocationConstraint': region}
#s3.create_bucket(Bucket=bucket_name,
                        #CreateBucketConfiguration=location)
buckets = s3.list_buckets()
#print(buckets)
# response = client.export_image(
#     Description='string',
#     DiskImageFormat='VMDK',
#     DryRun=False,
#     ImageId=images['Images'][0]['ImageId'],
#     RoleName="tester_123",
#     S3ExportLocation={
#         'S3Bucket': bucket_name
#         #'S3Prefix': 'string'
#     },
# )
bucket = s3r.Bucket(bucket_name)
file_name = 'export-ami-0381eaa21e40e5593.vmdk'

#s3.download_file(bucket_name, 'export-ami-0381eaa21e40e5593.vmdk', 'export-ami-0381eaa21e40e5593.vmdk')

# for my_bucket_object in bucket.objects.all():
import tqdm
#     print(my_bucket_object)
def hook(t):
  def inner(bytes_amount):
    t.update(bytes_amount)
  return inner


path = "/tmp/{}".format(file_name)
file_object = s3r.Object(bucket_name, file_name)
filesize = file_object.content_length
with tqdm.tqdm(total=filesize, unit='B', unit_scale=True, desc=file_name) as t:
    s3.download_file(bucket_name, 'export-ami-0381eaa21e40e5593.vmdk', 'export-ami-0381eaa21e40e5593.vmdk',Callback=hook(t))
