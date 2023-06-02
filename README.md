# lambda_trigger_from_s3
configure an AWS Lambda function to trigger only when the S3 bucket receives a file named "&lt;file_name>" that is stored within a dynamic directory path.

## Introduction:
Configuring an AWS Lambda function to trigger specific actions when certain conditions are met for objects stored in an Amazon S3 bucket. The conditions involve checking the presence of a file with the name **_demo** and verifying the structure of the S3 bucket path.

## Scenario:
I have an S3 bucket called *"transend,*" Within this bucket, there are various directories, each identified by a unique RECORDS_ID. To trigger the Lambda function, the following conditions must be satisfied:

>The Lambda function should only trigger when a file named "_demo" is uploaded to the S3 bucket.
The file must be located within a specific directory path format: **s3://transend/EMR/data/RECORDS_ID/host_id=YYYYMMDD/.**

>The host_id parameter within the path should adhere to the date format, where the first four digits represent the year (e.g., "YYYY"), the next two digits represent the month (e.g., "MM"), and the final two digits represent the day (e.g., "DD").

>Although the **host_id** can represent any valid date, it must follow the format **"YYYYMMDD"** consistently.

## Question:
How can I configure an AWS Lambda function to trigger only when the S3 bucket "transend" receives a file named "_demo" that is stored within a directory path adhering to the format **s3://transend/EMR/data/RECORDS_ID/host_id=YYYYMMDD/**, where the "*host_id*" parameter represents any valid date but consistently follows the "YYYYMMDD" format?*

## Steps to execute:

1. Create a lambda and use the python function
2. Create a event in S3 bucket then
   ### Edit event notification
a.**General configuration**

   ![alt text](https://github.com/piyushanand3/lambda_trigger_from_s3/blob/main/Screenshot%20from%202023-06-02%2013-19-27.png?raw=true)
b.**Event types**

   ![alt text](https://github.com/piyushanand3/lambda_trigger_from_s3/blob/main/Screenshot%20from%202023-06-02%2013-19-44.png?raw=true)
c.**Destination**

   ![alt text](https://github.com/piyushanand3/lambda_trigger_from_s3/blob/main/Screenshot%20from%202023-06-02%2013-20-31.png?raw=true)