counter = 0

def increment_counter():
    '''เพิ่มค่าตัวแปร counter ขึ้นทีละ 1'''
    global counter
    counter += 1
    print(f"Counter incremented to : {counter}")

def reset_counter():
    '''รีเซ็ตค่าตัวแปร counter เป็น 0'''
    global counter
    counter = 0
    print("Counter reset to 0")

increment_counter()
increment_counter()
increment_counter()
reset_counter()