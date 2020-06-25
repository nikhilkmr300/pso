import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pso",
    version="0.0.1",
    author="Nikhil Kumar",
    author_email="nikhilkmr300@gmail.com",
    description="A package that implements the particle swarm optimization algorithm",
    url="https://github.com/nikhilkmr300/pso",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
      'numpy>=1.18',
      'matplotlib>=3.2',
      'tqdm>=4.46'
    ],
    python_requires='>=3.6',
)
