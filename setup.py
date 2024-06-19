from setuptools import setup, find_packages

setup(
    name='pfhedge',  # The name of your package
    version='0.1.0',  # Initial release version
    description='A stock simulation package',  # Short description
    long_description=open('README.md').read(),  # Long description read from README.md
    long_description_content_type='text/markdown',  # Content type of long description
    author='Your Name',  # Your name
    author_email='your.email@example.com',  # Your email
    url='https://github.com/yourusername/mystock',  # URL of your package or GitHub repo
    packages=find_packages(),  # Automatically find packages in the directory
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum version requirement of Python
    install_requires=[
        # List your package dependencies here
        # e.g., 'numpy', 'pandas'
    ],
    include_package_data=True,  # Include other files specified in MANIFEST.in
)