# Harvester

## Overview
This repository contains the Harvester tool, which is designed for scanning and harvesting sensitive information from Windows systems. It is written in Go and includes scripts for additional functionality.

## Cloning the Repository
To clone this repository on Windows:

1. Install [Git for Windows](https://git-scm.com/download/win) if you don't have it.
2. Open Command Prompt or PowerShell.
3. Run:
   ```sh
   git clone https://github.com/AhmedYacineAbdelmalek/harvester.git
   ```
4. Change directory:
   ```sh
   cd harvester
   ```

## Building and Running

### Requirements
- [Go](https://golang.org/dl/) (version 1.18 or higher recommended)
- Windows OS

### Build
1. Open Command Prompt in the project directory.
2. Run:
   ```sh
   go build -o harvester.exe harvester.go
   ```

### Run
1. Execute the built binary:
   ```sh
   harvester.exe
   ```
   Optionally, you can provide a target address as an argument:
   ```sh
   harvester.exe <target_ip:port>
   ```

## Maintenance

- Keep Go updated to the latest stable version.
- To update dependencies, run:
  ```sh
  go mod tidy
  ```
- Review and update wallet paths and regexes in `harvester.go` as needed for new wallet types.
- Test changes on a Windows environment before deploying.

## Notes
- This tool is Windows-specific and uses Windows APIs.
- Ensure you have proper permissions to run and build executables.
- For any issues, check the Go documentation and Windows API references.

## License
See LICENSE for usage restrictions.
