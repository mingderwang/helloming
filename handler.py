import json
import random
import uuid
import time

def handle(event, context):
    result = json.dumps(
        {
            "id": str(uuid.uuid4()),
            "選號日期": time.strftime("%m/%d/%Y", time.localtime()) ,
            "可能中獎號碼": random.sample(range(10),3),
            "猜中機率": 0
        }, ensure_ascii=False)
    return {
        "body": result,
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        }
    }
