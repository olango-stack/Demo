import boto3

#open console programatrically
aws_management_console = boto3.session.Session(profile_name="default")
iam_console = aws_management_console.resource('iam') #open iam console


for each_user in iam_console.users.all():
    print(each_user.name)