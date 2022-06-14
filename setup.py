from setuptools import setup, find_packages


setup(
    name='pyqt-animated-svg-example',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_animated_svg_example.ico': ['rolling.svg']},
    description='PyQt animated SVG example',
    url='https://github.com/yjg30737/pyqt-animated-svg-example.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)