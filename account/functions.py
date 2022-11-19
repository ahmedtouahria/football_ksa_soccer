from account.utils import otp_generator
import requests
def send_otp(phone):
    """
    This is an helper function to send otp to session stored phones or 
    passed phone number as argument.
    """

    if phone:

        key = otp_generator()
        phone = str(phone)
        otp_key = str(key)
        print("otp",otp_key)
        link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=7c59cf94-d129-11ec-9c12-0200cd936042&to={phone}&from=MMBook&templatename=mymedbook&var1={otp_key}&var2={otp_key}'

        result = requests.get(link, verify=False)

        return otp_key
    else:
        return False
