############################################################################################################################
#
# Program      : Platform Surveillance System
# Input        : Time interval and folder name through command line arguments
# Output       : System information and log file
# Functions    : ProcessScan(), PlatFormSurveillance(), main()
# Description  : Monitors CPU, RAM, network usage and running processes
#                and maintains the information in timestamped log files.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import time
import psutil
import sys
import os
import schedule

############################################################################################################################
#
# Function Name : ProcessScan
# Input         : Nothing
# Output        : List containing information about running processes
# Description   : Fetches information about currently running processes
#                 including PID, name, username, status, CPU and RAM usage.
#
############################################################################################################################

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=("pid", "name", "username", "status"))
        info["cpu_percent"] = proc.cpu_percent(None)
        info["ram_percent"] = proc.memory_percent()

        listprocess.append(info)

    return listprocess

############################################################################################################################
#
# Function Name : PlatFormSurveillance
# Input         : Folder name
# Output        : Creates a log file containing system information
# Description   : Collects CPU, RAM, network and process information
#                 and stores the details in a timestamped log file.
#
############################################################################################################################

def PlatFormSurveillance(FolderName):
    Border = "-" * 60
    Ret = False

    # Check whether the folder exists
    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)

        if(Ret == False):
            print("Unable to proceed as directory's name is existing but its not a directory.\n")
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created successfully.\n")

    # Generate timestamp for the log file
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, f"Platform_{timestamp}.log")

    fd = open(FileName, "w")

    print(f"Log file gets successfully created with name : {FileName}")

    # Write log file header
    fd.write(Border + "\n")
    fd.write("---------- Platform Surveillance System ---------\n")
    fd.write("Log file gets created at : " + timestamp + "\n")
    fd.write(Border + "\n\n")

    print("--------------------------  System Report -----------------------")

    fd.write(Border + "\n")
    fd.write(Border + "\n")

    # CPU Information
    cpu_percentage = psutil.cpu_percent()
    fd.write(f"CPU Usage     : {cpu_percentage} %\n")

    cpu_count = psutil.cpu_count()
    fd.write(f"Number of CPU Cores: {cpu_count} \n")

    fd.write(Border + "\n")
    fd.write(Border + "\n")

    # RAM Information
    ram = psutil.virtual_memory()

    fd.write(f"RAM Total     : {ram.total // (1024 * 1024)} MB\n")
    fd.write(f"RAM Used      : {ram.used // (1024 * 1024)} MB\n")
    fd.write(f"RAM Available : {ram.available // (1024 * 1024)} MB\n")
    fd.write(f"RAM Usage     : {ram.percent} %\n")

    fd.write(Border + "\n")
    fd.write(Border + "\n")

    # Network Information
    net = psutil.net_io_counters()

    fd.write("Network Usage\n")
    fd.write(f"Network Sent     : {net.bytes_sent // (1024 * 1024)} MB\n")
    fd.write(f"Network Received : {net.bytes_recv // (1024 * 1024)} MB\n")

    fd.write(Border + "\n")
    fd.write(Border + "\n")

    # Process Information
    Data = ProcessScan()

    for info in Data:
        fd.write(f"{info}" + "\n")
        fd.write(Border + "\n")

    fd.write(Border + "\n")

    print("-------------------------- End of Log File -----------------------")

    fd.write(Border + "\n")

    print("-------------------------- End of Log File -----------------------")

    fd.write(Border + "\n")

    fd.close()

############################################################################################################################
#
# Function Name : main
# Input         : Command line arguments
# Output        : Displays help information or starts scheduler
# Description   : Handles command line arguments and starts the
#                 Platform Surveillance System periodically.
#
############################################################################################################################

def main():
    Border = "-" * 60

    print(Border)
    print("---------- Platform Surveillance System -----------")
    print(Border)

    # Handle --h and --u command line arguments
    if(len(sys.argv) == 2):

        # Display help information
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform : ")
            print("1 : It fetches the information of running processes")
            print("2 : It fetches the information about the primary storage as RAM")
            print("3 : It fetches the information about the secondary storage as HDD")
            print("4 : It fetches the information about the microprocessor")
            print("5 : It gets auto scheduled periodically")
            print("6 : It maintains all records into the log file")
            print("7 : It sends the log file through mail periodically")

        # Display usage information
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"Python {sys.argv[0]} Time_Interval Folder_Name")

        else:
            print("Unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for getting more details")

    elif(len(sys.argv) == 3):
        print("Scheduler started successfully.")

        schedule.every(int(sys.argv[1])).seconds.do(
            PlatFormSurveillance,
            sys.argv[2]
        )

        while True:
            schedule.run_pending()
            time.sleep(1)

    # Handle invalid number of arguments
    else:
        print("Invalid number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("---------- Thank you for using our automation System ----------")
    print(Border)

############################################################################################################################
#
# Application : Platform Surveillance System
#
############################################################################################################################

if __name__ == "__main__":
    main()
