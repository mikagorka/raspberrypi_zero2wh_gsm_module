# Raspberry Pi Zero 2W(H) GSM Module

In this repository, I want to share all my scripts and instructions I've been using to connect a SIM card to my Raspberry Pi (affectionately called "Strawberry" 🍓).
> FILES FOLLOWING SOON...😶‍🌫️

## Table of Contents

1. [Link Collection](#link-collection)
2. [Pre-work](#pre-work)
3. [Instructions](#instructions)
4. [Useful AT Commands](#useful-at-commands)
5. [Troubleshooting](#troubleshooting)

## Link Collection

- GSM HAT: [Waveshare GSM/GPRS/GNSS HAT](https://www.amazon.de/dp/B076CPX4NN?ref=ppx_yo2ov_dt_b_fed_asin_title)
- Waveshare Manual: [User Manual](https://files.waveshare.com/upload/4/4a/GSM_GPRS_GNSS_HAT_User_Manual_EN.pdf)
- Waveshare GSM HAT Introduction: [Wiki](https://www.waveshare.com/wiki/GSM/GPRS/GNSS_HAT)
- CP2102 Drivers: [Pololu Documentation](https://www.pololu.com/docs/0J7/all)
- SMSC Numbers: [List of SMS Centers](https://www.handyhase.de/magazin/sms-mitteilungszentrale/)

## Pre-work

1. **Solder header pins** to the Raspberry Pi Zero (if you're not using the WH version with pre-soldered headers).
2. **Get a SIM card** with SMS and calling functionality.
3. **Assemble the Raspberry Pi Zero 2W(H)** with the GSM module.
4. **Ensure proper power supply** to both the Raspberry Pi and the GSM module.

## Instructions

1. **Connect to the Raspberry Pi** via SSH.
2. **Run the Raspberry Pi configuration tool** with the command:
```bash
   sudo raspi-config
```
2.1 Navigate to **Interface Options** > **Serial Port** and configure the following:
   - **Disable the serial console**: When asked if you want the login shell to be accessible over serial, select **No**.
   - **Enable serial hardware**: When asked if you want to enable the serial port hardware, select **Yes**.

2.2 **Reboot the Raspberry Pi**:
   - If the configuration tool prompts you to reboot, do so by selecting the reboot option.
   - If not, manually reboot the Raspberry Pi using the following command:

   ```bash
   sudo reboot
   ```
3. **Install `minicom`** for serial communication by running the following commands:

   ```bash
   sudo apt update
   sudo apt install minicom
   ```
4. **Connect to the GSM module** using `minicom`
   ```bash
   sudo minicom -D /dev/serial0 -b 115200
   ```
5. Your screen should now be ready. If you cannot type anything in the `minicom` terminal, refer to the [Troubleshooting](#troubleshooting) section below.

6. **Test the connection** by typing the following command:
   ```bash
   AT
   ```

> ⚠️ **one last word** ⚠️
> 
> You will need to set the SMSC (Short Message Service Center) to your provider's number (https://www.handyhase.de/magazin/sms-mitteilungszentrale/). 
> Without this, you will not be able to use SMS or make phone calls.

---

---
## Useful AT Commands

Here are some essential AT commands for sending SMS messages and making phone calls:

### SMS Commands

| **Command**                      | **Description**                                      |
|----------------------------------|------------------------------------------------------|
| `AT+CMGF=1`                      | Set SMS mode to text (not PDU)                      |
| `AT+CMGS="+49XXXXXXXXXX"`        | Send an SMS to the number `+49XXXXXXXXXX`          |
| `AT+CPMS?`                       | Check SMS storage status                            |
| `AT+CMGL="ALL"`                  | Read all received SMS messages                     |
| `AT+CMGD=1`                      | Delete the SMS with index 1                        |
| `AT+CSCA="+49XXXXXXXXXX"`        | Set or check the SMSC (Short Message Service Center) number |

### Phone Call Commands

| **Command**                      | **Description**                                      |
|----------------------------------|------------------------------------------------------|
| `ATD+49XXXXXXXXXX;`              | Make a phone call to the number `+49XXXXXXXXXX`    |
| `ATH`                            | Hang up the current call                            |
| `ATA`                            | Answer an incoming call                             |

## Troubleshooting

<details>
<summary><strong>Information Box: Troubleshooting</strong></summary>

1. **Incorrect UART selection switch**:
   - Ensure the UART selection switch on your GSM HAT is correctly set. Refer to the Waveshare manual for switch positions:
     - **A**: Control the SIM868 via USB to UART.
     - **B**: Control the SIM868 via Raspberry Pi.
     - **C**: Access Raspberry Pi via USB to UART.
   - For typical Raspberry Pi usage, ensure the switch is set to **B**.

2. **GPIO pins blocked by other services**:
   - If the serial connection does not work, it might be due to GPIO pins being used by other services. In such cases, you may need to edit the `/boot/firmware/config.txt` file:
   
     ```bash
     # Add this line to enable the UART properly
     dtoverlay=pi3-miniuart-bt

     # Example placement in the file
     [cm5]
     dtoverlay=dwc2,dr_mode=host
     dtoverlay=pi3-miniuart-bt
     ```

   - After making changes to the file, reboot the Raspberry Pi for the changes to take effect:

     ```bash
     sudo reboot
     ```

3. **Check for Serial Port Configuration**:
   - Ensure the serial port is correctly configured in your Raspberry Pi settings. Verify that the `/dev/serial0` is correctly linked to your GSM HAT. You can check this with:

     ```bash
     ls -l /dev/serial*
     ```

4. **Permissions Issue**:
   - Ensure that your user has the necessary permissions to access the serial port. You might need to add your user to the `dialout` group:

     ```bash
     sudo usermod -aG dialout $USER
     ```

   - After adding the user to the `dialout` group, log out and log back in or reboot the Raspberry Pi:

     ```bash
     sudo reboot
     ```

5. **Check Power Supply**:
   - Ensure that both the Raspberry Pi and the GSM HAT have adequate power supply. Insufficient power can cause communication issues. Use a reliable power source and check connections.

6. **Verify Connections**:
   - Double-check all physical connections between the Raspberry Pi and the GSM HAT. Ensure that the wiring is correct and secure.

</details>

By following these troubleshooting steps, you should be able to resolve common issues related to the GSM module connection and communication. If problems persist, consult the hardware manual or seek additional support from the manufacturer.
