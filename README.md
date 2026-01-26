# AI Food Calorie Tracker

A real-time Computer Vision application that uses **Deep Learning (YOLOv8)** to identify food items through a webcam and instantly calculate nutritional data.

---

## 🚀 Key Features
- **Neural Network Detection**: Uses a Convolutional Neural Network (CNN) to distinguish between 80+ objects.
- **Human-Object Separation**: Solved the "Human Banana" problem—the AI identifies people and fruits separately to prevent false positives.
- **Smart Logic**: Prevents calorie double-counting by tracking unique items per session.
- **High Performance**: Optimized for 30+ FPS using Tkinter's `after()` loop for smooth video.

---

## 🍕 Calorie Reference Table
The application identifies these common items and maps them to their average caloric values:

| Food Item | AI Label | Calories (kcal) | Serving Size |
| :--- | :--- | :--- | :--- |
| **Banana** | `banana` | 105 | 1 Medium |
| **Orange** | `orange` | 62 | 1 Medium |
| **Apple** | `apple` | 95 | 1 Medium |
| **Pizza** | `pizza` | 285 | 1 Slice |
| **Burger** | `sandwich` | 350 | 1 Unit |
| **Hot Dog** | `hot dog` | 150 | 1 Unit |
| **Cake** | `cake` | 250 | 1 Slice |
| **Broccoli** | `broccoli` | 50 | 1 Cup |



https://github.com/user-attachments/assets/32306d42-8ebb-4ad4-a61e-77339df57bf5




---

## 🛠️ Installation & Setup

<<<<<<< HEAD
### Prerequisites
Ensure you have Python installed. Then, install the required libraries:
```bash
pip install ultralytics opencv-python pillow
=======
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/Bhuvan1326/food-calorie-detector.git](https://github.com/Bhuvan1326/food-calorie-detector.git)
>>>>>>> 9ad54a5 (Update README with Calorie Table and Technical explanation)
