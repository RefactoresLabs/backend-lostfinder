from backend.app.infrastructure.security.bcrypt_hasher import BcryptHasher

def test_hash_and_verify_success():

    hasher = BcryptHasher()

    password = "12345"
    
    hashed_password = hasher.hash(password)

    assert hasher.verify(password, hashed_password) is True

def test_bcrypt_salt_generate_different_hashes():

    hasher = BcryptHasher()

    password = "12345"

    hash1 = hasher.hash(password)
    hash2 = hasher.hash(password)

    assert hash1 != hash2

def test_hash_returns_string():

    password = "12345"

    assert isinstance(
        BcryptHasher().hash(password),
        str
    )