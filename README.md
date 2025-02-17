# Log File Analyzer

A Python script to analyze log files, count log levels, and identify the top 5 most frequent error messages.

-log_Analyzer.py is main file that is used to find the information present in all log file.
-First_file.py is file used to find the information for the first log file

## Features
- Processes multiple log files concurrently.
- Counts log levels (INFO, WARNING, ERROR).
- Identifies the most frequent ERROR messages.

## Usage
- Place your log files in the `logs/` directory.
- Run the log_Analyzer.py to generate a `summary.csv` report(that is our solution)

## Requirements
- Python 3.10.2
- `concurrent.futures`, `re`, `csv`, `os`, `collections`
