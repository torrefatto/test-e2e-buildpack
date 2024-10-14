import os
from setuptools import setup

with open("./src/static/test_env.txt", "w") as f:
    f.write(os.environ.get("TEST_ENV", ""))

with open("./src/static/test_secret.txt", "w") as f:
    f.write(os.environ.get("TEST_SECRET", ""))

with open("./requirements.txt", "r") as f:
    requirements_txt = f.read()
    requirements = requirements_txt.split("\n")

setup(
    name="test-e2e-buildpack",
    version="1.0",
    long_description=__doc__,
    packages=["src"],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
)
