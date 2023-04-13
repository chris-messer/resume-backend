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




    response = {
        "headers": {
            "content-type": "application/json"
        },
        "status_code": 200,
        "body": {
            "count": int(data['Item']['visitor_count'])
        }
    }

    return response
