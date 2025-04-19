
rm -r dist
rm -r build
mkdir build
mkdir dist
pyinstaller  -F -w --icon=default.ico --name CompoundPendulum  app.py
cp default.ico dist/
cp compoundpendulum.jpg dist/
zip -r pendulum.zip dist