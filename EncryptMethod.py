from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

import random
import time


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

# def generate_substitution_table():
#     """生成随机字节替换表"""
#     table = list(range(256))
#     random.shuffle(table)
#     return table

def nonlinear_transform(byte):
    """简单的非线性变换"""
    return (byte * 37 + 113) % 256

def xor_with_key(byte, key):
    """使用固定密钥进行异或加密"""
    return byte ^ key

def swap_bytes(data):
    """打乱字节顺序：将奇数位和偶数位互换"""
    swapped = bytearray(data)
    for i in range(0, len(swapped) - 1, 2):
        swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
    return swapped

def SelfDefEncrypt(data):
    key = 0xBB
    """加密数据"""
    # substitution_table = generate_substitution_table()  # 生成替换表
    encrypted = bytearray()

    for byte in data:
        # byte = substitution_table[byte]  # 字节替换
        byte = nonlinear_transform(byte)  # 非线性变换
        byte = xor_with_key(byte, key)  # 固定密钥异或加密
        encrypted.append(byte)

    encrypted = swap_bytes(encrypted)  # 打乱字节顺序
    return encrypted

