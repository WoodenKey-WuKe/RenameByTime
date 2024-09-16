# RenameByTime
这是一组：用于根据文件夹内的.py文件修改日期，进行重命名文件名称与撤回修改的Python脚本；
并且使用了映射map来实现撤销重命名.用途是在做Python学习或复习时，有需要按照练手/测试的.py脚本的创建时间进行编号的场景.

# 主要文件
rename.py：
实现修改当前文件夹内.py文件的文件名；
根据文件修改时间进行数字排序；
实现对rename.py和recall.py脚本的过滤；
实现生成了一个文件名映射map.
recall.py：
实现根据用rename.py生成的renamed_files_map.txt中的文件名映射，完成重命名任务的完美撤销.
renamed_files_map.txt：
由rename.py生成，用于存放文件名映射map；不用下载，我上传只是为了示例文件夹结构.

# 使用方法
1.将你要重命名的.py文件放在一个文件夹内，并保证其仍然拥有你所希望的时间特征（例如：我这里是文件修改时间）；
2.将该仓库内的rename.py和recall.py下载到你在“1.”中所使用的文件夹路径下；
3.尝试运行rename.py即可实现重命名工作，若要撤销可运行recall.py.

# 注意
renamed_files_map.txt不用下载，我上传只是为了示例文件夹结构；
欢迎进行测试，我知道这个脚本功能不够强大，但这只是一个特殊应用场景下的使用方案，希望可以给您提供帮助；
对文件名称进行修改可能会导致一系列难以预料的事情，因此尝试需谨慎，建议先备份后做实验，切勿直接使用，避免导致严重的后果！
