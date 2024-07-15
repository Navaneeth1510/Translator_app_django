from django.shortcuts import render, redirect
from django.contrib import messages
from googletrans import Translator
from .models import UserDetails

# Create your views here.
def show_main(request):
    return render(request, "mainpage.html")

def show_signup(request):
    return render(request, "signuppage.html")

def show_login(request):
    return render(request, "loginpage.html")

def translator(request):
    return render(request,"translator.html")


#login authentication
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            if UserDetails.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered.')
            else:
                user = UserDetails(email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful! Please log in.')
                return redirect('http://127.0.0.1:8000/loginpage.html/')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'http://127.0.0.1:8000/sign_up.html/')

def login_auth(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserDetails.objects.get(email=email)
            if user.password == password:
                messages.success(request, 'Login successful!')
                return redirect('http://127.0.0.1:8000/translator/')  # Replace with your desired redirect URL
            else:
                messages.error(request, 'Invalid email or password.')
        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'http://127.0.0.1:8000/loginpage.html/')
       


def translated(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    print('text :',text,'lang :',lang)
    
    translator = Translator()
    print(type(text))
    dt = translator.detect(text)
    dt2 = dt.lang

    translated = translator.translate(text,lang)
    tr = translated.text
    return render(request,"translated.html",{'translated':tr,'from_lang':dt2,'t_lang':lang})