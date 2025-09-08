from setuptools import setup, find_packages

setup(
    name='selenium-automation',
    version='1.0.0',
    packages=find_packages(),  # 自動抓取所有含 __init__.py 的資料夾
    install_requires=[],       # 如果有額外安裝需求可加進來，但你已經用 requirements.txt 安裝了
    author='Matrix Zhang',
    description='Automation testing project for web and API using Selenium and Pytest',
    include_package_data=True,
    python_requires='>=3.8',
)
