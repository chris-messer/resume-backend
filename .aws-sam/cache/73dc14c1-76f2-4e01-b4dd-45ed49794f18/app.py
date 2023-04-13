import json
import logging
import os
import time
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    table = dynamodb.Table('visitor_count')
    timestamp = str(time.time())

    # item = {
    #     'id': 1,
    #     'last_visited': timestamp,
    #     'visitor_count': 1
    # }
    #
    # table.put_item(Item=item)

    try:
        response = table.update_item(
            Key={"id": '1'},
            UpdateExpression="set visitor_count = visitor_count + :n, last_visited = :ts",
            ExpressionAttributeValues={
                ":n": 1,
                ":ts": timestamp
            },
            ReturnValues="UPDATED_NEW",
        )
        #print(response["Attributes"])

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Record added!",
                #"item": item,
                "event": json.dumps(event),
                "response": str(response["Attributes"])
            }),
        }
    except Exception as err:
        return {
            "statusCode": 202,
            "body": json.dumps({
                "error": json.dumps(err)
            }),
        }