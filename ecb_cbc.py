#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = AES.block_size


def decrypt(ciphertext: bytes) -> bytes:
    key = bytes.fromhex("2c4b295fe9ca7c02208e22d25e2875a8")
    cipher = AES.new(key, AES.MODE_ECB)

    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        print(f"ERROR: {e}")
        return -1

    return decrypted


def encrypt(plaintext: bytes) -> bytes:
    key = bytes.fromhex("2c4b295fe9ca7c02208e22d25e2875a8")
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    encrypted = cipher.encrypt(plaintext)
    ciphertext = iv + encrypted
    print(iv)

    return ciphertext


def get_plaintext(ciphertext: bytes):
    """
    the encytpted message uses the same key as the decryption function and the encryption function returns the ciphertext with the iv prepended.
    To get the plaintext we just need to use decrypt on each block of the ciphertext and XOR with the next block of ciphertext len(ciphertext)/BLOCK_SIZE) times.
    Since the IV is at the begining of the ciphertext using this algorithm will work.
    """
    # TODO: Replace this with your implementation
    
    message = b''
    for i in range(len(ciphertext),BLOCK_SIZE,-BLOCK_SIZE):
        temp = decrypt(ciphertext[i-BLOCK_SIZE:i])
        next = ciphertext[i-2*BLOCK_SIZE:i-BLOCK_SIZE]
        result = bytes(x ^ y for x, y in zip(temp, next))
        message = result + message

    return message 


       

if __name__ == "__main__":
    plaintext = b"comp2108_3cb_5uck5_4v01d_17!!!!!"
    ciphertext = encrypt(plaintext)
    print(b'cipher: '+ciphertext)
    decrypted = get_plaintext(ciphertext)
    print(b"decrpted: "+decrypted)
    assert decrypted == plaintext
