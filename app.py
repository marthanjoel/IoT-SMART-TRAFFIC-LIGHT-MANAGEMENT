import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import threading
import sys
import time

class TrafficApp:
    """A Tkinter GUI for an intelligent traffic management system."""
    def __init__(self, root, cascade_path):
        self.root = root
        self.root.title("Smart Traffic Management System")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # --- UI Setup ---
        self.main_frame = tk.Frame(root, padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.video_label = tk.Label(self.main_frame)
        self.video_label.pack(side=tk.LEFT, padx=10)

        self.info_frame = tk.Frame(self.main_frame)
        self.info_frame.pack(side=tk.RIGHT, padx=10)

        self.status_label = tk.Label(self.info_frame, text="System Status: Idle", font=("Helvetica", 14), fg="gray")
        self.status_label.pack(pady=5)

        self.vehicle_count_label = tk.Label(self.info_frame, text="Detected Vehicles: 0", font=("Helvetica", 16))
        self.vehicle_count_label.pack(pady=5)
        
        # Traffic Light Visuals
        self.traffic_light_canvas = tk.Canvas(self.info_frame, width=100, height=250, bg="gray")
        self.traffic_light_canvas.pack(pady=20)
        self.red_light = self.traffic_light_canvas.create_oval(10, 10, 90, 90, fill="darkred", outline="white", width=2)
        self.yellow_light = self.traffic_light_canvas.create_oval(10, 90, 90, 170, fill="gray", outline="white", width=2)
        self.green_light = self.traffic_light_canvas.create_oval(10, 170, 90, 250, fill="darkgreen", outline="white", width=2)

        # Control buttons
        self.start_button = tk.Button(self.info_frame, text="Start Detection", command=self.start_detection)
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.info_frame, text="Stop Detection", command=self.stop_detection, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        # --- OpenCV and detection variables ---
        self.car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')
        if self.car_cascade.empty():
            messagebox.showerror("Error", f"Could not load cascade file. Make sure 'haarcascade_car.xml' is in the project directory.")
            sys.exit()
        
        self.cap = None
        self.is_detecting = False
        self.thread = None
        
        # --- Traffic light logic ---
        self.traffic_state = "RED"
        self.light_timer_id = None
        self.green_duration = 10 
        self.yellow_duration = 3
        
    def start_detection(self):
        """Starts the video stream and vehicle detection."""
        if not self.is_detecting:
            self.is_detecting = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_label.config(text="System Status: Running", fg="green")
            
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                messagebox.showerror("Error", "Could not open webcam.")
                self.stop_detection()
                return
                
            self.thread = threading.Thread(target=self.video_stream)
            self.thread.daemon = True
            self.thread.start()
            
            self.update_traffic_light()

    def stop_detection(self):
        """Stops the video stream and detection process."""
        if self.is_detecting:
            self.is_detecting = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.status_label.config(text="System Status: Idle", fg="gray")
            
            if self.cap:
                self.cap.release()
            
            if self.light_timer_id:
                self.root.after_cancel(self.light_timer_id)
                self.light_timer_id = None
                self.set_light("darkred", "gray", "darkgreen")
            self.vehicle_count_label.config(text=f"Detected Vehicles: 0")

    def video_stream(self):
        """Captures frames from the webcam and runs vehicle detection."""
        while self.is_detecting:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cars = self.car_cascade.detectMultiScale(gray, 1.1, 3)
            
            self.vehicle_count_label.config(text=f"Detected Vehicles: {len(cars)}")
            
            for (x, y, w, h) in cars:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
            
        if self.is_detecting:
            self.stop_detection()
            
    def update_traffic_light(self):
        """Updates the traffic light state in a timed loop."""
        if not self.is_detecting:
            return

        if self.traffic_state == "RED":
            self.set_light("red", "gray", "gray")
            self.traffic_state = "GREEN"
            self.light_timer_id = self.root.after(self.green_duration * 1000, self.update_traffic_light)
        elif self.traffic_state == "GREEN":
            self.set_light("gray", "gray", "green")
            self.traffic_state = "YELLOW"
            self.light_timer_id = self.root.after(self.green_duration * 1000, self.update_traffic_light)
        elif self.traffic_state == "YELLOW":
            self.set_light("gray", "yellow", "gray")
            self.traffic_state = "RED"
            self.light_timer_id = self.root.after(self.yellow_duration * 1000, self.update_traffic_light)

    def set_light(self, red_color, yellow_color, green_color):
        """Changes the colors of the traffic light canvas."""
        self.traffic_light_canvas.itemconfig(self.red_light, fill=red_color)
        self.traffic_light_canvas.itemconfig(self.yellow_light, fill=yellow_color)
        self.traffic_light_canvas.itemconfig(self.green_light, fill=green_color)

    def on_closing(self):
        """Handles window closing event."""
        if self.is_detecting:
            self.stop_detection()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = TrafficApp(root, 'haarcascade_car.xml')
    root.mainloop()

if __name__ == "__main__":
    main()
