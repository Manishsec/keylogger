# 🚀 Antigravity Keylogger (TKinter GUI)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Issues](https://img.shields.io/github/issues/Manishsec/keylogger?style=for-the-badge)](https://github.com/Manishsec/keylogger/issues)
[![Build](https://img.shields.io/badge/Build-Stable-brightgreen.svg?style=for-the-badge)](https://github.com/Manishsec/keylogger)

A modern, threaded keylogger with a sleek Tkinter GUI, providing real-time keystroke monitoring and automated logging.

---

## 🛑 DISCLAIMER

> [!CAUTION]
> **Educational Purposes Only.**
> This project is created strictly for educational and security research purposes. Using this software to monitor others without their explicit consent is illegal and unethical. The developer (Manish Yadav / Manishsec) is not responsible for any misuse or damage caused by this tool. Proceed with legal authorization only.

---

## ✨ Features
- 🎨 **Modern GUI**: Sleek "Dracula-inspired" dark mode interface.
- 🧵 **Threaded Architecture**: Non-blocking listener ensures a responsive UI.
- 🕒 **Live Monitoring**: View keystrokes in real-time with precise timestamps.
- 💾 **Persistent Logs**: All activity is automatically saved to `keylog.txt`.
- 🕹️ **Control Center**: Simple START/STOP buttons to manage logging activity.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Manishsec/keylogger.git
   cd keylogger
   ```

2. **Install dependencies**:
   ```bash
   pip install pynput
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

## 🚀 Usage
1. Click the **START LOGGING** button to begin capturing keystrokes.
2. The log display area will show each key pressed in real-time.
3. All keystrokes are recorded in a file named `keylog.txt`.
4. To stop the capture, simply click **STOP LOGGING**.

## 📁 Repository Structure
- `main.py`: Entry point for launching the application.
- `gui.py`: Core GUI logic and background listener thread.
- `keylog.txt`: The file where logs are stored (generated on first run).

---

## 🤝 Contributing
Contributions are welcome! If you have suggestions or bug reports, please open an issue or submit a pull request.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Developed with ❤️ by [Manishsec](https://github.com/Manishsec)**
