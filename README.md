ตัวโปรแกรมนี้จะสามารถบอกที่เราชูขึ้นมาได้ โดยที่ใช้คำสั่งตรงบรรทัดที่ 16-27 ในการจำแนกนิ้วโดยที่ตำแหน่งแรกหมายถึงนิ้วโป้ง ตำแหน่งต่อๆไปก็จะเรียงตามลำดับนิ้ว 
เช่น ถ้าตัวโปรแกรมตรวจสอบเจอนิ้วโป้งจะเข้าสู่เงื่อนไข if fingerup == [1, 0, 0, 0, 0]: ซึ่งจะแสดงข้อความว่า "Thumb" ใน Therminal
และเมื่อโปรแกรมไม่พบนิ้วมือจะแสดงข้อความว่า "No Finger Detected" ใน Therminal

ซึ่งตัวโปรแกรมนี้มีข้อจำกัดคือ
1.ไม่สามารถตรวจหานิ้วเมื่อเราชูหลังมือจะสามารถตรวจสอบได้เพียงนิ้วที่เราแสดงจากหน้ามือเท่านั้น
2.เมื่อเราชูมือ2ข้างพร้อมกันจะต้องชูนิ้วที่เหมือนกันเพื่อให้โปรแกรมตรวจสอบได้
                                             