from setuptools import find_packages, setup

package_name = 'meu_pacote'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/meu_launch.py']),
        ('share/' + package_name + '/worlds', ['worlds/simple_room_with_gaps.world']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'meu_no = meu_pacote.meu_no:main', 
            'meu_segundo_no = meu_pacote.meu_segundo_no:main', 
            'meu_terceiro_no = meu_pacote.meu_terceiro_no:main',
            'publisher = meu_pacote.publisher:main',
            'subscriber = meu_pacote.subscriber:main',
            'r2d2 = meu_pacote.r2d2:main',
        ],
    },
)
