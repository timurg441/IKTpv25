import smtplib, ssl
from email.message import EmailMessage

def saada_email(saaja_email):
    kiri = "Test kiri Pythonist"
    saatja_email = "1ame.xyz07@gmail.com"
    parool = input("Sisesta rakenduse parool: ")

    smtp_server = "smtp.gmail.com"
    port = 587
    context = ssl.create_default_context()

    msg = EmailMessage()
    msg.set_content(kiri,subtype='html')
    msg["Subject"]=kiri
    msg["From"]=saatja_email
    msg["To"]=saaja_email
    with open("image.png", "rb") as f:
        image_data = f.read()
    msg.add_attachment(image_data, maintype="image", subtype="png")

    html_content = """\
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>HTML email</title>
</head>
<body>
    <h1>HTML-e-kirja saatmine Pythonist</h1>
    <p>Tere,</p>
    <a href="https://github.com/timurg441/IKTpv25">
        See on minu GitHub!
    </a>
</body>
</html>
"""

    msg.set_content(html_content, subtype="html")

    try: 
        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls(context=context)
            server.login(saatja_email,parool)
            server.send_message(msg) #kui ei kasuta with siis on vaja sulgeda server.quit()
        print("E-kiri saadetud!")
    except Exception as e:
        print(f"Midagi läks valesti... {e}")

kellele = input("Sisesta saaja e-posti aadress: ")
saada_email(kellele)
