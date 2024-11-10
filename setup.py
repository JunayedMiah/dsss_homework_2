from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here if needed
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  # Maps the CLI command to the function
        ],
    },
    author="junay",
    author_email="junayed.miah7667@gmail.com",
    description="A math quiz game to test arithmetic skills",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/JunayedMiah/dsss_homework_2.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
