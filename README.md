# Autonomous Drone-Based Real-Time Pollution Monitoring System

#### Introduction
The Autonomous Drone-Based Real-Time Pollution Monitoring System is designed to enhance air quality monitoring by utilizing autonomous drones equipped with advanced sensors and real-time data transmission capabilities. The system aims to extend the reach of existing pollution monitoring stations, providing comprehensive data collection over a wide geographical area. By automating drone operations and implementing safety mechanisms, the solution addresses the challenges of drone operation and data acquisition.

#### Features
Autonomous Drone Flights: Fully automated drone missions with minimal human intervention.
Real-Time Data Transmission: 5G-enabled data upload to cloud servers for immediate analysis.
Advanced Sensor Suite: Equipped with sensors to measure temperature, CO₂ levels, VOCs, and particulate matter.
Interactive Data Visualization: Web-based platform for real-time mapping and analysis of pollution data.
Safety Protocols: Built-in mechanisms to prevent crashes and ensure safe drone operations.
Scalable Architecture: Easily deployable in new geographical locations with customizable sensor payloads.
Technical Architecture

#### System Overview
The system comprises autonomous drones equipped with sensors and an onboard computer, a ground control station, cloud-based data storage, and a web interface for data visualization.

#### Data Flow Diagram
mermaid
Copy code
flowchart LR
    A[Authorized Personnel] --> B[Drone Flight Management Software]
    B --> C[Assign Mission Parameters]
    C --> D[Drone]
    D --> E[Sensors Collect Data]
    E --> F[Onboard Processing (NVIDIA Computer)]
    F --> G[5G Network]
    G --> H[AWS Cloud Server]
    H --> I[Web Interface]
    I --> J[Data Visualization]
    
#### Hardware Components

#### Drone Platform
Frame: Custom-built drone frame suitable for payload capacity and flight stability.
Propulsion System: Motors and propellers selected for efficient flight dynamics.
Power Supply: High-capacity batteries with monitoring for safe operation.
Sensors
BME680 Sensor: Measures temperature, humidity, CO₂ concentration, and VOCs.
GP2Y Sensor: Detects particulate matter (PM2.5 and PM10).
Thermal Camera: Captures thermal images for additional environmental data.
Visual Camera: Provides high-resolution images of the monitored area.
Onboard Computer
NVIDIA Jetson Nano: Handles real-time data processing and autonomous flight algorithms.
Processing Capabilities: Enables edge computing for immediate data analysis.
Communication Module
5G Module: Ensures low-latency, high-speed data transmission to the cloud server.
NodeMCU: Microcontroller for sensor data aggregation and initial processing.
Software Components

#### Drone Flight Management Software
Mission Planning: Allows authorized personnel to assign GPS coordinates and altitudes.
Automation: Handles autonomous takeoff, flight, hovering, data collection, and landing.
User Interface: Intuitive GUI for ease of operation.

#### Mission Planner
Open-Source Platform: Utilizes open-source tools for flexibility and customization.
Flight Control: Integrates with the drone's autopilot system for precise navigation.

#### Data Processing and Storage
AWS Cloud Server: Stores collected data securely with scalability.
Data Processing Pipelines: Processes raw data for visualization and analysis.

#### Web Interface for Visualization
Interactive Maps: Displays real-time pollution levels on geographical maps.
Data Analytics Tools: Provides charts and graphs for trend analysis.
User Access Control: Secure login for data access and administration.

#### Installation
<img width="1159" alt="Screenshot 2024-09-10 at 1 49 23 PM" src="https://github.com/user-attachments/assets/36c1cdd9-3c62-4561-9009-d6dee9d67d29">

#### Hardware Setup
Assemble the Drone: Follow the assembly guide to build the drone frame and install components.
Install Sensors: Mount the BME680 and GP2Y sensors securely on the drone.
Set Up Onboard Computer: Install the NVIDIA Jetson Nano and connect it to the sensors and communication modules.
Integrate 5G Module: Connect the 5G module to the onboard computer for network access.
Power Management: Ensure batteries are installed and configured correctly.

