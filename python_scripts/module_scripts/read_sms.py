import serial
import time

# Konfiguriere die serielle Verbindung
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Passe den Port an

def read_sms():
    time.sleep(1)
    ser.write(b'AT+CMGF=1\r')  # Setze den Textmodus
    time.sleep(1)
    
    ser.write(b'AT+CMGL="ALL"\r')  # Lese alle SMS
    time.sleep(1)

    # Lese die Antwort des GSM-Moduls
    response = ser.read(ser.in_waiting).decode('latin-1')
    print("Received SMS:")
    print(response)

if __name__ == "__main__":
    read_sms()
    ser.close()