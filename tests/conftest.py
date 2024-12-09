"""
Test Environment Configuration.

This module sets up the environment required for automated tests.
It adds the project's root directory to the `sys.path`, enabling proper
importing of project modules.

Structure:
- Configures the project's base path before running the tests.

Usage:
There is no need to explicitly call this file. It will be automatically
loaded by Pytest before executing the tests.
"""

import sys
import os

# Adds the project's root directory to sys.path before running the tests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
