import boto3

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

def extract_entities(text):

    response = client.converse(
        modelId="deepseek.v3.2",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": f"""
Extract the entities from the following text.

Return ONLY valid JSON in this format:

{{
  "persons": [],
  "organizations": [],
  "locations": [],
  "dates": [],
  "emails": [],
  "phone_numbers": []
}}

Do not include explanations or markdown.
If an entity type is not present, return an empty array.

Text:
{text}
"""
                    }
                ]
            }
        ],
        inferenceConfig={
            "temperature": 0
        }
    )

    return response["output"]["message"]["content"][0]["text"]