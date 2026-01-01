import json 
import boto3

"""
Zero-Shot: no examples are provided to the LLMs, think of it as if you were writing a multiple choice exam question, where the choices/test cases are going to be guessed by the LLM.
"""
client = boto3.client('bedrock-runtime')
prompt_data = """Generate test cases for this API endpoint:
HTTP method: POST
endpoint: /login
status code successful: 201
status code unsuccessful: 401
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