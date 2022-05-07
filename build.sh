rm -rf build
rm -rf dist
rm -rf app.spec
pyinstaller -F --clean ./app.py