from django.http import JsonResponse

def root_view(request):
    data = {
        "message": "Welcome to the Asset Management System API",
        "endpoints": {
            "admin": "/admin/",
            "asset_data": "/asset-data/"
        },
        "description": "This server manages asset data and prices. Use the provided endpoints to interact with the API."
    }
    return JsonResponse(data)