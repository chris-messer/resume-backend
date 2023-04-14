import json
import boto3
from decimal import Decimal
import time
# import requests

dynamodb = boto3.resource('dynamodb')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


def lambda_handler(event, context):
    timestamp = str(time.time())
    table = dynamodb.Table('visitor_count')
    data = table.get_item(
        #TableName='your-table-name',
        Key={
            'id': '1'
        }
    )

    response = table.update_item(
        Key={"id": '1'},
        UpdateExpression="set visitor_count = visitor_count + :n, last_visited = :ts",
        ExpressionAttributeValues={
            ":n": 1,
            ":ts": timestamp
        },
        ReturnValues="UPDATED_NEW",
    )



    itemsObjectOnly = data["Item"]
    visitcount = itemsObjectOnly["visitor_count"]

    # response = {
    #     'statusCode': 200,
    #     'body': visitcount #json.dumps(data, cls=DecimalEncoder)
    #     }
    response = {'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'},
                'body': json.dumps({"count": visitcount},
                                   cls=DecimalEncoder)}


    return response
