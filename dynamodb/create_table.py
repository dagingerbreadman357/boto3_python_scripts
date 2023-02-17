import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Title',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'Year',
            'AttributeType': 'N',
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'Title',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'Year',
            'KeyType': 'RANGE',
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1,
    },
    TableName='Favorite_Movies',
)

print(response)