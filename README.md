# DAQControl

DAQControl is a test software application intended for demonstrating the command-response operation of openDAQ.
This demo is compatible with Python 3.X.
* * *
**OpenDAQ** is an open source data acquisition instrument, which provides user
several physical interaction capabilities such as analog inputs and outputs,
digital inputs and outputs, timers and counters.

Through a USB connection, openDAQ brings all the information that it captures
to a host computer, where you can decide how to process, display and store it.
Several demos and examples are provided in website's support page.
(http://www.open-daq.com/paginas/support)

Please, go to http://www.open-daq.com for additional info.
For support, e-mail to support@open-daq.com
* * *
## Installation

You will need **administrator rights** (root access) to install this package
system-wide.

DAQControl demo will require to install **matplotlib** and **PyQt5** packages. To install them:

```sh
    $ pip3 install matplotlib==2.2.5
    $ pip3 install pyqt5
```

**DAQControl**

To install the last stable version:


```sh
    $ pip3 install daqcontrol
```

To install the development version (it is highly recommended to use a
[virtual environment](https://virtualenv.pypa.io/en/stable/) for this):

```sh
    $ git clone github.com/opendaq/daqcontrol
    $ cd daqcontrol
    $ python setup.py install
```

In any case, if for any reason the setup fails, DAQControl demo will require these **others packages**:

- opendaq

- setuptools

- numpy

- serial

All these packages are available on pip. To install them:

```sh
    $ pip3 install "package"
```
