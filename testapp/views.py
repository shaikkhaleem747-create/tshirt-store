from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TshirtSerializer, OrderSerializer

from .models import Tshirt, Order
from .forms import OrderForm


def signup(request):

    error = ""

    if request.method == "POST":

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            return redirect('/login/')

        else:

            error = "Passwords are not matching"

    return render(request, 'testapp/signup.html', {'error': error})


def userlogin(request):

    error = ""

    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/')

        else:

            error = "Invalid Username or Password"

    return render(request, 'testapp/login.html', {'error': error})


def userlogout(request):

    logout(request)

    return redirect('/login/')


@login_required(login_url='/login/')
def home(request):

    tshirts = Tshirt.objects.all()

    paginator = Paginator(tshirts, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'testapp/home.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def detail(request, id):

    tshirt = get_object_or_404(Tshirt, id=id)

    return render(request, 'testapp/detail.html', {'tshirt': tshirt})


@login_required(login_url='/login/')
def buy(request, id):

    tshirt = get_object_or_404(Tshirt, id=id)

    form = OrderForm()

    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.tshirt_name = tshirt.name

            order.price = tshirt.price

            order.total_amount = tshirt.price * order.quantity

            order.save()

            return redirect('/history/?success=1')

    return render(request, 'testapp/buy.html', {'form': form, 'tshirt': tshirt})


@login_required(login_url='/login/')
def history(request):

    orders = Order.objects.all()

    return render(request, 'testapp/history.html', {'orders': orders})


@login_required(login_url='/login/')
def clearhistory(request):

    Order.objects.all().delete()

    return redirect('/history/')


@login_required(login_url='/login/')
def contact(request):

    return render(request, 'testapp/contact.html')


@api_view(['GET'])
def tshirt_api(request):

    tshirts = Tshirt.objects.all()

    serializer = TshirtSerializer(tshirts, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def order_api(request):

    orders = Order.objects.all()

    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)