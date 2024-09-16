import os

# 读取重命名的映射关系
try:
    with open('renamed_files_map.txt', 'r') as f:
        renamed_files = {line.split(' -> ')[0].strip(): line.split(' -> ')[1].strip() for line in f.readlines()}
except FileNotFoundError:
    print("重命名映射文件未找到，请确保它位于同一目录下。")
    exit()

# 遍历映射关系并撤销重命名
for new_filename, old_filename in renamed_files.items():
    try:
        # 重命名文件
        os.rename(new_filename, old_filename)
        # 打印出被撤销重命名的文件
        print(f"Reverted '{new_filename}' to '{old_filename}'")
    except FileNotFoundError:
        print(f"文件 '{new_filename}' 不存在，无法撤销重命名。")
    except PermissionError:
        print(f"没有权限撤销 '{new_filename}' 的重命名。")
    except Exception as e:
        print(f"撤销 '{new_filename}' 的重命名时发生错误：{e}")