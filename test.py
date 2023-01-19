import os
from argparse import ArgumentParser


changes = 0

parser = ArgumentParser(
    prog="changes detector"
)
parser.add_argument("firstFilePath", action="store")
parser.add_argument("secondFilePath", action="store")


args = parser.parse_args('C:\\Users\\Lenovo\\Desktop\\mysite C:\\Users\\Lenovo\\Desktop\\mysite-Copy'.split())
first = args.firstFilePath
second = args.secondFilePath


first_dir_file = [[x[0],x[2]] for x in os.walk(first)]
second_dir_file = [[x[0],x[2]] for x in os.walk(second)]


for index, val in enumerate(first_dir_file):
    value = val[0]
    first_dir_file[index][0] = value.replace(first, '').replace('\\','/') + '/'

for index, val in enumerate(second_dir_file):
    value = val[0]
    second_dir_file[index][0] = value.replace(second, '').replace('\\','/') + '/'


first_dirs = [x[0] for x in first_dir_file]
second_dirs = [x[0] for x in second_dir_file]

for tup in first_dir_file:
        if tup[0] not in second_dirs:
            changes+=1
            print(f'Change #{changes}\n')
            print(f'{tup[0]} directory was removed:')
            for file in tup[1]:
                print(f'\t{file} file was removed')
            print('-'*50)
            first_dir_file.remove(tup)

for tup in second_dir_file:
        if tup[0] not in first_dirs:
            changes+=1
            print(f'Change #{changes}\n')
            print(f'{tup[0]} directory was added:')
            for file in tup[1]:
                print(f'\t{file} file was added')
            print('-'*50)
            second_dir_file.remove(tup)

first_files = []
second_files = []

for i in first_dir_file:
    first_files += i[1]
for i in second_dir_file:
    second_files += i[1]

for file in first_files:
    if file not in second_files:
        changes+=1
        print(f'Change #{changes}\n')
        print(f'{file} file was removed')
        print('-'*50)

for file in second_files:
    if file not in first_files:
        changes+=1
        print(f'Change #{changes}\n')
        print(f'{file} file was added')
        print('-'*50)


print('#'*50,'\t'*12,'Inner file changes\n')
for file in first_files:
    if file in second_files:
        print(file)
        file1, file2 = [],[]
        first_dirs+=['']
        second_dirs+=['']
        for i in first_dirs:
            try:    
                with open(first+'\\'+i+file) as f1:
                    for i in f1:
                        file1.append(i)
                break
            except:
                pass
        for i in second_dirs:
            try:
                with open(second+'\\'+i+file) as f2:
                    for i in f2:
                        file2.append(i)
                break
            except:
                pass
        cont = 0
        for i,v in enumerate(file1):
            try:
                if v!=file2[i]:
                    print(f'{i+1}) {v} -> {file2[i]}')
                cont = i
            except:
                print(f'{i+1}) {v} -> removed')
        try:
            while file2[cont+1]:
                cont+=1
                print(f'{cont+1}) {file2[cont]}       (new line)')
        except:
            pass
        print('='*50,'\n')

input()