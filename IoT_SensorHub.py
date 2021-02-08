import httplib
import urllib
import time
import smbus

key = "MGMP9U0Y209EB0FM"  # Put your API Key here


def thermometer():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        #temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        DEVICE_BUS = 1
        DEVICE_ADDR = 0x17

        TEMP_REG = 0x01
        STATUS_REG = 0x04
        ON_BOARD_HUMIDITY_REG = 0x06
        ON_BOARD_SENSOR_ERROR = 0x07
        BMP280_TEMP_REG = 0x08
        BMP280_PRESSURE_REG_L = 0x09
        BMP280_PRESSURE_REG_M = 0x0A
        BMP280_PRESSURE_REG_H = 0x0B
        BMP280_STATUS = 0x0C

        bus = smbus.SMBus(DEVICE_BUS)

        aReceiveBuf = []

        aReceiveBuf.append(0x00)

        for i in range(TEMP_REG,BMP280_STATUS + 1):
            aReceiveBuf.append(bus.read_byte_data(DEVICE_ADDR, i))
        
        if aReceiveBuf[STATUS_REG] & 0x01 :
            extTemp = "overrange"
            #print("Off-chip temperature sensor overrange!")
        elif aReceiveBuf[STATUS_REG] & 0x02 :
            extTemp = "false"
            #print("No external temperature sensor!")
        else :
            extTemp = aReceiveBuf[TEMP_REG]
            #print("Current off-chip sensor temperature = %d Celsius" % aReceiveBuf[TEMP_REG])
        
        intHumid = aReceiveBuf[ON_BOARD_HUMIDITY_REG]

        if aReceiveBuf[ON_BOARD_SENSOR_ERROR] != 0 :
            intSensor = "false"
            #print("Onboard temperature and humidity sensor data may not be up to date!")

        if aReceiveBuf[BMP280_STATUS] == 0 :
            baroSensor = "true"
            #print("Current barometer temperature = %d Celsius" % aReceiveBuf[BMP280_TEMP_REG])
            baroTemp = aReceiveBuf[BMP280_TEMP_REG]
            #print("Current barometer pressure = %d pascal" % (aReceiveBuf[BMP280_PRESSURE_REG_L] | aReceiveBuf[BMP280_PRESSURE_REG_M] << 8 | aReceiveBuf[BMP280_PRESSURE_REG_H] << 16))
            baroPress = (aReceiveBuf[BMP280_PRESSURE_REG_L] | aReceiveBuf[BMP280_PRESSURE_REG_M] << 8 | aReceiveBuf[BMP280_PRESSURE_REG_H] << 16)
        else :
            baroSensor = "false"
            #print("Onboard barometer works abnormally!")
            
        params = urllib.urlencode({'field1': extTemp, 'key':key,'field2': intHumid, 'key':key,'field3': baroPress, 'key':key, 'field4': baroTemp, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print extTemp, intHumid, baroTemp, baroPress
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        break
if __name__ == "__main__":
        while True:
                thermometer()