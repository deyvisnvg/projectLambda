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


# json que se envía desde el Postman
# No olvidar actualizar el clave "token" para hacer las pruebas
# {
#     "transaction_amount": 10,
#     "token": "0d03b31223fcb5f31c216bbc7d92096d",
#     "installments": 1,
#     "issuer_id": "12551",
#     "payment_method_id": "visa",
#     "payer": {
#         "email": "deyvisnvg00@gmail.com",
#         "identification": {
#             "type": "DNI",
#             "number": "48254628"
#         }
#     }
# }


# API GATEWAY
# https://3xbhdn5867.execute-api.us-east-2.amazonaws.com/default/mercadopago-api-a3
