#The Docker file is a script used by Docker to create an image

#Start by saying what base image(AWS Python 3.11 runtime image) to use to build this image.
#This is the foundation of our container
FROM public.ecr.aws/lambda/python:3.11

#Include requirements file into the image.(It contains the "boto3" string)
#Place it within the directory where the Lambda function code should be.
COPY requirements.txt ${LAMBDA_TASK_ROOT}

#Include python handler file into image, place it within same dir as lambda code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

#Use the python package installer(pip) to install dependencies from requirements file
RUN pip install -r requirements.txt

CMD ["lambda_function.handler"
