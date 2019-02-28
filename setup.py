setup(
    name='Anchor',
    version='1.0',
    py_modules=['customCli'],
    install_requires=[
        'Click', 'requests'
    ],
    entry_points='''
        [console_scripts]
        hello=welcome:cli,
    ''',
)
