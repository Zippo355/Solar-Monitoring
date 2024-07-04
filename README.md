# Solar-Monitoring
A Python script used to monitor the solar parameters of a photovoltaic system in real-time, using Grafana as a monitoring platform.
This scripts works only using for your PV system if you have an EPEVER Solar Charge Controller and a RS485 to USB cable in order to communicate with the controller. Also, you will need to install the packages that can be found in the requirements.txt file using: "python -m pip install -r requirements.txt"
You will need to run the influxdb service using: "sudo systemctl start influxdb". 
You can verify if it's running using: "sudo systemctl status influxdb"
After following the Grafana installation guide: "https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/" , start the Grafana service:
"sudo systemctl start grafana-server", 
"sudo systemctl enable grafana-server"
