#!/bin/bash

# Hilfe-Funktion
usage() {
    echo "Verwendung: $0 -r <Empfängernummer> -m <Nachricht>"
    echo "  -r <Empfängernummer>  Die Telefonnummer des Empfängers (z.B. +49123456789)"
    echo "  -m <Nachricht>        Die Nachricht in Hochkommas (z.B. 'Hallo Welt!')"
    echo "  -h                    Zeigt diese Hilfe an"
    exit 1
}

# Argumente parsen
while getopts ":r:m:h" opt; do
    case ${opt} in
        r)
            recipient=$OPTARG
            ;;
        m)
            message=$OPTARG
            ;;
        h)
            usage
            ;;
        \?)
            echo "Ungültige Option: -$OPTARG" >&2
            usage
            ;;
        :)
            echo "Option -$OPTARG benötigt ein Argument." >&2
            usage
            ;;
    esac
done

# Überprüfen, ob die Empfängernummer und die Nachricht gesetzt sind
if [ -z "$recipient" ] || [ -z "$message" ]; then
    usage
fi

# Python-Skript aufrufen
python3 send_sms.py "$recipient" "$message"