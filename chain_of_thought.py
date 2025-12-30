import json 
import boto3

# Configure AWS credentials and region
# Option 1: Use AWS CLI: aws configure
# Option 2: Set environment variables:
#   AWS_ACCESS_KEY_ID=your_access_key
#   AWS_SECRET_ACCESS_KEY=your_secret_key
#   AWS_DEFAULT_REGION=us-east-1
# Option 3: Use IAM roles (if running on EC2/Lambda)

# Specify region (required for Bedrock)
# Common regions: us-east-1, us-west-2, eu-west-1
client = boto3.client('bedrock-runtime')
prompt_data = """
On a given week, the viewers for a TV channel were
Monday: 6500 viewers
Tuesday: 6400 viewers
Wednesday: 6300 viewers


Question: How many viewers can we expect on Friday?
Answer: Based on the numbers given and without any more information, there is a daily decrease of 100 viewers. If we assume this trend will continue during the following days, we can expect 6200 viewers on the next day that would be Thursday, and therefore 6100 viewers on the next day that would be Friday.


Question: How many viewers can we expect on Saturday? (Think Step-by-Step)
Answer:
"""

response = client.invoke_model(
    modelId='amazon.nova-2-lite-v1:0',
    contentType='application/json',
    accept='application/json',
    body=json.dumps({
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt_data
                    }
                ]
            }
        ],
        "max_tokens": 50,
        "temperature": 1.0,
        "top_p": 0.9
    })
)
response_body = json.loads(response['body'].read())
print(response_body['content'][0]['text'])