import os
import random
from dotenv import load_dotenv, dotenv_values

from .base import *

# 먼저 루트의 .env 파일을 로드해서 MODE 등 기본 환경변수를 설정합니다.
load_dotenv(os.path.join(BASE_DIR, ".env"))

# .env 파일에 정의된 MODE 값을 읽어오며, 없으면 기본값은 "prod"로 사용합니다.
mode = os.getenv("MODE", "local")

# MODE에 따라 해당하는 env 파일을 로드합니다. 예를 들어, MODE가 prod라면 prod.env 파일을 로드합니다.
ENV = dotenv_values(os.path.join(BASE_DIR, f"{mode}.env"))

SECRET_KEY = ENV.get(
    "DJANGO_SECRET_KEY",
    "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()?", k=50)),
)

ROOT_URLCONF = "config.urls"

# Database 설정
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
KAKAO_CALLBACK_URL = f"{backend_url}/v1/users/login/kakao/callback/"

frontend_url = os.getenv("FRONTEND_BASE_URL", "").rstrip("/")
FRONTEND_CALLBACK_URL = f"{frontend_url}/login/?code="
