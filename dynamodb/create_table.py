import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.create_table(                # create dynamodb table w/ .create_table method. creating response variable is not necessary
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

print(response)                                     # prints variable to screen which shows output of table in a list (optional)

#print("Dyanmodb table created")                    # prints visual confirmation if code results in 0 (optional) 