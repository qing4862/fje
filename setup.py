from setuptools import setup, find_packages

setup(
    name="FunnyJSONExplorer",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fje=fje.json_explorer:main"
        ]
    },
    install_requires=[
        # 当前没有额外的依赖
    ],
)
