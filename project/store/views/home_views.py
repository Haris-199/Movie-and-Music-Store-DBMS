from django.shortcuts import redirect


# Redirect to artist list page
def home(request):
    return redirect('artist/')
