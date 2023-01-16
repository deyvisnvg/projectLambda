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
        "body": {
            "status": payment['status'],
            "status_detail": payment['status_detail'],
            "id": payment['id'],
            "payment_method": payment['payment_method'],

        }
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

# URL LAMBDA
# https://6lid6lbrzrilv4crc2dhthah2y0qkuxc.lambda-url.us-east-2.on.aws/default/mercadopago-api-a3
