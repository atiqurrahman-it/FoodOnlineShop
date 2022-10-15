# views.py er data control korte parbo ....sob html file data er access pabe 
# alada alada  kore  view e data={} likh te  hobe na 

from vendor.models import Vendor

def get_all_data_vendor(request):
    try:
        vendor=Vendor.objects.get(user=request.user)
    except:
        # if logout 
        vendor=None

    data={
        'vendor':vendor,

    }
    return dict(data)