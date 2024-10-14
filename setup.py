import os
from setuptools import setup

with open("./src/static/test_env.txt", "w") as f:
    f.write(os.environ.get("TEST_ENV", ""))

with open("./src/static/test_secret.txt", "w") as f:
    f.write(os.environ.get("TEST_SECRET", ""))

requirements = [
    "click==8.1.3",
    "Flask==2.2.2",
    "gunicorn==20.1.0",
    "itsdangerous==2.1.2",
    "Jinja2==3.1.2",
    "MarkupSafe==2.1.1",
    "Werkzeug==2.2.2",
]

setup(
    name="test-e2e-buildpack",
    version="1.0",
    long_description=__doc__,
    packages=["src"],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
)
