import qrcode

Name = input("Please Enter Your Name : ")
Tel = input("Please Enter Youre Mobile Number : ")

QR = qrcode.make(f"Name : {Name} | Tel: {Tel}")

QR.save("QR.png")