#### Software Setup
Install Drone Firmware: Load the flight control firmware compatible with the mission planner.
Configure Mission Planner: Set up the open-source mission planner software on the ground control station.
Set Up NodeMCU: Program the microcontroller to read sensor data and communicate with the onboard computer.
Deploy Data Processing Scripts: Install necessary scripts on the NVIDIA computer for data handling.
Configure AWS Server: Set up cloud storage buckets and databases for data reception.
Deploy Web Interface: Host the visualization platform on a web server, connecting it to the AWS backend.

#### Usage
<img width="607" alt="Screenshot 2024-09-10 at 1 42 32 PM" src="https://github.com/user-attachments/assets/d979a974-95bf-43ac-ae39-24e804925932"># DragonFly

#### Assigning Missions
Access the Flight Management Software: Authorized personnel log in to the software interface.
Set Mission Parameters:
Input GPS coordinates for the target location.
Specify the altitude for data collection.
Schedule the mission time or set it to start immediately.
Launch Mission: Send the mission to the drone over the 5G network.

#### Autonomous Flight and Data Collection
Takeoff: Drone performs automated pre-flight checks and takes off.
Navigation: Flies to the designated GPS coordinates using onboard GPS and navigation systems.

![photo_2024-09-10 13 45 43](https://github.com/user-attachments/assets/3c5fd76d-f7c3-4425-b283-79f6f5371b71)


Data Collection:
Hovers at the specified altitude.
Sensors collect air quality data.
Cameras capture thermal and visual data.
Return to Launch: Upon mission completion or low battery detection, the drone returns and lands autonomously.

#### Real-Time Data Upload
Data Transmission: Sensor data is processed by the NVIDIA computer and sent via the 5G module.
Cloud Upload: Data is uploaded to the AWS server in real time.
Data Storage: Stored securely for access by the visualization interface.

#### Data Visualization

#### Interactive Maps
Real-Time Updates: Map displays current pollution levels at various locations.
Geographical Insights: Users can zoom in/out and click on markers for detailed data.
Heatmaps: Visual representation of pollution intensity across regions.

#### Charts and Graphs
Temporal Analysis: Line charts showing pollution levels over time.
Comparative Analysis: Bar graphs comparing different pollutants or locations.
Alerts: Notifications for areas exceeding pollution thresholds.

#### Safety Mechanisms
Free Fall Detection: Sensors detect rapid descent, triggering automatic safety protocols.
Battery Monitoring: Continuous monitoring ensures the drone returns before the battery depletes.
Obstacle Avoidance: Sensors detect obstacles to prevent collisions.
Failsafe Procedures: Pre-programmed actions in case of communication loss or system failure.

#### Challenges and Solutions

Potential Challenges
Complexity of Drone Operations: Requires expertise in piloting and maintenance.
Risk of Crashes: Environmental factors or technical issues can lead to accidents.
Data Security: Protecting sensitive data during transmission and storage.

Strategies for Overcoming Challenges
Automation: Reduces the need for skilled pilots by automating flight operations.
Robust Safety Features: Implements multiple safety mechanisms to prevent crashes.
Data Encryption: Uses secure protocols for data transmission and storage.
Regulatory Compliance: Adheres to aviation and data protection regulations.

#### Future Work
Enhanced AI Capabilities: Integrate machine learning for predictive analysis and anomaly detection.
Additional Sensors: Expand sensor suite to monitor other environmental parameters.
Network Optimization: Explore alternative communication methods like LoRaWAN for areas without 5G coverage.
Community Engagement: Develop mobile applications for public access to pollution data.

#### Contributing
We welcome contributions from the community. Please follow these steps:
Fork the Repository: Create a personal copy of the project.
Create a Branch: Use git checkout -b feature-name to create a new branch.
Commit Changes: Make your changes and commit with clear messages.
Push to Branch: Push your changes to your forked repository.
Submit a Pull Request: Describe your changes and submit for review.

#### License
This project is licensed under the MIT License.


# **Local Run Setup Instructions**

---

### **Table of Contents**
1. [Prerequisites](#prerequisites)
2. [Cloning the Repository](#cloning-the-repository)
3. [AWS Credentials Setup](#aws-credentials-setup)
4. [NodeMCU Configuration](#nodemcu-configuration)
5. [Running the Program](#running-the-program)
6. [Accessing Collected Data](#accessing-collected-data)
7. [Troubleshooting](#troubleshooting)

---

## **1. Prerequisites**

Before running the program locally, ensure that you have the following prerequisites installed and ready:

- **Python 3.x** (for running scripts)
- **Git** (for cloning the repository)
- **NodeMCU** (already configured for data collection)
- **AWS CLI** (optional, for manual access to AWS services)
- **Access to our AWS credentials** (you'll need to contact us for IAM access)

---

## **2. Cloning the Repository**

To get started, you need to clone the GitHub repository to your local machine. Run the following commands in your terminal or command prompt:

```bash
# Clone the repository
git clone https://github.com/YourRepoName/Drone-Pollution-Monitoring.git

# Change to the repository directory
cd Drone-Pollution-Monitoring
```

---

## **3. AWS Credentials Setup**

In order to access the AWS database where sensor data is stored, you need to have IAM credentials with appropriate permissions. Please **contact us** to get your IAM user set up.

Once you have received your AWS credentials, follow these steps to set them up locally:

1. Open a terminal/command prompt.
2. Use the following command to configure AWS credentials:

```bash
aws configure
```

You'll be prompted to enter:

- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default region** (Choose the region your AWS services are hosted in)
- **Output format** (Leave as default or type `json`)

After configuring, you’ll have access to the AWS data needed by the application.

---

## **4. NodeMCU Configuration**

Ensure your **NodeMCU** is already set up and connected to the sensors. The NodeMCU is responsible for gathering data from the **GP2Y** and **BME680** sensors and uploading this data to the **AWS database**.

If you haven't configured NodeMCU yet, follow these basic steps:

1. Flash your NodeMCU with the firmware provided in the repository (`nodemcu-firmware.ino`).
2. Configure the NodeMCU to connect to your Wi-Fi network for internet access.
3. Verify that the NodeMCU uploads data to AWS in real-time.

---

## **5. Running the Program**

Once everything is configured and the repository is cloned, you can run the program locally. The program fetches data from the AWS server in real-time and visualizes it.

1. **Install required Python packages**:
   
   Ensure you're in the project directory and run:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the main script**:

   ```bash
   python app.py
   ```

3. This will start fetching data from AWS and processing it for display on your local machine.

---

## **6. Accessing Collected Data**

The data collected by the **GP2Y** and **BME680** sensors is uploaded to AWS. You can access this data in two ways:

- **Via the Web Interface**: The program also offers a website where data is visualized in real-time. Once the program is running, navigate to `http://localhost:5000` in your web browser to see the interactive charts and maps.
  
- **Via AWS Database**: You can directly query the data stored in AWS by connecting through the **AWS Management Console** or using the **AWS CLI**.

---

## **7. Troubleshooting**

- **Problem**: Cannot access AWS services.
  - **Solution**: Ensure your AWS credentials are properly configured. Use `aws configure` to set them up.

- **Problem**: Data is not being uploaded to AWS.
  - **Solution**: Verify that the NodeMCU is correctly set up and has internet access. Check the Wi-Fi configuration and ensure the sensor data is being uploaded to AWS.

- **Problem**: Web interface not loading.
  - **Solution**: Ensure the `app.py` is running without errors and check if the local server is active at `http://localhost:5000`.

---

For any further assistance or credentials requests, please reach out to the project maintainers via email or through the GitHub repository issues section.


#### Team Details
Team Name: DRAGONFLY

Team Leader: Prashant Kumar

Team Members:

*Prashant - 2021UEA6565 - @Prashant2804*

*Tatwansh Jaiswal - 2021UCB6023 - @Tatwansh*

*Vishal Kumar - 2022UEA6572 - Sonia-036*

*Vaibhav Bhatia - 2021UEA6519 - Vaibhav-Bhatia-29*

*Sonia - 2022UCB6058 - sonia-036*

*Dhruv Bhardwaj - 2022UCB6056 - D18hr-uv*

#### Presentation Link: https://drive.google.com/file/d/1-rRpX-yOBYdBNJCx_QKKyCrxQJtyGUA8/view?usp=sharing

#### Video Link: https://www.youtube.com/watch?v=8XaMQl64hbo

For any questions or support, please contact dragonfly.on.nano@gmail.com.


