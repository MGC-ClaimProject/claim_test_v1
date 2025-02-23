import random
from .base import *
from dotenv import dotenv_values

DEBUG = True

ENV = dotenv_values(os.path.join(BASE_DIR, 'prod.env'))
SECRET_KEY = ENV.get(
    "DJANGO_SECRET_KEY",
    "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()?", k=50)),
)

ROOT_URLCONF = "config.urls"
# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": ENV.get("POSTGRES_HOST", "db"),
        "USER": ENV.get("POSTGRES_USER", "postgres"),
        "PASSWORD": ENV.get("POSTGRES_PASSWORD", "postgres"),
        "NAME": ENV.get("POSTGRES_DBNAME", "claim"),
        "PORT": ENV.get("POSTGRES_PORT", 5432),
    }
}

# Static
STATIC_URL = "/static/"
STATIC_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / ".static_root"


# Media
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"


# OAuth
NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID", "")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET", "")

KAKAO_CLIENT_ID = os.getenv("KAKAO_CLIENT_ID", "")
KAKAO_CLIENT_SECRET = os.getenv("KAKAO_CLIENT_SECRET", "")

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")


backend_url = os.getenv("BACKEND_BASE_URL", "").rstrip("/")
KAKAO_CALLBACK_URL = f"{backend_url}/v1/users/login/kakao/callback/"  # 카카오 콜백 URL, 카카오 인증후 리디렉션될 URL

frontend_url = os.getenv("FRONTEND_BASE_URL", "").rstrip("/")
FRONTEND_CALLBACK_URL = f"{frontend_url}/login/?code="
