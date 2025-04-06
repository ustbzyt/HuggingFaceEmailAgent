import sys
import os

def remove_null_bytes(filepath):
    """
    Reads a file, removes null bytes, and writes the cleaned content back to the same file.

    Args:
        filepath (str): The path to the file to clean.
    """
    try:
        # --- 安全措施：先创建备份 ---
        backup_filepath = filepath + ".bak"
        print(f"创建备份文件: {backup_filepath}")
        with open(filepath, 'rb') as original_file, open(backup_filepath, 'wb') as backup_file:
            backup_file.write(original_file.read())
        # --- 备份结束 ---

        print(f"正在读取文件: {filepath}")
        # 以二进制模式读取文件内容
        with open(filepath, 'rb') as f:
            content = f.read()

        # 检查是否包含 null bytes
        if b'\x00' not in content:
            print(f"文件中未找到 Null bytes: {filepath}")
            # 如果不需要备份文件，可以删除它
            # os.remove(backup_filepath)
            # print(f"已删除备份文件: {backup_filepath}")
            return

        print("检测到 Null bytes，正在移除...")
        # 移除 null bytes (替换为空的 bytes)
        cleaned_content = content.replace(b'\x00', b'')

        print(f"正在将清理后的内容写回文件: {filepath}")
        # 以二进制模式写回清理后的内容到原文件
        with open(filepath, 'wb') as f:
            f.write(cleaned_content)

        print(f"成功从 {filepath} 移除 Null bytes。")
        print(f"原始文件已备份为: {backup_filepath}")

    except FileNotFoundError:
        print(f"错误: 文件未找到 {filepath}")
    except Exception as e:
        print(f"处理文件时发生错误: {e}")

if __name__ == "__main__":
    # 检查是否提供了命令行参数（文件名）
    if len(sys.argv) != 2:
        print("使用方法: python <脚本名称.py> <要清理的文件路径>")
        # 例如: python remove_nulls.py C:\Users\ustbz\20250404_BookAgent\main.py
        sys.exit(1) # 退出脚本，指示错误

    file_to_clean = sys.argv[1]
    remove_null_bytes(file_to_clean)