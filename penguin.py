#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = AES.block_size
from Crypto.Util.Padding import pad, unpad

def ecb_penguin(key: bytes, img: bytes) -> bytes:
    """
    bmp file has header length of 54, performed slicing of img to get header, and body. 
    Perform padding to deal with trailing bytes in the block and finally encrypt the body that has been padded. Return the header and encrypted body.
    The encrypted penguin looks like that because blocks that are the same when encrypted look exactly the same.  

    """
    # TODO: Replace this with your implementation
    header_length = 54

    header = img[:header_length]
    body = img[header_length:]

    padded_body = pad(body, BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_body = cipher.encrypt(padded_body)

    final_image = header + encrypted_body

    return final_image
 


def cbc_penguin(key: bytes, iv: bytes, img: bytes) -> bytes:
    """
    same implementation as the ECB penguin but instead using CBC. The encrypted penguin looks like this because the first block is encrypted and XOR with the IV.
    Every proceding block that is encrpyted is XOR with the previous block, thus identical blocks will not be identical when encrypted.
    """
    assert iv is not None
    # TODO: Replace this with your implementation

    header_length = 54
    header = img[:header_length]
    body = img[header_length:]
    padded_body = pad(body,BLOCK_SIZE)
    cipher = AES.new(key,AES.MODE_CBC,iv)
   
    encrypted_body = cipher.encrypt(padded_body)
    final_image = header + encrypted_body
    
    return final_image 

if __name__ == "__main__":
    key = b"2108SaysAvoidECT"

    with open("tux.bmp", "rb") as f:
        img = f.read()

    with open("ecb_tux.bmp", "wb") as f:
        ciphertext = ecb_penguin(key, img)
        f.write(ciphertext)

    #  TODO: Uncomment below for cbc_penguin()
    iv = get_random_bytes(BLOCK_SIZE)
    with open("cbc_tux.bmp", "wb") as f:
        ciphertext = cbc_penguin(key, iv, img)
        f.write(ciphertext)
