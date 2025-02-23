from django.shortcuts import render
from django.http import JsonResponse
from django.db import connections


def index(request):
    return render(request, "index.html")  # ✅ 프론트엔드 index.html 서빙



def health_check(request):
    try:
        # 데이터베이스 연결 확인
        connections['default'].cursor()
        return JsonResponse({"status": "ok"}, status=200)
    except Exception as e:
        return JsonResponse({"status": "error", "detail": str(e)}, status=500)
