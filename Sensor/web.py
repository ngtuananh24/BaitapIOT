from flask import Flask, render_template_string
from sense_emu import SenseHat
import time
import threading

# Khởi tạo Sense HAT Emulator
sense = SenseHat()

app = Flask(__name__)

# Hàm đọc dữ liệu từ Sense HAT
def read_sensors():
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    joystick = sense.stick.get_events()
    return temperature, humidity, joystick

# HTML content lồng trong Python
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ứng dụng giám sát cảm biến</title>
</head>
<body>
    <h1>Ứng dụng giám sát cảm biến với Flask</h1>
    
    <h2>Dữ liệu cảm biến</h2>
    <p><strong>Nhiệt độ:</strong> {{ temperature }} °C</p>
    <p><strong>Độ ẩm:</strong> {{ humidity }} %</p>
    
    <h3>Trạng thái Joystick</h3>
    <p><strong>Joystick:</strong> {{ joystick_state }}</p>
    
    <h2>Hiển thị tên trên ma trận LED</h2>
    <p>Tên: Tuấn Anh</p>
</body>
</html>
"""

# Hàm hiển thị dữ liệu trong web
@app.route('/')
def display_data():
    # Đọc dữ liệu từ cảm biến
    temperature, humidity, joystick = read_sensors()

    # Trạng thái joystick
    joystick_state = "Không có sự kiện"
    if joystick:
        last_event = joystick[-1]
        joystick_state = f"{last_event.direction} - {last_event.action}"

    # Trả về HTML lồng trong Flask và dữ liệu cảm biến
    return render_template_string(html_template, 
                                  temperature=temperature, 
                                  humidity=humidity, 
                                  joystick_state=joystick_state)

# Hàm chạy Sense HAT emulator và cập nhật dữ liệu liên tục
def run_sensehat():
    while True:
        sense.show_message("Tuấn Anh", scroll_speed=0.05)
        time.sleep(2)

# Chạy Sense HAT emulator trong luồng riêng
if __name__ == "__main__":
    threading.Thread(target=run_sensehat, daemon=True).start()
    app.run(debug=True)