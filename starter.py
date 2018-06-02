"""Quandl hitting script."""

import sys
import quandl

data = quandl.get("FRED/GDP")
print(data)
