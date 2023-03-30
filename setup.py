import setuptools
import os

kwargs = {}

if os.path.isfile("requirements.txt"):
    with open('requirements.txt') as f:
        kwargs["install_requires"] = f.read().splitlines()

setuptools.setup(
    name="Mocniny",
    version="1.0",
    author="Filip Polák",
    author_email="polakf@kky.zcu.cz",
    description="Example dialog manager for SpeechCloud platform",
    url="https://github.com/Filipfill123/mocniny",
    data_files=[("static", ["index.html"])],
    py_modules=["mocniny"],
    python_requires='>=3.7',
    **kwargs
)
