#
# Author: Logan Gunthorpe <logang@deltatee.com>
# Copyright (c) Deltatee Enterprises Ltd. 2015, All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3.0 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library.

try:
    from .d2xx import list_devices, D2XXException
    from .d2xx import D2xx as Ft232
    from .d2xx import D2XXException as Ft232Exception

except OSError:
    from .libftdi import list_devices, LibFtdiException
    from .libftdi import LibFtdi as Ft232
    from .libftdi import LibFtdiException as Ft232Exception

from .mpsse import SPI, GPIO
from .boards import FT232H, FT2232H, FT2232D, FT4232H