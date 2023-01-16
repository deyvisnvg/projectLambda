# Proyecto Silabuz Unidad 6

Proyecto final de la Unidad 6

## API endpoint de función Mercado Pago

API endpoint: [API Gateway](https://3xbhdn5867.execute-api.us-east-2.amazonaws.com/default/mercadopago-api-a3)

```bash
https://3xbhdn5867.execute-api.us-east-2.amazonaws.com/default/mercadopago-api-a3
```

### JSON que se envía desde el Postman. No olvidar actualizar la clave "token" para hacer las pruebas.

```bash
{
    "transaction_amount": 10,
    "token": "0d03b31223fcb5f31c216bbc7d92096d",
    "installments": 1,
    "issuer_id": "12551",
    "payment_method_id": "visa",
    "payer": {
        "email": "deyvisnvg00@gmail.com",
        "identification": {
            "type": "DNI",
            "number": "48254628"
        }
    }
}
```
