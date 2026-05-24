from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="supervision",
    version="0.1.0",
    author="Roboflow",
    author_email="help@roboflow.com",
    description="A set of easy-to-use utils that will come in handy in any Computer Vision project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roboflow/supervision",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "docs.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "isort>=5.0.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
            # added ipykernel so I can use this in jupyter notebooks easily
            "ipykernel>=6.0.0",
        ],
    },
)
