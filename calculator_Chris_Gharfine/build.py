"""PyBuilder build descriptor for Chris Gharfine's calculator."""

from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "calculator_Chris_Gharfine"
version = "0.1"
default_task = "publish"
summary = "Lab 6 calculator by Chris Gharfine"
author = "Chris Gharfine"


@init
def initialize(project):
    project.set_property(
        "dir_source_unittest_python",
        "tests/unittest/calculator_Chris_Gharfine",
    )
    project.set_property("unittest_module_glob", "test_*")
