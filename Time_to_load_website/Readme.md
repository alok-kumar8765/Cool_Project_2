# 🚀 Cool Project 2 – Website Load Time Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Stable-success.svg)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey.svg)
![Networking](https://img.shields.io/badge/Category-Networking-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Maintainer](https://img.shields.io/badge/Maintainer-alok--kumar8765-purple.svg)

---

## 📌 Project Title
**Website Load Time Analyzer using Python**

---

<details>
<summary><strong>📖 Project Description</strong></summary>

This project is a **lightweight Python-based CLI utility** that measures the **time taken to load a website URL**.  
It helps developers, testers, and system administrators **analyze website responsiveness** by calculating the total load duration in seconds.

The tool uses Python’s built-in networking and time modules to ensure:
- Minimal dependencies
- Accurate measurement
- Cross-platform compatibility

</details>

---

<details>
<summary><strong>📂 Table of Contents</strong></summary>

1. Project Overview  
2. Features  
3. Tech Stack  
4. How It Works  
5. Code Explanation  
6. Architecture Diagram  
7. Data Flow Diagram (DFD)  
8. Execution Flow Diagram  
9. Pros & Cons  
10. Real-World Use Cases  
11. Example Output  
12. Limitations  
13. Future Enhancements  

</details>

---

<details>
<summary><strong>🎯 Project Overview</strong></summary>

- **Input**: Website URL  
- **Process**: Measures network fetch duration  
- **Output**: Load time in seconds  
- **Mode**: Command Line Interface (CLI)

</details>

---

<details>
<summary><strong>✨ Features</strong></summary>

- ⏱️ Accurate load time measurement  
- 🌐 Supports HTTP & HTTPS URLs  
- 🧠 Automatic protocol handling  
- 🖥️ CLI-based (simple & fast)  
- 🧩 No external dependencies  

</details>

---

<details>
<summary><strong>🛠 Tech Stack</strong></summary>

- **Language**: Python 3  
- **Libraries**:
  - `urllib.request`
  - `time`
- **Execution**: Terminal / Command Prompt  

</details>

---

<details>
<summary><strong>⚙️ How It Works</strong></summary>

1. User inputs a website URL  
2. URL is validated for protocol  
3. Website content is fetched  
4. Start and end timestamps are recorded  
5. Load time is calculated and displayed  

</details>

---

<details>
<summary><strong>📘 Code Explanation</strong></summary>

### `get_load_time(url)`
- Accepts a URL string
- Opens the website using `urlopen`
- Reads the full response
- Measures execution time
- Returns load duration in seconds

### `__main__`
- Takes user input
- Calls the load time function
- Prints formatted result

</details>

---

<details>
<summary><strong>🏗 Architecture Diagram</strong></summary>

```mermaid
graph TD
    User -->|Enters URL| CLI
    CLI --> Python_Function
    Python_Function -->|Fetch URL| Internet
    Internet --> Python_Function
    Python_Function -->|Time Calculated| CLI
    CLI --> User
```

</details>


---

<details>
<summary><strong>📊 Data Flow Diagram (DFD)</strong></summary>

```mermaid
flowchart LR
    A[User] --> B[Input URL]
    B --> C[URL Validator]
    C --> D[HTTP Request]
    D --> E[Time Measurement]
    E --> F[Result Output]
```

</details>

---

<details>
<summary><strong>🔄 Execution Flow Diagram</strong></summary>

```mermaid
sequenceDiagram
    participant U as User
    participant P as Python Program
    participant W as Website

    U->>P: Enter URL
    P->>W: Send Request
    W-->>P: Response Data
    P->>P: Calculate Load Time
    P-->>U: Display Result
```

</details>


---

<details>
<summary><strong>✅ Pros & ❌ Cons</strong></summary>

## ✅ Pros

- Simple and beginner-friendly

- No third-party dependencies

- Fast execution

- Works on any OS


## ❌ Cons

- Measures only total load time

- No DNS / TTFB breakdown

- No timeout handling

- No async support


</details>

---

<details>
<summary><strong>🌍 Real-World Use Cases</strong></summary>

Web Performance Testing
- Measure site responsiveness during development.

Server Health Monitoring
- Quickly verify if a website is slow or unreachable.

Educational Tool
- Learn about HTTP requests and performance metrics.

Automation Scripts
- Integrate into CI pipelines for uptime checks.


</details>

---

<details>
<summary><strong>🧪 Example Output</strong></summary>

Enter the url whose loading time you want to check: google.com

The time taken to load google.com is 0.42 seconds.

</details>

---

<details>
<summary><strong>⚠️ Limitations</strong></summary>

- No error handling for invalid URLs

- No retry mechanism

- Blocking I/O

- Does not handle redirects explicitly


</details>

---

<details>
<summary><strong>🚀 Future Enhancements</strong></summary>

- Add timeout & exception handling

- Measure DNS lookup & TTFB

- Async version using aiohttp

- GUI or Web Dashboard

- Logging & CSV export


</details>

---

## 👨‍💻 Author

Alok Kumar
GitHub: https://github.com/alok-kumar8765/Cool_Project_2


---

## 📄 License

This project is licensed under the MIT License – free to use, modify, and distribute.


---

> ⭐ If you find this project useful, please give it a star on GitHub!

---
