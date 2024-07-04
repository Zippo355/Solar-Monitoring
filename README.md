# Solar-Monitoring
A Python script used in a Raspberry Pi Model 4 B to monitor the solar parameters of a photovoltaic system in real-time, using Grafana as a monitoring platform. <br>
This scripts works only if you have an EPEVER Solar Charge Controller, as the registers defined in the code are the modbus addresses that are unique to this specific controller, and a RS485 to USB cable in order to communicate with the controller. Also, you will need to install the packages that can be found in the requirements.txt file using: "python -m pip install -r requirements.txt" <br>
You will need to run the influxdb service using: "sudo systemctl start influxdb". <br>
You can verify if it's running using: "sudo systemctl status influxdb" <br>
After following the Grafana installation guide: "https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/" , start the Grafana service: <br>
"sudo systemctl start grafana-server" <br> 
"sudo systemctl enable grafana-server" <br>
Accessing the InfluxDB database from a browser: "http://localhost:8086" or "http://your-raspberrypi-ip-address:8086" <br>
Accessing the Grafana Dashboard from a browser: "http://localhost:3000" or "http://your-raspberrypi-ip-address:3000"
