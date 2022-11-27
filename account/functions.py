from account.utils import otp_generator
import json
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
def jsonDjangoTupple(jsonData):
    dicOfTupple = dict()
    for key, valueList in jsonData.items():
        dicOfTupple[str(key)]=[(value,value) for value in valueList]
    return dicOfTupple
def try_except_model(model,to,type):

    try:
        if type=="user":
            self_model = model.objects.get(user=to)
        elif type=="id":
            self_model = model.objects.get(id=to)
    except:
        self_model=None
    return self_model