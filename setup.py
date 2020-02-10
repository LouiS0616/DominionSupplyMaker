import os
import sys
from setuptools import setup, find_packages


# References
#   numpy's setup.py
#   https://github.com/numpy/numpy/blob/943695bddd1ca72f3047821309165d26224a3d12/setup.py

def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    with open('README.md') as f:
        readme = f.read()

    metadata = dict(
        name='dominion_supply_maker',
        version='0.8.0',
        description='',
        long_description=readme,
        long_description_content_type='text/markdown',
        python_requires='>=3.7',
        author='LouiSakaki',
        author_email='e1352207@outlook.jp',
        url='https://github.com/LouiS0616/DominionSupplyMaker',
        license='MIT',
        packages=find_packages(),

        install_requires=[
            'pyyaml', 'sortedcontainers', 'tqdm',
        ],
        package_data={
            'supply_maker': [
                'res/kingdom_cards/*.csv', 'res/translate/**/*.csv', 'res/constraints.yml',
            ]
        }
    )

    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)
    return


if __name__ == '__main__':
    setup_package()