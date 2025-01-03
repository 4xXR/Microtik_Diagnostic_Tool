**MikroTik Diagnostic Tool**

A Python-based diagnostic tool for MikroTik routers that connects via
the MikroTik API and SSH to retrieve essential information for
troubleshooting. The script provides system details, interface statuses,
extended ping results, and clock configuration.

**Features**

-   Retrieve system information (model, version, uptime, CPU load,
    memory usage).

-   Display the status of all interfaces (active or inactive).

-   Perform an extended ping test to diagnose connectivity issues.

-   Retrieve the current date and time configuration on the MikroTik
    device.

**Requirements**

**Dependencies**

-   Python 3.6 or later

-   Libraries:

    -   librouteros: For MikroTik API interaction.

    -   paramiko: For SSH-based commands.

Install the required libraries:

pip install librouteros paramiko

**Usage**

1.  Clone the repository and navigate to the project folder:

> git clone https://github.com/4xXR/Microtik_Diagnostic_Tool.git
>
> cd Microtik_Diagnostic_Tool

2.  Update the connection details in the script:

> API_HOST = \'192.168.88.1\' \# Replace with your MikroTik IP address
>
> API_USER = \'admin\' \# Replace with your MikroTik username
>
> API_PASS = \'\' \# Replace with your MikroTik password

3.  Run the script:

> python \<script_name\>.py

**Output Example**

The script provides output similar to the following:

**MikroTik Info**

=== MikroTik Info===

Model: hAP ac²

Version: 6.49.7

Uptime: 5d12h35m

CPU-Load: 18%

Memory usage: 245760 free of 524288

**Interfaces Status**

=== Interfaces status ===

Interface name: ether1 \| Active: True

Interface name: wlan1 \| Active: False

**Extended Ping**

=== Extended Ping to 8.8.8.8 ===

SEQ HOST SIZE TTL TIME STATUS

0 8.8.8.8 64 115 17ms

1 8.8.8.8 64 115 18ms

2 8.8.8.8 64 115 15ms

3 8.8.8.8 64 115 20ms

4 8.8.8.8 64 115 18ms

5 8.8.8.8 64 115 18ms

6 8.8.8.8 64 115 17ms

sent=10 received=10 packet-loss=0% min-rtt=15ms avg-rtt=17ms
max-rtt=20ms

\...

**Clock Configuration**

=== Clock Configuration ===

Date: dec/19/2024

Time: 14:35:12

**Functionality Breakdown**

1.  **System Info Retrieval (get_router_info)**:

    -   Fetches basic system information such as model, version, uptime,
        CPU load, and memory usage.

2.  **Interface Status Check (get_interfaces_status)**:

    -   Lists all interfaces and their active/inactive states.

3.  **Extended Ping via SSH (perform_ping_ssh)**:

    -   Performs a customizable extended ping to a specified address.

4.  **Clock Info Retrieval (get_clock_info)**:

    -   Displays the current date and time on the MikroTik device.

**Error Handling**

The script gracefully handles:

-   Connection errors due to incorrect IP or credentials.

-   SSH or API errors with descriptive messages.

**Future Improvements**

-   Add support for saving the diagnostic output to a file.

-   Include more advanced diagnostic checks (e.g., firewall rules,
    routing table).

-   Automate diagnostics for multiple MikroTik devices.
