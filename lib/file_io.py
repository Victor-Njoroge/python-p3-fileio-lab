def write_file(file_name="/home/victor/python-p3-fileio-lab/lib/text.txt", file_content="Log 1: 5 bananas added"):
    with open(file_name, mode='w', encoding='utf-8') as log_file:
        log_file.write(file_content)
#write_file()

def append_file(file_name="/home/victor/python-p3-fileio-lab/lib/text.txt", append_content="Log 2: 3 bananas subtracted"):
    with open(file_name, mode='a', encoding='utf-8') as log_file:
        log_file.write(append_content)
#append_file()

def read_file(file_name="/home/victor/python-p3-fileio-lab/lib/text.txt"):
    with open(file_name, mode='r', encoding='utf-8')as log_file:
        for line in log_file:
            print(line)
read_file()