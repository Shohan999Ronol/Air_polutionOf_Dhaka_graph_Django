from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')
    

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


# from home.models import line_charts1
# from home.models import CO2
# from django.http import HttpResponse
# from django.shortcuts import render
# from invoices.models import Invoice
# import plotly.express as px

# Create your views here.
# def index(request):
#     return render(request, 'index.html')


# def ch1(request):
#     # start = request.GET.get('start')
#     # end = request.GET.get('end')

#     co2 = CO2.objects.all()
#     # if start:
#     #     co2 = co2.filter(date__gte=start)
#     # if end:
#     #     co2 = co2.filter(date__lte=end)

#     fig = px.line(
#         x=[c.div for c in co2],
#         y=[c.pmm for c in co2],
#         title="CO2 PPM",
#         labels={'x': 'Date', 'y': 'CO2 PPM'}
#     )

#     fig.update_layout(
#         title={
#             'font_size': 24,
#             'xanchor': 'center',
#             'x': 0.5
#     })
#     chart = fig.to_html()
#     context = {'ch1': ch1}
#     return render(request, 'ch1.html', context)



def ch1(request):
    return render(request,'ch1.html')




# def ch2(request):
#     obj = Invoice.objects.get(id=1)
#     qs = Invoice.objects.all()
#     print(obj.__dict__)
#     print('*****')
#     print(qs.query)
#     return render(request, 'ch2.html', {'obj_': obj})



def ch2(request):
    return render(request,'ch2.html')



# def chart(request):
#     start = request.GET.get('start')
#     end = request.GET.get('end')

#     line_charts1 = line_charts1.objects.all()
#     if start:
#         line_charts1 = line_charts1.filter(date__gte=start)
#     if end:
#         line_charts1 = line_charts1.filter(date__lte=end)

#     fig = px.line(
#         x=[c.date for c in line_charts1],
#         y=[c.average for c in line_charts1],
#         title="CO2 PPM",
#         labels={'x': 'Date', 'y': 'CO2 PPM'}
#     )

#     fig.update_layout(
#         title={
#             'font_size': 24,
#             'xanchor': 'center',
#             'x': 0.5
#     })
#     chart = fig.to_html()
#     context = {'chart': chart}
#     return render(request, 'core/chart.html', context)