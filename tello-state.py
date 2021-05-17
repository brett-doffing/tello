"""
This will print out the state variables of the drone:

Data type: String

Example: “pitch:%d;roll:%d;yaw:%d;vgx:%d;vgy%d;vgz:%d;templ:%d;temph:%d;tof:%d;h:%d;bat:%d;baro:%.2f;time:%d;agx:%.2f;agy:%.2f;agz:%.2f;\r\n”

Explanation:
- pitch: Attitude pitch, degree o roll: Attitude roll, degree
- yaw: Attitude yaw, degree o vgx: Speed x,
- vgy: Speed y, 
- vgz: Speed z,
- templ: Lowest temperature, celcius degree o temph: Highest temperature, celcius degree o tof: TOF distance, cm
- h: Height, cm
- bat: Current battery percentage, %
- baro: Barometer measurement, cm
- time: Motors on time,
- agx: Acceleration x,
- agy: Acceleration y,
- agz: Acceleration z,
"""
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 8890))

while True:
    try:
        data, server = sock.recvfrom(1024)
        print(data.decode())
    except Exception as err:
        print(err)
        sock.close()
        break

sock.close()
