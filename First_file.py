import os
from collections import Counter

##this file is used to extract information for the first log file only
class LogAnalyzer:
    def __init__(self,file_path:str):

        self.file_path=file_path
        self.log_counter=Counter()

    def process_file(self)->None:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("file: {self.file_path} not found")
        try:
            with open(self.file_path, mode ='r') as file:
                for line in file:
                    new_line=line.strip()
                    if 'INFO' in new_line:
                        self.log_counter['INFO']+=1
                        print(f"info found,count:{self.log_counter['INFO']}")
                    if 'WARNING' in new_line:
                        self.log_counter['WARNING']+=1
                        print(f"warning found,count:{self.log_counter['WARNING']}")
                    if 'ERROR' in new_line:
                        self.log_counter['ERROR']+=1
                        print(f"error found,count:{self.log_counter['ERROR']}")
        except FileNotFoundError:
            print("filr not found")
           
        except Exception as e:
            print(f"An error occured: {e}")
    def print_summary(self):
        print("log count")
        for level,count in self.log_counter.items():
            print(f"{level} : {count}")
def main():
    print("hello")
    file_path="logs\server1.log"
    analyzer=LogAnalyzer(file_path)
    analyzer.process_file()
    analyzer.print_summary()
if __name__=='__main__':
    main()
