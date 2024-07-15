# IoT Temperature Monitoring System

This project implements an IoT-based temperature monitoring system using an ESP32 microcontroller, Flask server, and data visualization with matplotlib.

## Project Structure

- `sensor_code.ino`: Arduino code for ESP32 to read temperature data from DHT22 sensor and send it to the server.
- `server.py`: Python Flask server to receive temperature data from the ESP32 and log it to a file.
- `visualize.py`: Python script to visualize temperature data logged by the server using matplotlib.
- `temperature_log.txt`: Log file to store temperature data.

## Requirements

- Python 3
- Flask
- matplotlib
- Arduino IDE or PlatformIO (for ESP32)

- Python 3 <i class="fab fa-python"></i>
- Flask <i class="fab fa-flask"></i>
- matplotlib <i class="fab fa-chart-line"></i>
- Arduino IDE or PlatformIO (for ESP32) <i class="fab fa-arduino"></i>

## Setup and Installation

### Microcontroller (ESP32)

1. Upload `sensor_code.ino` to your ESP32 using Arduino IDE or PlatformIO.

### Server (Flask)

1. Install Python dependencies:
   ```bash
   pip install flask matplotlib
Start the Flask server:
 ```bash
python server.py
 ```

The server will run on http://localhost:5000.
Visualization
Run the visualization script:
 ```bash
python visualize.py
 ```

This will generate a plot (temperature_plot.png) based on data logged in temperature_log.txt.

Troubleshooting

Port Already in Use: If port 5000 is already in use, modify server.py to use a different port (app.run(port=5001)).
No Graph Displayed: If running in a non-interactive environment (e.g., SSH without X11 forwarding), matplotlib will save the plot as temperature_plot.png instead of displaying it.
Contributing
Contributions are welcome! Please fork the repository and submit pull requests.
