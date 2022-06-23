from django.core.mail import send_mail
from django.http import HttpResponse
def simple_email(request):
    print("Hello world")
    send_mail("Testing", "Sending via cron job.",'testingclt4@gmail.com', ['prabhat.namdharani@gmail.com'] ) 
    return HttpResponse("<h2>Thank you mail sent</h2>")