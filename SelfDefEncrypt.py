from EncryptMethod import *
from CommonMethod import *


encrypted_shellcode = xor_encrypt(buf)
encrypted_shellcode = SelfDefEncrypt(encrypted_shellcode)
encrypted_shellcode = Aes_encrypt(encrypted_shellcode)

cpp_code = to_cplusplus_format(encrypted_shellcode)

print(cpp_code)


