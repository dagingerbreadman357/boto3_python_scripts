import boto3

dynamodb = boto3.client('dynamodb')


dynamodb.put_item(                                # adding items to the dynamodb table
    Item={
        'Title':{
          'S': 'Dennis the Menace'  ,
        },
        'Year': {
            'N': '1993',
        },
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='Favorite_Movies',
)

dynamodb.put_item(                                # adding items to the dynamodb table
    Item={
        'Title':{
          'S': 'Honey, I Shrunk the Kids'  ,
        },
        'Year': {
            'N': '1989',
        },
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='Favorite_Movies',
)

table_name = 'Favorite_Movies'                      # (optional) creating a variable to use in print statement

response = dynamodb.scan(                           # using the scan method to place items in a variable list
    TableName='Favorite_Movies')

print(response['Items'])                            # print 'Key' Items which should return a list of K/V pair for all items in list


