# Python 이미지로 시작
FROM python:3.13

WORKDIR /app/src

# 필요한 패키지 설치
RUN pip install --no-cache-dir poetry

# Poetry 환경 설정
RUN poetry config virtualenvs.create false

# 프로젝트 의존성 설치
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

# 프론트엔드 빌드 파일 복사
COPY ../frontend/dist /usr/share/nginx/html

# 백엔드 코드 복사
COPY . /app

# Django 환경 변수 설정
ENV PYTHONPATH="/app"

# Gunicorn 실행
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn --chdir . --bind 0.0.0.0:8000 config.wsgi:application"]

