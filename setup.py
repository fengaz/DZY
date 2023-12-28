from setuptools import setup, find_packages

setup(
    name='DZY',  # 项目名称
    version='0.1.0',  # 项目版本
    url='https://github.com/fengaz/DZY',  # 项目的URL
    author='fengaz',  # 作者名字
    author_email='1295138769@qq.com',  # 作者邮箱
    description='lalala',  # 项目简介
    packages=find_packages(),  # 自动发现所有包和子包
    install_requires=[  # 项目依赖
        'streamlit',
        'requests',
        'beautifulsoup4',
        'plotly',
        'jieba',
        'pandas',
        'wordcloud',
        'matplotlib',
        'nltk',
        'Pillow'
    ],
)
