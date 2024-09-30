import serial
import time
import argparse

# Konfiguriere die serielle Verbindung
ser = serial.Serial('/dev/serial0', 9600, timeout=1)  # Passe den Port an

def send_sms(phone_number, message):
    """Sendet eine SMS an die angegebene Telefonnummer mit der Nachricht."""
    time.sleep(1)
    ser.write(b'AT\r')
    time.sleep(1)

    ser.write(b'AT+CMGF=1\r')  # Setze SMS in den Textmodus
    time.sleep(1)

    ser.write(f'AT+CMGS="{phone_number}"\r'.encode())  # Empfängernummer senden
    time.sleep(1)

    ser.write(message.encode() + b'\x1A')  # Nachricht senden und mit Ctrl+Z (\x1A) abschließen
    time.sleep(1)

    # Rohdaten ausgeben
    response = ser.read(ser.in_waiting)
    print("Raw response:", response)  # Rohdaten ausgeben

    try:
        print("Decoded response:", response.decode('latin-1'))  # Dekodierte Antwort
    except UnicodeDecodeError:
        print("Error decoding response.")

if __name__ == "__main__":
    # Erforderliche Argumente aus der Kommandozeile abrufen
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 send_sms.py <recipient> <message>")
        sys.exit(1)

    recipient = sys.argv[1]
    message = sys.argv[2]

    # SMS senden
    send_sms(recipient, message)

    # Serielle Verbindung schließen
    ser.close()