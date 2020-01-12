from setuptools import setup, find_packages

setup(
    name='ha_classes',
    version='0.0.1',
    description='Home Automation Classes',
    url='git@github.com:richvigorito/switch_classes.git',
    author='Rich Vigorito',
    author_email='nicetry.bozo@gmail.com',
    license='unlicense',
    #package_dir={'switch_classes': 'src'},
    #package_dir={'switch_devices': 'src/switch_devices'},
    #package_dir={'switches': 'src'},
    #package_dir={'': 'ha_classes'},
   packages=find_packages(),
 #   packages=['ha_classes','ha_classes.house','ha_classes.device','ha_classes.x10','ha_classes.zwave','ha_classes.parseHouse'],
    include_package_data=True,
   # ext_modules=[Extension('switches.src', ['switches.src','switches.src.house','switches.src.devices'])],
    #packages=['src'],
    #packages=[house,devices,loadhouse]
    #python_requires='>=3.1.*, <4',
    #install_requires=['json'],
    zip_safe=False

)

