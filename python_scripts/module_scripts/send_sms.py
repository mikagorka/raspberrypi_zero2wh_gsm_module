import serial
import time

# Konfiguriere die serielle Verbindung
ser = serial.Serial('/dev/serial0', 9600, timeout=1)  # Passe den Port an

def send_sms(phone_number, message):
    time.sleep(1)
    ser.write(b'AT\r')
    time.sleep(1)
    
    ser.write(b'AT+CMGF=1\r')
    time.sleep(1)
    
    ser.write(f'AT+CMGS="{phone_number}"\r'.encode())
    time.sleep(1)
    
    ser.write(message.encode() + b'\x1A')  # \x1A ist das Endzeichen für die SMS
    time.sleep(1)

    # Rohdaten ausgeben
    response = ser.read(ser.in_waiting)
    print("Raw response:", response)  # Rohdaten ausgeben

    try:
        print("Decoded response:", response.decode('latin-1'))  # Dekodierte Antwort
    except UnicodeDecodeError:
        print("Error decoding response.")

if __name__ == "__main__":
    phone_number = input("Gib die Telefonnummer ein (z.B. +49123456789): ")
    message = input("Gib die Nachricht ein: ")
    send_sms(phone_number, message)
    ser.close()