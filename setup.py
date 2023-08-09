import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mock_cmd',
    version="0.1",
    author='CSST Team',
    author_email='bozhang@nao.cas.cn',
    description='The CSST L1 pipeline - common modules',  # short description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://csst-tb.bao.ac.cn/code/csst-l1/csst_common',
    project_urls={
        'Source': 'https://csst-tb.bao.ac.cn/code/csst-l1/csst_common',
    },
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Intended Audience :: Science/Research",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python :: 3.8",
                 "Topic :: Scientific/Engineering :: Physics",
                 "Topic :: Scientific/Engineering :: Astronomy"],
    package_dir={'mock_cmd': 'mock_cmd'},
    # include_package_data=True,
    package_data={"": ["LICENSE", "README.md"],
                  "mock_cmd": ["data/*"]},
    # install_requires=['sphinx',
    #                   'numpy',
    #                   'scipy', 'matplotlib',
    #                   'astropy', 'healpy', 'ccdproc', 'deepCR', 'photutils'],
    python_requires='>=3.8',
)
