# macOS DNS Flush
A simple Python script to flush the DNS cache on macOS.

## Description
This script automates the process of flushing the DNS resolver cache on macOS. It's useful when you are experiencing DNS issues, such as websites not loading correctly or to clear old cache entries after a network change.

The script executes the following command, which requires administrative privileges:
```bash
sudo killall -HUP mDNSResponder
```

## Requirements
- Python 3
- macOS

## Usage
1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/macos_dnsflush.git
    cd macos_dnsflush
    ```
2.  Run the script with `sudo`:
    ```bash
    sudo python3 flush.py
    ```
3.  You will be prompted to enter your administrator password to proceed.

## Automation

### Method 1: Create an Alias (Recommended)
The simplest method - create a shell alias for quick execution.

1. Open your shell configuration file:
   ```bash
   # For zsh users (macOS default)
   nano ~/.zshrc
   
   # For bash users
   nano ~/.bash_profile
   ```

2. Add the following line:
   ```bash
   alias dnsflush="sudo python3 /path/to/macos_dnsflush/flush.py"
   ```

3. Apply the changes:
   ```bash
   source ~/.zshrc  # or source ~/.bash_profile
   ```

4. Now you can run the script using the `dnsflush` command in your terminal.

### Method 2: Schedule with cron
Set up a cron job to flush DNS automatically at regular intervals.

1. Edit crontab:
   ```bash
   sudo crontab -e
   ```

2. Add the following line (example: run daily at 3 AM):
   ```bash
   0 3 * * * /usr/bin/python3 /path/to/macos_dnsflush/flush.py
   ```

**Note**: For cron execution without password prompts, you need to configure sudoers:
```bash
sudo visudo
```
Add this line:
```
your_username ALL=(ALL) NOPASSWD: /sbin/killall -HUP mDNSResponder
```

### Method 3: LaunchAgent (Recommended - macOS Native)
Use macOS's native scheduler, LaunchAgent.

1. Create a plist file:
   ```bash
   nano ~/Library/LaunchAgents/com.user.dnsflush.plist
   ```

2. Add the following content:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.user.dnsflush</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/bin/python3</string>
           <string>/path/to/macos_dnsflush/flush.py</string>
       </array>
       <key>StartCalendarInterval</key>
       <dict>
           <key>Hour</key>
           <integer>3</integer>
           <key>Minute</key>
           <integer>0</integer>
       </dict>
   </dict>
   </plist>
   ```

3. Load the LaunchAgent:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.dnsflush.plist
   ```

4. To unload:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.user.dnsflush.plist
   ```

### Method 4: Network Change Trigger
Automatically run the script when network changes occur:

1. Create a script:
   ```bash
   sudo nano /usr/local/bin/auto-dnsflush.sh
   ```

2. Add the following content:
   ```bash
   #!/bin/bash
   /usr/bin/python3 /path/to/macos_dnsflush/flush.py
   ```

3. Make it executable:
   ```bash
   sudo chmod +x /usr/local/bin/auto-dnsflush.sh
   ```

4. Create a LaunchDaemon:
   ```bash
   sudo nano /Library/LaunchDaemons/com.dnsflush.network.plist
   ```

5. Add the following content:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.dnsflush.network</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/local/bin/auto-dnsflush.sh</string>
       </array>
       <key>WatchPaths</key>
       <array>
           <string>/Library/Preferences/SystemConfiguration</string>
       </array>
   </dict>
   </plist>
   ```

### Method 5: Keyboard Shortcut with Automator
Create a GUI shortcut for execution:

1. Open the **Automator** app
2. Select **Quick Action**
3. Add **Run Shell Script** action
4. Enter the following:
   ```bash
   sudo /usr/bin/python3 /path/to/macos_dnsflush/flush.py
   ```
5. Save (e.g., "DNS Flush")
6. Assign a keyboard shortcut in **System Settings > Keyboard > Shortcuts > Services**

## Security Notes
- Use with caution as this requires `sudo` privileges
- Be careful when editing the sudoers file to avoid typos
- Understand the security implications before automating with elevated privileges

## License
This project is licensed under the MIT License.
