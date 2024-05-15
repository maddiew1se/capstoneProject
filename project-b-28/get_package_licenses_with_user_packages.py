
import requests
from bs4 import BeautifulSoup

def get_package_license(package_name):
    # Retrieve package info from PyPI
    url = f"https://pypi.org/project/{package_name}/"
    response = requests.get(url)
    
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the license information in the sidebar
        for div in soup.find_all('div', class_='sidebar-section'):
            if 'License' in div.get_text():
                return div.get_text(strip=True).replace('License:', '').strip()
    return "Not Found"

# The full list of packages from the user's environment.
packages = [
    "Faker", "PyJWT", "asgiref", "beautifulsoup4", "boto3", "botocore",
    "certifi", "cffi", "charset-normalizer", "cryptography", "defusedxml",
    "dj-database-url", "django-allauth", "django-bootstrap-v5", "django-bootstrap5",
    "django-haystack", "django-heroku", "django-js-asset", "django-mptt",
    "django-storages", "django-widget-tweaks", "factory-boy", "gunicorn", "idna",
    "iniconfig", "jmespath", "markdown2", "oauthlib", "packaging", "pillow", "pip",
    "pluggy", "psycopg2", "psycopg2-binary", "pycparser", "pytest", "python-dateutil",
    "python3-openid", "requests", "requests-oauthlib", "s3transfer", "setuptools",
    "six", "soupsieve", "sqlparse", "typing_extensions", "tzdata", "urllib3", "wheel",
    "whitenoise"
]

for package in packages:
    license = get_package_license(package)
    print(f"{package}: {license}")
