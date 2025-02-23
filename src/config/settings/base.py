import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ALLOWED_HOSTS = [
    "*",
    "localhost",
    "127.0.0.1",
    "backend",
    "django_app",
    "211.188.62.104",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8000",
    "http://192.168.219.179:8000",
    "http://192.168.219.179:5173",
    "http://211.188.62.104",
    "https://211.188.62.104",
]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = [
    "config",
    "users",
    "common",
    "members",
    "insurances",
    "claims",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "rest_framework",
    "drf_spectacular",
    "rest_framework_simplejwt.token_blacklist",
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS 미들웨어 추가
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8000",
    "http://192.168.219.179:8000",
    "http://192.168.219.179:5173",
    "http://211.188.62.104",
    "https://211.188.62.104",
]

# 모든 Origin 허용 (개발용)
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "OPTIONS",
    "PATCH",
]
CORS_ALLOW_HEADERS = [
    "Authorization",
    "Content-Type",
]
CORS_ALLOW_ALL_ORIGINS = True

# settings.py
SESSION_ENGINE = "django.contrib.sessions.backends.db"  # ✅ 데이터베이스 기반 세션
SESSION_COOKIE_SECURE = (
    False  # ✅ HTTPS가 아닌 환경에서 세션 유지 가능하도록 설정 (로컬 개발 시)
)
SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SAMESITE = "Lax"  # ✅ 프론트엔드와 백엔드 간 쿠키 유지


CSRF_COOKIE_SECURE = False  # HTTPS 환경에서는 True



ROOT_URLCONF = "config.urls"

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "frontend", "build", "static"),
# ]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [os.path.join(BASE_DIR, "frontend", "build")],  # React build directory
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_USER_MODEL = "users.User"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
        "rest_framework.permissions.IsAuthenticated",  # 기본적으로 인증된 사용자만 허용
    ],
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "BLACKLIST_AFTER_ROTATION": True,
    "ROTATE_REFRESH_TOKENS": True,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "CLAIM",  # 스웨거 문서의 제목
    "DESCRIPTION": "보험 청구 간편 서비스",  # 스웨거 문서의 설명
    "VERSION": "1.0.0",  # API 버전
    "SERVE_INCLUDE_SCHEMA": False,  # 스웨거 UI에 스키마 포함 여부
    "SERVE_PERMISSIONS": [
        "rest_framework.permissions.AllowAny"
    ],  # 인증된 사용자만 접근 가능
}


# 카카오 oauth

KAKAO_LOGIN_URL = "https://kauth.kakao.com/oauth/authorize"  # 카카오 로그인 URL, 카카오 로그인 요청 URL,인증페이지로 이동
KAKAO_TOKEN_URL = "https://kauth.kakao.com/oauth/token"  # 카카오 액세스 토큰 URL, 인증코드로 액세스토큰을 교환하는 URL,리프레쉬?
KAKAO_USER_INFO_URL = "https://kapi.kakao.com/v2/user/me"  # 카카오 사용자 정보 URL, 카카오 사용자 정보를 가져오기 위한 URL
KAKAO_ACCESS_TOKEN_INFO_URL = "https://kapi.kakao.com/v1/user/access_token_info"  # 액세스 토큰 정보 확인 URL, 발급된 액세스 토큰의 유효성을 확인하기 위한 URL
