from sense_emu import SenseHat  # Sử dụng sense_emu cho mô phỏng
import time  # Thư viện để tạm dừng

# Khởi tạo Sense HAT Emulator
sense = SenseHat()

# Vòng lặp vô hạn để đọc và hiển thị dữ liệu
while True:
    # Đọc dữ liệu từ cảm biến
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    joystick = sense.stick.get_events()

    # Hiển thị dữ liệu ra màn hình
    print(f"Nhiệt độ: {temperature:.2f}°C")
    print(f"Độ ẩm: {humidity:.2f}%")
    print("-----------------------")
    if joystick:
        print(f"Trạng thái Joystick: {joystick[-1].direction} - {joystick[-1].action}")
    
    # Hiển thị tên "Tuấn Anh" trên ma trận LED
    sense.show_message("Tuan Anh", scroll_speed=0.2)

    # Tạm dừng 2 giây
    time.sleep(3)