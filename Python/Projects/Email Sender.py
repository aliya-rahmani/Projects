import smtplib

u_email = input("Enter Your Email:-")
u_Password = input("Enter Your Password:-")

r_email = input("Enter receiver's Email")

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(u_email, u_Password)

message = input("Enter Your Message")

s.sendmail(u_email, r_email, message)

s.quit()
