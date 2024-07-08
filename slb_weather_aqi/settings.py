ROOT_URLCONF = 'slb_weather_aqi.urls'

OPENWEATHERMAP_KEY = 'dd19b3d5a57d6a6aea546eba672a234b'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'weather_aqi',
]

STATIC_URL = '/static/'

SECRET_KEY = 'dummy'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

CORS_ORIGIN_ALLOW_ALL = True

DEBUG = True

ALLOWED_HOSTS = []
