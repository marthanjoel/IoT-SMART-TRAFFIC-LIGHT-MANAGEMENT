Project Title: IoT Smart Traffic Light Management System





----
##Objective
To develop an intelligent, IoT-based traffic management system that optimizes urban traffic flow and enhances road safety. The system uses real-time vehicle detection to dynamically adjust traffic light timings, aiming to reduce congestion and improve efficiency at intersections.
--
##Tools & Technologies
Programming Language: Python 3.x
Frameworks/Libraries: OpenCV, Haar-Cascade Classifiers, NumPy, Tkinter (for GUI)
IoT Hardware: Raspberry Pi (or similar SBC)
Communication: Python Networking, BLOB (Binary Large Object - likely for image/video data transfer)
Dependencies: (List from requirements.txt - you'll need to create this if you haven't already)
opencv-python
numpy
Pillow (if used with Tkinter for images)
Any other specific libraries your project uses

---
##Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/marthanjoel/IoT-SMART-TRAFFIC-LIGHT-MANAGEMENT.git
cd IoT-SMART-TRAFFIC-LIGHT-MANAGEMENT
Use code with caution.

2. Create Virtual Environment
bash
python3 -m venv venv
source venv/bin/activate
Use code with caution.

3. Install Dependencies
bash
pip install -r requirements.txt
Use code with caution.

(Note: You need to create a requirements.txt file listing all Python libraries your project depends on. You can typically generate this with pip freeze > requirements.txt after installing all necessary packages in your virtual environment.)
4. Hardware Setup (if using Raspberry Pi)
Ensure your Raspberry Pi is configured with a camera module.
Connect LEDs/relays to GPIO pins of the Raspberry Pi to simulate or control traffic lights.
Configure network connectivity for potential remote access or data transfer.
5. Run the Project
bash
python3 app.py
Use code with caution.


--
##Simulation Details
Sensor Emulated: Camera (for vehicle detection)
Actuator Emulated: Traffic Lights (represented by LEDs controlled via Raspberry Pi/or GUI elements)
Trigger Logic: Traffic light timings dynamically adjusted based on real-time vehicle counts and density detected by the camera. For example, a lane with higher detected vehicle count might receive a longer green light duration.


--
##Screenshots
1<img width="1366" height="768" alt="Screenshot from 2025-09-19 14-17-22" src="https://github.com/user-attachments/assets/1fea764d-ad3e-4e0a-a92a-fd1c93c414c0" />

 2<img width="1366" height="768" alt="Screenshot from 2025-09-19 14-18-50" src="https://github.com/user-attachments/assets/08329b8e-8d5a-4fa6-af06-08747a824c39" />

---
##Observations
What worked well? (e.g., "Real-time vehicle detection using Haar-Cascade was effective in various lighting conditions," "The adaptive logic successfully adjusted light timings based on simulated traffic density.")
Any bugs or challenges? (e.g., "Optimizing Haar-Cascade performance on Raspberry Pi was a challenge," "Ensuring robust vehicle tracking across frames," "Handling false positives/negatives in detection.")
How was the simulation validated? (e.g., "Validated by observing GUI updates and LED behavior matching expected logic based on injected traffic scenarios," "Tested with pre-recorded video feeds simulating different traffic patterns.")


----
##Future Improvements
Implement more advanced object detection models (e.g., YOLO, SSD) for improved accuracy and speed.
Integrate cloud-based data logging and analytics for long-term traffic pattern analysis.
Incorporate pedestrian detection and safety features.
Develop a more sophisticated traffic prediction model.
Expand to manage multiple interconnected intersections.
Files & Structure
IoT-SMART-TRAFFIC-LIGHT-MANAGEMENT/
├── .iot_traffic_gui.py.swp (temporary GUI file)
├── app.py                  (Main application orchestrator)
├── background_subtraction.py (Module for background subtraction in video processing)
├── cars3.xml               (Haar-Cascade classifier for car detection)
├── README.md               (This documentation file)
├── vehicle_detection.py    (Core logic for vehicle detection and counting)
├── vehicle_detection.py.bak (Backup/older version of vehicle detection)
├── requirements.txt        (List of Python dependencies)
References
GitHub Repository: https://github.com/marthanjoel/IoT-SMART-TRAFFIC-LIGHT-MANAGEMENT
OpenCV Documentation: https://docs.opencv.org/
Raspberry Pi Documentation: https://www.raspberrypi.com/documentation/
