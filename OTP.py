from flask import Flask, render_template, request
import smtplib
import pyotp

OTP=""

# generate a secret key
secret_key = pyotp.random_base32()

# create a TOTP object using the secret key
totp = pyotp.TOTP(secret_key)

# generate an OTP
OTP = totp.now()
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Email ID", "App Password")

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
