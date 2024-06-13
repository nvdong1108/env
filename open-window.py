from pywinauto import Application

app_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Khởi tạo ứng dụng
app = Application(backend="uia").start(app_path)

# Chờ cho ứng dụng khởi động hoàn toàn
main_window = app.window(title_re='.*Google Chrome')

# Đặt kích thước của cửa sổ
main_window.set_size(width=800, height=600)

# Đóng ứng dụng sau khi hoàn thành
#app.kill()
