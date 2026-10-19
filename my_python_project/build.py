"""PyBuilder build descriptor for the combined optional exercise."""

from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "my_python_project"
version = "1.0"
default_task = "publish"
summary = "Lab 6 PyBuilder and Makefile greeting example"
author = "Chris Gharfine"


@init
def initialize(project):
    project.set_property("unittest_module_glob", "test_*")
