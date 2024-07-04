import secrets

def generate_jwt_secret_key():
    # Generate a 32-byte secure random key
    key = secrets.token_hex(32)  # 32 bytes = 64 hex characters
    print(f"Your JWT Secret Key is:\n{key}")

if __name__ == "__main__":
    generate_jwt_secret_key()
