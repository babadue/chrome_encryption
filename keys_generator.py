from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        # format=serialization.PrivateFormat.TraditionalOpenSSL,  #older pkcs1 format
        format=serialization.PrivateFormat.PKCS8,  # new pkcs8 format
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open("private_key.pem", "wb") as private_file:
        private_file.write(private_pem)
    with open("public_key.pem", "wb") as public_file:
        public_file.write(public_pem)

if __name__ == "__main__":
    generate_keys()