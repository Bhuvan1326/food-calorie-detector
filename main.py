import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ultralytics import YOLO

FOOD_CALORIES = {
    "banana": 105,
    "apple": 95,
    "orange": 62,
    "pizza": 285,
    "sandwich": 250, 
    "broccoli": 50,
    "cake": 250
}

class YOLOFoodTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Food Detector")
        self.root.geometry("900x800")
        
     
        self.model = YOLO('yolov8n.pt') 
        
        self.total_calories = 0
        self.detected_items = set()
        
        self.setup_ui()
        
     
        self.cap = cv2.VideoCapture(0)
        self.update_loop()

    def setup_ui(self):
    
        self.video_label = ttk.Label(self.root)
        self.video_label.pack(pady=10)

        self.info_label = ttk.Label(
            self.root, 
            text="Total: 0 kcal", 
            font=("Arial", 32, "bold"), 
            foreground="#2e7d32"
        )
        self.info_label.pack(pady=10)

        # Reset Button
        ttk.Button(self.root, text="Clear/Reset", command=self.reset).pack(pady=10)

    def reset(self):
        self.total_calories = 0
        self.detected_items.clear()
        self.info_label.config(text="Total: 0 kcal")

    def update_loop(self):
        ret, frame = self.cap.read()
        if ret:     
            results = self.model(frame, conf=0.4, verbose=False)
            
            for r in results:
                for box in r.boxes:
                    cls_id = int(box.cls[0])
                    label = self.model.names[cls_id]
                    
                    if label in FOOD_CALORIES:

                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                        
                        cv2.putText(frame, f"{label.upper()}", (x1, y1 - 10), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                        if label not in self.detected_items:
                            self.total_calories += FOOD_CALORIES[label]
                            self.info_label.config(text=f"Total: {self.total_calories} kcal")
                            self.detected_items.add(label)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb).resize((800, 600))
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
 
        self.root.after(10, self.update_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = YOLOFoodTracker(root)
    root.mainloop()