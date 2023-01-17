from flask import Flask, render_template, request
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("subhanshugupta1995@gmail.com", "zgqvkedzzdcvpbjc")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate",methods=['post'])
def generate():

    email=""
    email=request.form.get('email')
    s.sendmail('&&&&&&&&&&&',email,msg)

    return render_template('verify.html')

@app.route('/verify',methods=['post'])
def verify():
    res=""
    user_otp=""

    user_otp+=request.form.get('ist')
    user_otp+=request.form.get('sec')
    user_otp+=request.form.get('third')
    user_otp+=request.form.get('fourth')
    user_otp+=request.form.get('fifth')
    user_otp+=request.form.get('sixth')

    if user_otp==OTP:
        res="Verified"
    else:
        res="Not Verified"
    return render_template('result.html',res=res)

if __name__ == "__main__":
    app.run(debug=True)



