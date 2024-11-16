

def to_csharp_format(encrypted_shellcode):
    # 将加密后的 shellcode 转换为 C# 格式
    csharp_code = "using System;\nusing System.Text;\n\nclass Program \n"

    csharp_code += "byte[] shellcode = new byte[] { "

    # 输出每个字节的十六进制表示
    csharp_code += ", ".join(f"0x{byte:02X}" for byte in encrypted_shellcode)
    csharp_code += " ;\n"

    return csharp_code

def to_cplusplus_format(encrypted_shellcode):
    cpp_shellcode = ', '.join(f'0x{byte:02X}' for byte in encrypted_shellcode)
    cpp_code = f'BYTE encryptedShellcode[] = {{ {cpp_shellcode} }};'
    return cpp_code