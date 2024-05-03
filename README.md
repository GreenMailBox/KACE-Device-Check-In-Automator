# Force Device Check-In Script

This script is designed to force devices with outdated KACE agents to check into the KACE server. It reads a CSV file containing device information, pings each device to check its status, and if the device responds, it runs commands to update the device's information on the KACE server.

## Usage

1. Ensure that Python is installed on your system.
2. Install the necessary modules by running `pip install -r requirements.txt`.
3. Run the script by executing `python force_check_in.py`.
4. Follow the on-screen instructions, if any.

## Dependencies

- Python 3.x
- CSV module
- OS module
- Sys module
- Getpass module
- Datetime module

## Instructions

1. Update the `devices.csv` file with the relevant device information.
2. Ensure that the paths to `runkbot.exe` and `AMPTools.exe` are correctly set in the script.
3. Run the script with appropriate permissions.

## Contributors

- [Your Name]

## License

This project is licensed under the [MIT License](LICENSE).
