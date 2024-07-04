# Solar-Monitoring
A Python script used to monitor the solar parameters of a photovoltaic system in real-time, using Grafana as a monitoring platform.
This scripts works only using for your PV system if you have an EPEVER Solar Charge Controller and a RS485 to USB cable in order to communicate with the controller. Also, you will need to install minimalmodbus library and InfluxDB (run the below commands):
pip install minimalmodbus
pip install influxdb-client
