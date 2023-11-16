# ECB-and-CBC

Demonstrating how ECB and CBC encryption works. 

# Encrypting our favourite penguin Tux 

Run penguin.py to encrypt Tux using ECB and CBC

![tux](https://github.com/Braeden-Cheung/ECB-and-CBC/assets/120347252/c34ac8a6-5236-499b-9168-02a2ec1df3da)

Encrypting Tux using ECB mode:

![ecb_tux](https://github.com/Braeden-Cheung/ECB-and-CBC/assets/120347252/9ab9d939-9f61-4300-87be-c7ef5ebed23e)

Encrypting Tux using CBC mode:

![cbc_tux](https://github.com/Braeden-Cheung/ECB-and-CBC/assets/120347252/1e7258ff-f4c5-445c-bbc0-f6911e1069e7)


Here you can see why ECB mode is not the best way to go for encryption. ECB is a block encryption that encrypts blocks with a key. Encrypting identical blocks gives identical cipher blocks. CBC is a better encryption mode as it uses an IV vector to XOR the first block and then chains subsequent plaintext blocks and XOR's them with the previous ciphertext blocks. This solves the ECB flaw of encrypting identical blocks.
