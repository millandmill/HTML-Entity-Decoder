
# HTML Entity Decoder

**HTML Entity Decoder** is a simple Python desktop application built with Tkinter for decoding HTML entities into readable text. It supports standard HTML entities, numeric character references, and repeatedly encoded HTML entities.

**HTML Entity Decoder** เป็นโปรแกรมบนเดสก์ท็อปที่พัฒนาด้วย Python และ Tkinter สำหรับถอดรหัส HTML Entity ให้กลับมาเป็นข้อความที่อ่านได้ รองรับ HTML Entity มาตรฐาน, Numeric Character References และข้อความที่ผ่านการเข้ารหัส HTML Entity ซ้อนกันหลายชั้น

---

## Features / คุณสมบัติ

- **HTML Entity Decoding** – Decode HTML entities into readable characters.
- **Numeric Entity Support** – Supports decimal (`&#65;`) and hexadecimal (`&#x41;`) character references.
- **Nested Entity Decoding** – Automatically decodes repeatedly encoded HTML entities up to 10 levels.
- **Thai and English Support** – Supports Thai, English, and Unicode characters.
- **Multiline Text** – Supports decoding multiple lines of text.
- **Copy Result** – Easily copy decoded text to the clipboard.
- **Paste Text** – Paste text directly from the clipboard.
- **Clear All** – Clear both input and output fields.

### คุณสมบัติ

- **ถอดรหัส HTML Entity** – แปลง HTML Entity ให้กลับมาเป็นอักขระปกติ
- **รองรับ Numeric Entity** – รองรับรหัสอักขระแบบเลขฐานสิบ (`&#65;`) และเลขฐานสิบหก (`&#x41;`)
- **ถอดรหัส Entity ซ้อนกัน** – ถอดรหัสข้อความที่ผ่านการเข้ารหัสซ้ำได้สูงสุด 10 ชั้น
- **รองรับภาษาไทยและภาษาอังกฤษ** – รองรับภาษาไทย ภาษาอังกฤษ และอักขระ Unicode
- **รองรับข้อความหลายบรรทัด** – สามารถถอดรหัสข้อความหลายบรรทัดพร้อมกัน
- **คัดลอกผลลัพธ์** – คัดลอกข้อความที่ถอดรหัสแล้วไปยัง Clipboard ได้
- **วางข้อความ** – วางข้อความจาก Clipboard ได้โดยตรง
- **ล้างข้อความ** – ล้างข้อความต้นฉบับและผลลัพธ์ได้พร้อมกัน

---

## Screenshots / ภาพตัวอย่าง

<!-- Add application screenshots here -->
<!-- เพิ่มภาพหน้าจอโปรแกรมที่นี่ -->

---

## Requirements / สิ่งที่ต้องมี

- Python 3.x
- Tkinter (usually included with Python)

No additional Python packages are required.

### สิ่งที่ต้องมี

- Python 3.x
- Tkinter (โดยปกติมาพร้อมกับ Python)

ไม่จำเป็นต้องติดตั้ง Python Package เพิ่มเติม

---

## Installation / การติดตั้ง

1. Clone this repository or download the source code.
2. Save the Python source file as `HTML_Entity_Decoder.py`.
3. Run the application using Python.

### วิธีติดตั้ง

1. Clone Repository หรือดาวน์โหลด Source Code
2. บันทึกไฟล์ Python เป็น `HTML_Entity_Decoder.py`
3. เปิดโปรแกรมด้วย Python

---

## Usage / วิธีใช้งาน

Run the following command:

```bash
python HTML_Entity_Decoder.py
```

1. Enter or paste the encoded text into the input field.
2. Click **Decode** to decode HTML entities.
3. The decoded text will appear in the output field.
4. Click **Copy Result** to copy the decoded text.

### วิธีใช้งาน

1. ป้อนหรือวางข้อความที่ต้องการถอดรหัสลงในช่องข้อความต้นฉบับ
2. คลิกปุ่ม **ถอดรหัส** เพื่อเริ่มถอดรหัส HTML Entity
3. ผลลัพธ์ที่ถอดรหัสแล้วจะแสดงในช่องผลลัพธ์
4. คลิกปุ่ม **คัดลอกผลลัพธ์** เพื่อคัดลอกข้อความไปใช้งาน

---

## Example / ตัวอย่าง

**Input / ข้อความต้นฉบับ**

```text
Hello &quot;World&quot;!
Tom &amp; Jerry
&lt;html&gt;Hello&lt;/html&gt;
&#65;&#66;&#67;
&#x41;&#x42;&#x43;
```

**Output / ผลลัพธ์**

```text
Hello "World"!
Tom & Jerry
<html>Hello</html>
ABC
ABC
```

---

## How It Works / หลักการทำงาน

The application uses Python's built-in `html` module, specifically the `html.unescape()` function, to convert HTML character references into their corresponding Unicode characters.

The program repeats the decoding process up to 10 times or stops when no further changes occur. This allows it to handle nested HTML entities.

### หลักการทำงาน

โปรแกรมใช้โมดูล `html` ที่มีอยู่ใน Python โดยเรียกใช้ฟังก์ชัน `html.unescape()` เพื่อแปลง HTML Character References ให้กลับมาเป็นอักขระ Unicode ที่ถูกต้อง

โปรแกรมจะทำการถอดรหัสซ้ำได้สูงสุด 10 รอบ หรือหยุดเมื่อไม่พบการเปลี่ยนแปลงของข้อความ เพื่อรองรับข้อความที่มีการเข้ารหัส HTML Entity ซ้อนกันหลายชั้น

---

## Limitations / ข้อจำกัด

This application is designed specifically for HTML Entity decoding. It does not decrypt encrypted data, passwords, Base64, XOR, or other encoding formats.

โปรแกรมนี้ออกแบบมาสำหรับถอดรหัส HTML Entity เท่านั้น ไม่สามารถถอดรหัสข้อมูลที่ผ่านการเข้ารหัสด้วย Encryption, Password, Base64, XOR หรือรูปแบบการเข้ารหัสชนิดอื่นได้

---

## License / ลิขสิทธิ์

This project is provided for educational and general-purpose use.

โปรเจกต์นี้จัดทำขึ้นเพื่อการศึกษาและการใช้งานทั่วไป
