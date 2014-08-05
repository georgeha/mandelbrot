radical-pilot
=============

<h1> Requirements: </h1>

radical-pilot has the following requirements:


RADICAL-Pilot needs Python >= 2.6. All dependencies are installed automatically by the installer. Besides that, RADICAL-Pilot needs access to a MongoDB database that is reachable from the internet. User groups within the same institution or project can share a single MongoDB instance.

<h2> To run the Mandelbrot example you need to install the following: </h2>

You can find more information and the executables about the two implementations in the folders: mandelbrot_core and mandelbrot_core

<h3> -Create a virtual environment: </h3>

```
virtualenv $HOME/myenv
source $HOME/myenv/bin/activate
```

<h3> -install radical.pilot: </h3>

```
pip install radical.pilot:
```

<h3> - Install MongoDB: </h3>

Linux User:

```
apt-get -y install scons libssl-dev libboost-filesystem-dev libboost-program-options-dev libboost-system-dev libboost-thread-dev
git clone -b r2.6.3 https://github.com/mongodb/mongo.git
cd mongo
scons --64 --ssl all
scons --64 --ssl --prefix=/usr install
```
Mac User:

```
brew install mongodb --with-openssl
```
then: Crete a Data directory:
```
mkdir -p /data/db
```
set read & write permissions to this folder:
```
chmod 755 /data/db
```
Run MongodB:
```
mongod
```

<h3> - Install PIL Image: </h3>

```
pip install Pillow

```

More information about the radical.pilot project can be found here:

[Radical.Pilot](http://radical-cybertools.github.io/radical-pilot/index.html)


