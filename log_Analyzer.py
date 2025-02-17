#This is the main file that i have used to extract information from all log file

import os
import re
import csv
from collections import Counter
from concurrent.futures import ThreadPoolExecutor


class LogAnalyzer:
    def __init__(self, log_dir: str):
        self.log_dir = log_dir
        self.log_counter = Counter()
        self.error_messages = Counter()

    def process_file(self, file_path: str):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if '[INFO]' in line:
                        self.log_counter['INFO'] += 1
                    elif '[WARNING]' in line:
                        self.log_counter['WARNING'] += 1
                    elif '[ERROR]' in line:
                        self.log_counter['ERROR'] += 1
                        match = re.search(r'\[ERROR\] (.+)', line)
                        if match:
                            error_message = match.group(1).strip()
                            self.error_messages[error_message] += 1
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    def process_logs(self):
        if not os.path.exists(self.log_dir):
            raise FileNotFoundError(f"Directory {self.log_dir} not found")
        
        log_files = [os.path.join(self.log_dir, f) for f in os.listdir(self.log_dir) if f.endswith(".log")]
        
        with ThreadPoolExecutor() as executor:
            executor.map(self.process_file, log_files)

    def write_summary(self, output_file: str):
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Log Level", "Count"])
            for level, count in self.log_counter.items():
                writer.writerow([level, count])

            writer.writerow([])
            writer.writerow(["Error Message", "Count"])
            for error, count in self.error_messages.most_common(5):
                writer.writerow([error, count])

def main():
    log_dir = "logs"  # Folder containing log files
    output_file = "summary.csv"
    
    analyzer = LogAnalyzer(log_dir)
    analyzer.process_logs()
    analyzer.write_summary(output_file)
    print(f"Summary written to {output_file}")

if __name__ == '__main__':
    main()
