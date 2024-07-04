import minimalmodbus
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

def read_signed_register(instrument, register, num_decimals=2, function_code=4):
    try:
        value = instrument.read_register(register, num_decimals, function_code, signed=True)
        return value
    except Exception as e:
        print(f"Error reading register {register}: {e}")
        return None

def main():
    # Initialization of the instrument
    instrument = minimalmodbus.Instrument('/dev/ttyACM0', 1) # You can have a different port other than ACM0
    instrument.serial.baudrate = 115200
    instrument.serial.timeout = 1 

    # Connection with the database, you'll need to replace these values with the ones that you will define in your InfluxDB database
    bucket = "solar-monitor"
    org = "my-org"
    token = "Vsed7yVlxzYR87RmReK4KMtpS1g53M_6USe93DwJ09_YPp3-YtCpv8NAleTT35cwriBxT1UIf_cnTuwQ5KJXug=="
    try:
        client = InfluxDBClient(url=url, token=token, org=org)
        write_api = client.write_api(write_options=SYNCHRONOUS)
        print("Connected to InfluxDB successfully.")
    except Exception as e:
        print(f"Error connecting to InfluxDB: {e}")
        return
while True:
    # Read values from the registers
    ambient_temp = instrument.read_register(0x3110, 2) 
    controller_temp = instrument.read_register(0x3111, 2)
    load_voltage = instrument.read_register(0x310C, 2)
    load_current = read_signed_register(instrument, 0x310D, 2)
    battery_voltage = instrument.read_register(0x331A, 2)
    battery_current = read_signed_register(instrument, 0x331B, 2) 
    battery_soc = instrument.read_register(0x311A, 0)
    solar_voltage = instrument.read_register(0x3100, 2)
    solar_current = read_signed_register(instrument, 0x3101, 2)
    solar_power = instrument.read_register(0x3102, 2)
    battery_power = instrument.read_register(0x3106, 2)
    load_power = instrument.read_register(0x310E, 2)
        
    try:    
        # Write data to InfluxDB
        point = Point("solar_parameters") \
            .field("solar_voltage", solar_voltage) \
            .field("solar_current", solar_current) \
            .field("solar_power", solar_power) \
            .field("load_voltage", load_voltage) \
            .field("load_current", load_current) \
            .field("load_power", load_power) \
            .field("battery_voltage", battery_voltage) \
            .field("battery_current", battery_current) \
            .field("battery_power", battery_power) \
            .field("battery_soc", battery_soc) \
            .field("ambient_temp", ambient_temp) \
            .field("controller_temp", controller_temp)
            write_api.write(bucket=bucket, org=org, record=point)
            print("Data written to InfluxDB successfully.")
    except Exception as e:
            print(f"Error writing data to InfluxDB: {e}")

        
    print("Solar Panel:")
    print(f"  Voltage: {solar_voltage} V")
    print(f"  Current: {solar_current} A")
    print(f"  Power: {solar_power} W")
    print("Load:")
    print(f"  Voltage: {load_voltage} V")
    print(f"  Current: {load_current} A")
    print(f"  Power: {load_power} W")
    print("Battery:")
    print(f"  Voltage: {battery_voltage} V")
    print(f"  Current: {battery_current} A")
    print(f"  Power: {battery_power} W")
    print(f"  State of Charge: {battery_soc} %")
    print(f"Ambient Temperature: {ambient_temp} °C")
    print(f"Controller Temperature: {controller_temp} °C")

        # Waits 5 seconds to print the values again
        time.sleep(5)

if __name__ == "__main__":
    main()
 
