from Crypto.Random import get_random_bytes
key = get_random_bytes(32)  # AES-256
iv = get_random_bytes(16)   #初始化向量

#print(key)
key1 = b'\x96\x99\xa8\xce_[\xc4\xf88TV\xfd%[\xa6\x8e\xc4\n\x87\x12\xf8\x88\\\xdc\x82\xb79,\x9d\xb3\x81\xc0'
key2 = b'g6\x01\xef3a>\x14\x92\x8c~i\xd0\xb4\x844\x86\xbd9\x08z\x1b\xde\xa0\xf3\xf4\xc8\xbdL\xbd\xcb\x8e'

iv1 = b'\xdd\xea\x88\xb1\xa4\xca\x81\xb9\xae503\xd6X`\xae'
iv2 = b'\xa4\xfeS\xdb7u\x82\xa4\xe2Y\x0b\xbb\xd1\x95x\x1f'

def to_Cpp_format(byte_string):
    cpp_array = "unsigned char AESkey[32] = {"
    cpp_array += ', '.join(f"0x{byte:02X}" for byte in byte_string)
    cpp_array += "};"
    print(cpp_array)

to_Cpp_format(iv1)