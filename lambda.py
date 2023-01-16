import json
import mercadopago
import os


def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])

    payment_data = json.loads(event['body'])

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "status": payment['status'],
                "status_detail": payment['status_detail'],
                "payment_method": payment['payment_method'],
                "id": payment['id']
            }
        )
    }
