import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cirq_multiplexer",
    version="0.0.1",
    description="Multiplexers for quantum circuits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahirth/quantum_circuit_multiplexers",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['cirq==0.10.0.dev20210219235859']
)
