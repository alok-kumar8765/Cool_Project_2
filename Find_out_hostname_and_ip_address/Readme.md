# 🌐 Find Hostname and IP Address Tool

![GitHub Repo Size](https://img.shields.io/github/repo-size/alok-kumar8765/Cool_Project_2)
![GitHub Contributors](https://img.shields.io/github/contributors/alok-kumar8765/Cool_Project_2)
![GitHub Stars](https://img.shields.io/github/stars/alok-kumar8765/Cool_Project_2)
![GitHub License](https://img.shields.io/github/license/alok-kumar8765/Cool_Project_2)
![Python Version](https://img.shields.io/badge/python-3.x-blue)

---

## Table of Contents
<details>
<summary>Click to expand</summary>

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Code Explanation](#code-explanation)  
6. [Architecture & Flow](#architecture--flow)  
7. [Pros & Cons](#pros--cons)  
8. [Real-World Use Cases](#real-world-use-cases)  
9. [SEO & Optimization](#seo--optimization)  
10. [Contributing](#contributing)  
11. [License](#license)  

</details>

---

## Project Overview
<details>
<summary>Click to expand</summary>

**Find Hostname and IP Address Tool** is a lightweight Python utility that allows users to retrieve the IP address of any website by entering its hostname (URL). It is ideal for network troubleshooting, cybersecurity auditing, and general IT diagnostics.

**Key Highlights:**
- Simple and user-friendly interface.
- Instant hostname to IP resolution.
- Handles invalid hostnames gracefully.

</details>

---

## Features
<details>
<summary>Click to expand</summary>

- 🔹 **Hostname Resolution:** Converts a given hostname to its corresponding IP address.  
- 🔹 **Error Handling:** Provides informative messages for invalid or unreachable hostnames.  
- 🔹 **Command-Line Interface:** Easy to run on any Python-supported system.  
- 🔹 **Lightweight & Portable:** No heavy dependencies.  

</details>

---

## Installation
<details>
<summary>Click to expand</summary>

1. Clone the repository:
```bash
git clone https://github.com/alok-kumar8765/Cool_Project_2.git
````

2. Navigate to the project directory:

```bash
cd Cool_Project_2/Find_out_hostname_and_ip_address
```

3. Ensure Python 3.x is installed:

```bash
python --version
```

4. Run the script:

```bash
python find_hostname_ip.py
```

</details>

---

## Usage

<details>
<summary>Click to expand</summary>

```bash
Please enter website address(URL): www.example.com
Hostname: www.example.com
IP: 93.184.216.34
```

**Steps:**

1. Run the script using Python.
2. Enter any website URL (e.g., `google.com`).
3. View the resolved IP address instantly.
4. If an invalid hostname is entered, an error message will be displayed.

</details>

---

## Code Explanation

<details>
<summary>Click to expand</summary>

```python
# importing socket library
import socket

def get_hostname_IP():
    hostname = input("Please enter website address(URL):")
    try:
        print(f'Hostname: {hostname}')
        print(f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print(f'Invalid Hostname, error raised is {error}')

get_hostname_IP()
```

**Explanation:**

* **`socket` library:** Python standard library used for networking operations.
* **`gethostbyname()` method:** Resolves a hostname to its IPv4 address.
* **Error Handling (`socket.gaierror`):** Captures invalid hostname or DNS resolution errors.
* **Interactive Input:** Users can type any URL for instant resolution.

</details>

---

## Architecture & Flow

<details>
<summary>Click to expand</summary>

### Data Flow Diagram (DFD)

```mermaid
flowchart TD
    A[User Input: Hostname] --> B[Python Script: get_hostname_IP()]
    B --> C{Valid Hostname?}
    C -->|Yes| D[Resolve IP using socket.gethostbyname()]
    D --> E[Display Hostname & IP]
    C -->|No| F[Display Error Message]
```

### System Architecture

```mermaid
graph LR
    User[User] --> CLI[Command-Line Interface]
    CLI --> Script[Python Script]
    Script --> DNS[DNS Lookup]
    DNS --> Internet[Internet/Server]
    DNS --> Script
    Script --> CLI
    CLI --> User
```

### Execution Flow

1. User runs the script.
2. Script prompts for a hostname.
3. Script validates the hostname.
4. Script performs DNS lookup.
5. IP is returned to the user or error displayed.

</details>

---

## Pros & Cons

<details>
<summary>Click to expand</summary>

**Pros:**

* Lightweight and fast.
* Minimal dependencies.
* Easy to use for beginners.
* Cross-platform compatibility.

**Cons:**

* Supports only IPv4.
* Requires internet connectivity for hostname resolution.
* No GUI interface.

</details>

---

## Real-World Use Cases

<details>
<summary>Click to expand</summary>

* 🔹 **Network Troubleshooting:** Quickly find IP addresses for servers or websites.
* 🔹 **Cybersecurity Auditing:** Check hostname/IP mappings during penetration testing.
* 🔹 **System Administration:** Monitor hostnames and verify DNS resolutions.
* 🔹 **Educational Use:** Teaching networking basics to students.

**Example:**

```bash
Input: www.google.com
Output: Hostname: www.google.com
        IP: 142.250.190.36
```

</details>

---

## SEO & Optimization

<details>
<summary>Click to expand</summary>

**SEO-Friendly Attributes:**

* Rich headings with keywords: `Python hostname IP tool`, `DNS lookup`, `network troubleshooting`.
* Markdown structured for crawler readability.
* Includes badges and repository metadata for social proof.
* Collapsible sections improve readability and engagement.

</details>

---

## Contributing

<details>
<summary>Click to expand</summary>

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature_name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature_name`.
5. Create a pull request for review.

</details>

---

## License

<details>
<summary>Click to expand</summary>

This project is licensed under the MIT License. See the [LICENSE](https://github.com/alok-kumar8765/Cool_Project_2/blob/main/LICENSE) file for details.

</details>


---

