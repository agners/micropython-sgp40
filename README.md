# Sensirion SGP40 VOC Sensor I2C driver for MicroPython

Sensirion SGP40 is a digital VOC (volatile organic compound) sensor. This
is a I2C driver written in Python 3 for MicroPython.

## Getting Started

### Prerequisites

* Sensirion SGP40 Sensor Module
* MicroPython board with I2C interface

### Wiring

Wire the I2C bus to the I2C bus on your MicroPython board. This is an example
using the Pyboard D:

| Pyboard       | SGP40         |
| ------------- |---------------|
| X15 (3V3)     | VDD           |
| X14 (GND)     | GND           |
| X9            | SCL           |
| X10           | SDA           |

### Usage

This example reads the measurements in a continous loop:

```
import time
from machine import I2C, Pin
from sgp40 import SGP40

i2cbus = I2C(1)
sgp40 = SGP40(i2c, 0x59)

while True:
    sgp40.measure_raw()
    time.sleep(1)
```

This returns raw data from the sensor. The data is meant to be processed by
the Sensirion specific VOC Algorithm, which returns air quality reflected by
an index.

## Built With

* [MicroPython](http://micropython.org/)
* [SGP40 Sensor Module](https://www.sensirion.com/en/environmental-sensors/gas-sensors/sgp40/)

## License

This project is licensed under the MIT License - see the
[LICENSE](LICENSE) file for details

