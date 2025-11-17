def caesar_cipher(text, shift, mode):
    """
    เข้ารหัส (encode) หรือถอดรหัส (decode) ข้อความโดยใช้ Caesar Cipher.
    :param text: ข้อความต้นฉบับ
    :param shift: ค่าการเลื่อน (key)
    :param mode: 'e' สำหรับ encode, 'd' สำหรับ decode
    :return: ข้อความที่ถูกเข้ารหัสหรือถอดรหัสแล้ว
    """
    result = ""
    
    # ถ้าเป็นโหมดถอดรหัส ให้เปลี่ยนทิศทางของค่า shift
    if mode.lower() == 'd':
        shift = -shift

    for char in text:
        if char.isalpha(): # ตรวจสอบว่าเป็นตัวอักษรหรือไม่
            
            start = ord('A') if char.isupper() else ord('a')
            
            # คำนวณตำแหน่งใหม่
            # 1. แปลงตัวอักษรเป็นตำแหน่ง (0-25)
            # 2. บวก/ลบค่า shift
            # 3. ใช้ % 26 เพื่อวนกลับไปที่ต้นแถว
            # 4. บวกด้วยค่า start เพื่อแปลงกลับเป็นรหัส ASCII
            new_ord = (ord(char) - start + shift) % 26 + start
            
            result += chr(new_ord)
        elif char.isspace():
            result += char # คงช่องว่างไว้
        else:
            result += char # คงตัวเลขหรือสัญลักษณ์อื่น ๆ ไว้
            
    return result

if __name__ == "__main__':
    print("=======================================")
    print("    Caesar Cipher Encoder/Decoder")
    print("=======================================")

    while True:
        mode = input("ต้องการเข้ารหัส (e) หรือถอดรหัส (d)? (พิมพ์ 'exit' เพื่อออก): ").lower()
        if mode == 'exit':
            break
        if mode not in ['e', 'd']:
            print("❌ กรุณาป้อน 'e' หรือ 'd' เท่านั้น")
            continue

        text = input("ป้อนข้อความ: ")
        
        try:
            shift = int(input("ป้อนค่าการเลื่อน (Shift Key) (เช่น 3): "))
        except ValueError:
            print("❌ กรุณาป้อนตัวเลขสำหรับค่าการเลื่อน")
            continue

        output = caesar_cipher(text, shift, mode)
        
        if mode == 'e':
            print(f"\n✅ ข้อความเข้ารหัส: {output}")
        else:
            print(f"\n✅ ข้อความถอดรหัส: {output}")
            
        print("---------------------------------------")