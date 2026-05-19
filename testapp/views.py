from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Tshirt, Order
from .forms import OrderForm


def home(request):

    tshirts = Tshirt.objects.all()

    paginator = Paginator(tshirts, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'testapp/home.html', {'page_obj': page_obj})


def detail(request, id):

    tshirt = get_object_or_404(Tshirt, id=id)

    return render(request, 'testapp/detail.html', {'tshirt': tshirt})


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

            return render(request, 'testapp/success.html')

    return render(request, 'testapp/buy.html', {'form': form, 'tshirt': tshirt})


def history(request):

    orders = Order.objects.all()

    return render(request, 'testapp/history.html', {'orders': orders})


def contact(request):

    return render(request, 'testapp/contact.html')