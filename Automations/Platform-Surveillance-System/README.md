# Platform Surveillance System

A Python automation project that monitors system resources and running
processes and periodically stores the collected information in log files.

## Features

- CPU usage monitoring
- CPU core information
- RAM usage monitoring
- Network usage monitoring
- Running process information
- Process CPU usage
- Process RAM usage
- Automatic log file generation
- Periodic execution using scheduler
- Command-line argument support

## Technologies Used

- Python
- psutil
- schedule

## How It Works

The program periodically collects information about the system and
running processes.

The collected information is stored in a timestamped log file inside
the folder provided by the user.

## How to Run

```bash
python PlatformSurveillance.py Time_Interval Folder_Name
