from setuptools import setup

package_name = 'pacote_de_exemplos'

import os
data_files=[
   ('share/ament_index/resource_index/packages',
       ['resource/' + package_name]),
   ('share/' + package_name, ['package.xml']),
]

def package_files(data_files, directory_list):
   paths_dict = {}
   for directory in directory_list:
       for (path, directories, filenames) in os.walk(directory):
           for filename in filenames:
               file_path = os.path.join(path, filename)
               install_path = os.path.join('share', package_name, path)
               if install_path in paths_dict.keys():
                   paths_dict[install_path].append(file_path)
               else:
                   paths_dict[install_path] = [file_path]
   for key in paths_dict.keys():
       data_files.append((key, paths_dict[key]))
   return data_files

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=package_files(data_files, [ 'config/', 'launch/', 'simulation/', 'urdf/']),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Fagner Pimentel',
    maintainer_email='FagnerPimentel@gmail.com',
    description='Pacote com exemplos utilizados no curso "aprendendo_ros2"',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'no_simples = pacote_de_exemplos.no_simples:main',
            'no_com_classe = pacote_de_exemplos.no_com_classe:main',
            'checkpoints = pacote_de_exemplos.checkpoints:main'
        ],
    },
)
