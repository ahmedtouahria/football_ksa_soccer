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
        return otp_key
    else:
        return False
