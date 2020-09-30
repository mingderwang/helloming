import json
import random

def handle(event, context):
    result = json.dumps({"可能中獎號碼": random.sample(range(10),3)}, ensure_ascii=False)
    return {
        "body": result,
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        }
    }
