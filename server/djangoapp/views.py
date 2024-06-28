from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json

from .models import CarMake, CarModel
from .populate import initiate
from .restapis import get_request, analyze_review_sentiments, post_review

logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data["userName"]
    password = data["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)


def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})


@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data["userName"]
    email = data["email"]
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(
            username=username,
            first_name=data["firstName"],
            last_name=data["lastName"],
            password=data["password"],
            email=email,
        )
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    return JsonResponse({"userName": username, "error": "Already Registered"})


def get_cars(request):
    if CarMake.objects.count() == 0:
        initiate()
    cars = [
        {"CarModel": car_model.name, "CarMake": car_model.car_make.name}
        for car_model in CarModel.objects.select_related("car_make")
    ]
    return JsonResponse({"CarModels": cars})


def get_dealerships(request, state="All"):
    endpoint = "/fetchDealers" + ("/" + state if state != "All" else "")
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        reviews = get_request(f"/fetchReviews/dealer/{dealer_id}")
        for review in reviews:
            review["sentiment"] = analyze_review_sentiments(review["review"])[
                "sentiment"
            ]
        return JsonResponse({"status": 200, "reviews": reviews})
    return JsonResponse({"status": 400, "message": "Bad Request"})


def get_dealer_details(request, dealer_id):
    if dealer_id:
        dealership = get_request(f"/fetchDealer/{dealer_id}")
        return JsonResponse({"status": 200, "dealer": dealership})
    return JsonResponse({"status": 400, "message": "Bad Request"})


def add_review(request):
    if request.user.is_anonymous is False:
        data = json.loads(request.body)
        try:
            post_review(data)
            return JsonResponse({"status": 200})
        except Exception as e:
            return JsonResponse(
                {
                    "status": 401,
                    "message": "Error in posting review",
                    "error": str(e)
                }
            )
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})
