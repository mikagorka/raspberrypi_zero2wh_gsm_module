import serial
import time

# Konfiguriere die serielle Verbindung
ser = serial.Serial('/dev/serial0', 9600, timeout=1)  # Passe den Port an

def read_sms():
    time.sleep(1)
    ser.write(b'AT+CMGF=1\r')  # Setze den Textmodus
    time.sleep(3)  # Warte länger
    
    ser.write(b'AT+CMGL="ALL"\r')  # Lese alle SMS
    time.sleep(3)  # Warte länger

    # Lese die Antwort des GSM-Moduls
    response = ser.read(ser.in_waiting)
    print("Raw response:", response)  # Rohdaten ausgeben

    # Versuche, die Daten zu dekodieren
    try:
        decoded_response = response.decode('latin-1')
        print("Decoded response:")
        print(decoded_response)
    except UnicodeDecodeError:
        print("Error decoding response.")

    # Verarbeite die SMS-Nachrichten
    sms_messages = decoded_response.split("\n")
    for message in sms_messages:
        if "+CMGL" in message:
            print("SMS entry:", message)

if __name__ == "__main__":
    read_sms()
    ser.close()