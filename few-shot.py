import json 
import boto3

"""
Few-shot: some examples expected are provided for the model to know what type of response is required.
"""
client = boto3.client('bedrock-runtime')
prompt_data = """
Test cases for the /login API endpoint:

Test case 1: Valid credentials email and password
Test case 2: Invalid credentias email and password
Test case 3: Invalid email, valid password
Test case 4: invalid password, valid email
Test case 5: Missing password, valid email
test case 6: Missing email, valid password
test case 7: missing both email and passsword
test case 8:
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