import setuptools

import numpy

# Setup just to build the numpy extension
setuptools.setup(
    ext_modules=[
        setuptools.Extension(
            "online_cc",
            sources=["onset_fingerprinting/c/cross_corr.c"],
            include_dirs=[numpy.get_include()],
        )
    ]
)
