import os
import shutil
import time
import ctypes
import json
import sys
import traceback
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def set_cmd_title(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        print(f'\033]0;{title}\007', end='', flush=True)

def update_cmd_title(action, hofs_loaded, successful_count, start_time):
    current_time = round(time.time() - start_time, 2)
    cmd_title = f"HOF SENDER | Action: {action} | HOFs Loaded: {hofs_loaded} | Successful: {successful_count} | Time Taken: {current_time}s"
    set_cmd_title(cmd_title)

def reset_cmd_title():
    set_cmd_title("HOF SENDER | Made by @L Z N#6966")

def get_hof_count(source_folder):
    source_path = os.path.join(os.path.dirname(__file__), source_folder)
    hof_files = [f for f in os.listdir(source_path) if f.endswith('.hof')]
    return len(hof_files)

def list_hofs(source_folder):
    source_path = os.path.join(os.path.dirname(__file__), source_folder)
    hof_files = [f for f in os.listdir(source_path) if f.endswith('.hof')]
    return hof_files

def load_config(file_path=os.path.abspath("config.json")):
    if os.path.exists(file_path):
        with open(file_path, "r") as config_file:
            return json.load(config_file)
    else:
        print(f"Config file not found at {file_path}. Using default values.")
        return {"source_folder": "hof", "destination_folder": r"C:\Program Files (x86)\Steam\steamapps\common\OMSI 2\Vehicles"}

def save_config(config, file_path="config.json"):
    with open(file_path, "w") as config_file:
        json.dump(config, config_file, indent=4)

def copy_hof_to_vehicles(source_folder, destination_folder, hofs_loaded, successful_count):
    # Load configuration
    config = load_config()

    # Get the count of HOF files in the source folder
    hof_count = get_hof_count(config["source_folder"])

    # Get the full path to the source .hof files
    source_path = os.path.join(os.path.dirname(__file__), config["source_folder"])

    # Get a list of all .hof files in the source folder
    hof_files = [f for f in os.listdir(source_path) if f.endswith('.hof')]

    # Initialize a list to store successfully sent vehicles
    sent_vehicles = []

    # Record the start time
    start_time = time.time()

    # Clear the console
    clear_console()

    # Iterate through each vehicle folder in the destination
    for vehicle_folder in os.listdir(config["destination_folder"]):
        vehicle_path = os.path.join(config["destination_folder"], vehicle_folder)

        # Check if it's a directory
        if os.path.isdir(vehicle_path):
            # Copy each .hof file to the vehicle folder
            for hof_file in hof_files:
                destination_path = os.path.join(vehicle_path, hof_file)

                # Check if the .hof file doesn't already exist in the destination folder
                if not os.path.exists(destination_path):
                    try:
                        shutil.copy(os.path.join(source_path, hof_file), destination_path)
                        sent_vehicles.append(vehicle_folder)
                        print(f"{Fore.GREEN}[OK] Successfully sent {hof_count} HOF file(s) to {vehicle_folder}")
                        successful_count += 1
                    except Exception as e:
                        print(f"{Fore.RED}[ERROR] Failed to copy {hof_file} to {vehicle_folder}: {e}")
                else:
                    print(f"{Fore.YELLOW}[SKIP] {hof_file} already exists in {vehicle_folder}")
                update_cmd_title("Sending", hofs_loaded, successful_count, start_time)
                print(f"{Fore.CYAN}[INFO] Copying {hof_file} to {vehicle_folder}")

    # Print success message
    if sent_vehicles:
        print(f"\n{Fore.GREEN}[SUCCESS] Successfully sent HOF file(s) to {len(sent_vehicles)} vehicle folders{Style.RESET_ALL}")
        time.sleep(5)  # Pause for 5 seconds
    else:
        print(f"{Fore.YELLOW}[WARNING] No HOF files sent.{Style.RESET_ALL}")
        time.sleep(5)  # Pause for 5 seconds

    # Update CMD title
    update_cmd_title("Sending", hof_count, successful_count, start_time)

    # Reset CMD title
    reset_cmd_title()

def delete_all_hof_files(destination_folder, hofs_loaded, successful_count):
    # Load configuration
    config = load_config()

    # Get the count of HOF files in the source folder
    hof_count = get_hof_count(config["source_folder"])

    # Get the full path to the destination folder
    destination_path = os.path.join(os.path.dirname(__file__), config["destination_folder"])

    # Initialize a variable to count the number of cleared folders
    cleared_folders_count = 0

    # Record the start time
    start_time = time.time()

    # Clear the console
    clear_console()

    # Iterate through each vehicle folder in the destination
    for vehicle_folder in os.listdir(destination_path):
        vehicle_path = os.path.join(destination_path, vehicle_folder)

        # Check if it's a directory
        if os.path.isdir(vehicle_path):
            # Get a list of all .hof files in the vehicle folder
            hof_files = [f for f in os.listdir(vehicle_path) if f.endswith('.hof')]

            # Delete each .hof file from the vehicle folder
            for hof_file in hof_files:
                file_path = os.path.join(vehicle_path, hof_file)

                # Check if the .hof file exists in the destination folder
                if os.path.exists(file_path):
                    try:
                        os.remove(file_path)
                        cleared_folders_count += 1
                        print(f"{Fore.GREEN}[OK] Successfully deleted {hof_file} from {vehicle_folder}")
                        successful_count += 1
                    except Exception as e:
                        print(f"{Fore.RED}[ERROR] Failed to delete {hof_file} from {vehicle_folder}: {e}")
                else:
                    print(f"{Fore.RED}[SKIP] {hof_file} does not exist in {vehicle_folder}")
                update_cmd_title("Deleting", hofs_loaded, successful_count, start_time)
                print(f"{Fore.CYAN}[INFO] Deleting {hof_file} from {vehicle_folder}")

            # Check if the folder had no HOF files
            if not hof_files:
                print(f"{Fore.CYAN}[INFO] No HOF files found in {vehicle_folder}")

    # Print success message
    if cleared_folders_count > 0:
        print(f"\n{Fore.GREEN}[SUCCESS] Successfully cleared HOF file(s) from {cleared_folders_count} vehicle folders{Style.RESET_ALL}")
        time.sleep(5)  # Pause for 5 seconds
    else:
        print(f"{Fore.YELLOW}[WARNING] No HOF files cleared.{Style.RESET_ALL}")
        time.sleep(5)  # Pause for 5 seconds

    # Update CMD title
    update_cmd_title("Deleting", hof_count, successful_count, start_time)

    # Reset CMD title
    reset_cmd_title()

def list_hofs_menu(hofs_loaded):
    # Load configuration
    config = load_config()

    # Get the count of HOF files in the source folder
    hof_count = get_hof_count(config["source_folder"])

    # Get the list of HOF files
    hof_files = list_hofs(config["source_folder"])

    clear_console()

    print(f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}List of HOF Files ({hof_count} HOFs Loaded)\n")
    for hof_file in hof_files:
        print(hof_file)
    print(f"\n{Fore.LIGHTYELLOW_EX}Press Enter to return to the main menu.{Style.RESET_ALL}")

    # Update CMD title
    set_cmd_title(f"HOF SENDER | HOFs Loaded: {hofs_loaded}")

    # Wait for user input before returning to the main menu
    input()

    # Reset CMD title
    reset_cmd_title()

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_menu():
    clear_console()

    print(f"""
{Fore.LIGHTWHITE_EX}{Style.BRIGHT}   _    _  ____  ______    _____ ______ _   _ _____  ______ _____  
  | |  | |/ __ \|  ____|  / ____|  ____| \ | |  __ \|  ____|  __ \ 
  | |__| | |  | | |__    | (___ | |__  |  \| | |  | | |__  | |__) |
  |  __  | |  | |  __|    \___ \|  __| | . ` | |  | |  __| |  _  / 
  | |  | | |__| | |       ____) | |____| |\  | |__| | |____| | \ \ 
  |_|  |_|\____/|_|      |_____/|______|_| \_|_____/|______|_|  \_\

  {Fore.LIGHTYELLOW_EX}HOF File Sender for OMSI 2 by {Fore.LIGHTWHITE_EX}@L Z N#6966

  {Fore.LIGHTYELLOW_EX}1. {Fore.LIGHTWHITE_EX}Send HOF files to Vehicles
  {Fore.LIGHTYELLOW_EX}2. {Fore.LIGHTWHITE_EX}Delete all HOF files from Vehicles
  {Fore.LIGHTYELLOW_EX}3. {Fore.LIGHTWHITE_EX}List HOF files
  {Fore.LIGHTYELLOW_EX}4. {Fore.LIGHTWHITE_EX}Exit
{Style.RESET_ALL}""")

if __name__ == "__main__":
    config = load_config()
    hofs_loaded = get_hof_count(config["source_folder"])
    successful_count = 0

    # Set CMD title
    reset_cmd_title()

    try:
        while True:
            print_menu()
            choice = input(f"{Fore.CYAN}Enter your choice (1, 2, 3, or 4): {Style.RESET_ALL}")

            if choice == "1":
                copy_hof_to_vehicles(config["source_folder"], config["destination_folder"], hofs_loaded, successful_count)
                hofs_loaded = get_hof_count(config["source_folder"])
            elif choice == "2":
                delete_all_hof_files(config["destination_folder"], hofs_loaded, successful_count)
                hofs_loaded = get_hof_count(config["source_folder"])
            elif choice == "3":
                list_hofs_menu(hofs_loaded)
            elif choice == "4":
                print(f"{Fore.LIGHTWHITE_EX}Exiting HOFSENDER. Goodbye!{Style.RESET_ALL}")
                time.sleep(1)  # Pause for 1 second before exiting
                break
            else:
                print(f"{Fore.RED}Invalid choice. Please enter 1, 2, 3, or 4.{Style.RESET_ALL}")
                time.sleep(2)  # Pause for 2 seconds after displaying error message
    except KeyboardInterrupt:
        print(f"{Fore.LIGHTWHITE_EX}\nExiting HOFSENDER. Goodbye!{Style.RESET_ALL}")
    except Exception as e:
        # Print traceback to error.log file
        with open("error.log", "w") as error_log:
            traceback.print_exc(file=error_log)

        print(f"{Fore.RED}\nAn error occurred. Details have been saved to error.log.{Style.RESET_ALL}")
        time.sleep(5)  # Pause for 5 seconds before exiting