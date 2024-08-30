import json
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from datetime import date
import base64



def generate_private_key():
    private_key = rsa.generate_private_key(
    public_exponent = 65537,    
    key_size = 2048,
)
    return private_key

def generate_public_key(private_key):
    public_key = private_key.public_key()
    return public_key

def function_cryptographing_message(public_key):
    message = {
        "person_id":1,
        "name":"Alberto",
        "email":"albertocarvalho@gmail.com",
        "gender":"man",
        "birth_date":date(1999, 1, 30),  
        "address":"street slovenia, 123",
        "salary":1890.00,
        "cpf":"900.323.545-39"
    }

    # Convertendo a mensagem para uma string JSON e depois para bytes
    message_bytes = json.dumps(message).encode('utf-8')

    #mensagem criptografada
    message_cryptographed = public_key.encrypt(
        message_bytes,
        padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes. SHA256(),
                label=None
        ))

    # Convertendo a mensagem criptografada para string usando Base64
    message_cryptographed_str = base64.b64encode(message_cryptographed).decode('utf-8')
    return print("Mensagem criptografada:", message_cryptographed_str)

def function_descrypted_message(message_cryptographed_str,private_key):
    try:
        # Convertendo a string Base64 de volta para bytes
        message_cryptographed_bytes = base64.b64decode(message_cryptographed_str)

        # Descriptografando
        message_decrypted = private_key.decrypt(
            message_cryptographed_bytes,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
            )
        )

        # Convertendo de volta para dicionário
        message_dict = json.loads(message_decrypted.decode('utf-8'))
        print("Mensagem descriptografada:", message_dict)
        return message_dict
    except Exception as error:
        print("Was not possible to decrypt", error)
        return None
