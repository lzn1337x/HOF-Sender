# HOF Sender for OMSI 2

This project provides a simple Python script to facilitate the management of HOF files for OMSI 2, a popular bus simulation game. The script allows users to send HOF files to vehicle folders, delete HOF files from vehicle folders, and list the HOF files present in the HOF folder.

## Features

- **Send HOF Files:** Copy HOF files from the HOF folder to vehicle folders.
- **Delete HOF Files:** Remove all HOF files from vehicle folders.
- **List HOF Files:** Display the names of HOF files in the HOF folder and the total count.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) installed
- Dependencies are listed in `requirements.txt` and will be installed automatically.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lzn1337x/HOF-Sender.git
   ```

2. Navigate to the project directory:

   ```bash
   cd hof-sender
   ```

3. Update the `config.json` file with your OMSI 2 vehicle folder path. Open `config.json` and replace the `destination_folder` value with the path to your OMSI 2 vehicle folder. The default path is set for Steam installations:

   ```json
   {
      "destination_folder": "C:/Program Files (x86)/Steam/steamapps/common/OMSI 2/Vehicles"
   }
   ```

4. Run the batch file to install dependencies and execute the script:

   ```bash
   start.bat
   ```

   > **Note:** Ensure the batch file is in the same directory as your Python script.

### Usage

1. Follow the on-screen menu to choose an action:
   - Press `1` to send HOF files to vehicle folders.
   - Press `2` to delete all HOF files from vehicle folders.
   - Press `3` to list HOF files in the HOF folder.

2. For the send and delete actions, follow the prompts to complete the process.

3. After each action, the script will return to the main menu.

## Additional Notes

- For support or feedback, contact the project author: **@L Z N#6966**

---

*Project created by L Z N.*
