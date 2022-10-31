from hashlib import sha256


def encrypt_password(password):
    return sha256(password.encode()).hexdigest()
