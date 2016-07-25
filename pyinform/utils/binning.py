# Copyright 2016 ELIFE. All rights reserved.
# Use of this source code is governed by a MIT
# license that can be found in the LICENSE file.
import numpy as np

from ctypes import byref, c_double, c_int, c_ulong, POINTER
from pyinform import _inform
from pyinform.error import ErrorCode, error_guard

def range(series):
    """
    Compute the range of a continuously-valued timeseries.
    """
    xs = np.asarray(series, dtype=np.float64)
    data = xs.ctypes.data_as(POINTER(c_double))

    min, max = c_double(), c_double()
    
    e = ErrorCode(0)
    rng = _inform_range(data, c_ulong(len(xs)), byref(min), byref(max), byref(e))
    error_guard(e)
    
    return rng, min.value, max.value

def bin_series(series, b):
    """
    Bin a continuously-valued timeseries into `b` uniform bins
    """
    xs = np.asarray(series, dtype=np.float64)
    shape = xs.shape
    data = xs.ravel().ctypes.data_as(POINTER(c_double))

    binned = np.empty(xs.size, dtype=np.int32)
    out = binned.ctypes.data_as(POINTER(c_int))

    e = ErrorCode(0)
    step = _inform_bin(data, c_ulong(xs.size), c_int(b), out, byref(e))
    error_guard(e)

    binned = np.reshape(binned, shape)

    return binned, step


_inform_range = _inform.inform_range
_inform_range.argtypes = [POINTER(c_double), c_ulong, POINTER(c_double), POINTER(c_double), POINTER(c_int)]
_inform_range.restype = c_double