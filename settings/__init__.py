# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import os, sys
from django.core.management import call_command

try:
    print("Trying import prod.py settings...", file=sys.stderr)
    from .prod import *
except ImportError:
    print("Trying import dev.py settings...", file=sys.stderr)
    from .dev import *