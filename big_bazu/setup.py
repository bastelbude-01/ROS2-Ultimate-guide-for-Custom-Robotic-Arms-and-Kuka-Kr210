from setuptools import setup
import os
from glob import glob 

package_name = 'big_bazu'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        (os.path.join('share', package_name,'launch'), glob('launch/*')),
        
        (os.path.join('share', package_name,'urdf'), glob('urdf/*')),

        (os.path.join('share', package_name,'config'), glob('config/*')),


    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luqman',
    maintainer_email='noshluk2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'trajectory_msg = big_bazu.control_bazu:main'
        ],
    },
)
