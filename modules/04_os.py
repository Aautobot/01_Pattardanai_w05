import os
from pathlib import Path

os_name = os.name
os_path = os.getcwd()
os_user = os.getenv("USER")

print(f"Operating System Name : {os_name}")
print(f"Current Working Directory : {os_path}")
print(f"Current User : {os_user}")

# การทำงานใน path
current_path = Path.cwd()
## print(f"Current Path : {current_path}")

# การสร้าง Folder
make_folder = current_path / "test123"
make_folder.mkdir(exist_ok=True)  # exist_ok=True จะไม่ทำให้เกิด error ถ้าโฟลเดอร์มีอยู่แล้ว

# # การสร้างไฟล์
make_file = current_path / "test.txt"
make_file.write_text("Hello, World!")   # เขียนข้อความลงในไฟล์

## make_file.exists()  # ตรวจสอบว่าไฟล์มีอยู่หรือไม่

#print(f"{make_file.stat()}")  # แสดงข้อมูลเกี่ยวกับไฟล์

# การอ่านไฟล์
content_test = make_file
content = content_test.read_text(encoding="UTF-8")
print(content)