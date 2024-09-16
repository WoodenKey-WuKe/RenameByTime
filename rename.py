import os

# 获取当前目录下的所有文件和目录名
files = os.listdir('.')

# 过滤出所有的.py文件，并获取它们的修改时间
py_files = [(f, os.path.getmtime(f)) for f in files if f.endswith('.py')]

# 根据修改时间对文件进行排序
py_files.sort(key=lambda x: x[1])

# 初始化一个计数器
counter = 1

# 记录重命名的映射关系
renamed_files = {}

# 白名单文件，这些文件不会被重命名
whitelist = ['recall.py', os.path.basename(__file__)]

# 遍历排序后的文件列表
for filename, _ in py_files:
    # 检查文件是否在白名单中
    if filename in whitelist:
        continue
    # 分割文件名和扩展名
    name, ext = os.path.splitext(filename)
    # 构造新的文件名
    new_filename = f"{counter}_{name}{ext}"
    # 重命名文件
    os.rename(filename, new_filename)
    # 打印出被重命名的文件
    print(f"Renamed '{filename}' to '{new_filename}'")
    # 记录重命名的映射关系
    renamed_files[new_filename] = filename
    # 计数器递增
    counter += 1

# 将重命名的映射关系保存到一个文件中
with open('renamed_files_map.txt', 'w') as f:
    for new, old in renamed_files.items():
        f.write(f"{new} -> {old}\n")