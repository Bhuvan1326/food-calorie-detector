# 🍎 AI Food Calorie Tracker

A real-time, deep-learning-based application that identifies food items through a webcam and tracks total calorie intake. This project leverages **YOLOv8** for high-accuracy object detection and **Tkinter** for a smooth, user-friendly interface.

---

## 🌟 Key Features
* **Deep Learning Recognition:** Utilizes the YOLOv8 neural network to distinguish between humans and food, eliminating the "false positive" issues found in traditional image matching.
* **Real-time Calorie Calculation:** Instantly adds calories to a running total when a new food item is detected.
* **Anti-Double Counting:** Smart session management ensures an item is only counted once per scan.
* **Flicker-Free Display:** Optimized Tkinter main loop integration to prevent camera lag and visual artifacts.
* **Broad Detection Range:** Recognizes fruits (Apples, Bananas, Oranges) and prepared meals (Pizza, Burgers, Cake).

---

## 🛠️ Built With
* **Python 3.9+**
* **Ultralytics YOLOv8:** For state-of-the-art object detection.
* **OpenCV:** For real-time video processing.
* **Tkinter:** For the graphical user interface.
* **Pillow (PIL):** For image handling within the UI.

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python installed. Then, install the required libraries:
```bash
pip install ultralytics opencv-python pillow