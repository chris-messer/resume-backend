import json
import boto3
from decimal import Decimal
# import requests

dynamodb = boto3.resource('dynamodb')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


def lambda_handler(event, context):
    table = dynamodb.Table('visitor_count')
    data = table.get_item(
        #TableName='your-table-name',
        Key={
            'id': '1'
        }
    )

    itemsObjectOnly = data["Item"]
    visitcount = itemsObjectOnly["visitor_count"]

    # response = {
    #     'statusCode': 200,
    #     'body': visitcount #json.dumps(data, cls=DecimalEncoder)
    #     }
    response = {'statusCode': 200,
                'body': json.dumps({"count": visitcount},
                                   cls=DecimalEncoder)}


    return response
