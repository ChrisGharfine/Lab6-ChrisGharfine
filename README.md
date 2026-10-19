# Lab 6 Automatic Builds

Chris Gharfine

This repository completes the graded calculator exercise and both optional
Makefile examples. Each project can be run from its own directory. Python 3.12,
pip, and GNU Make are required; the calculator only requires Python and pip.

## Setup

Virtual environment setup at the repository root:

```console
python -m venv .venv
```

Activation uses `.venv\Scripts\Activate.ps1` in Windows PowerShell or
`source .venv/bin/activate` on Linux/macOS. The commands below assume an active
environment and Python 3.12 available as `python`.

## Graded calculator exercise

```console
cd calculator_Chris_Gharfine
python -m pip install -r requirements.txt
pyb run_unit_tests
python -m unittest tests.unittest.calculator_Chris_Gharfine.test_calculator_Chris_Gharfine -v
pyb clean install_build_dependencies run_unit_tests publish
```

The package implements `add(x, y)`, `subtract(x, y)`, `multiply(x, y)`,
`divide(x, y)`, `modulus(x, y)`, `power(x, y)`, and `square_root(x)`.
Division and modulus reject a zero divisor with `ValueError`. Square root
rejects negative inputs with `ValueError`. Modulus follows Python's `%`
semantics, including for negative numbers; exponentiation follows `**`.

PyBuilder discovers the `test_*.py` files under `tests`, runs 21 unit tests,
and generates distribution files under `target/dist`. A plain `pyb` runs the
default `publish` task, including testing and packaging. Dependencies are
installed automatically into PyBuilder's isolated build environments.

Build evidence is included in [the calculator console screenshot](screenshots/calculator-build.jpg).
It captures the actual GitHub Actions build output showing 21 passing tests,
`BUILD SUCCESSFUL`, the base directory containing `calculator_Chris_Gharfine`,
the finish timestamp, and the elapsed time of 14 seconds. The image is an
unmodified capture of [the successful build console](https://github.com/ChrisGharfine/Lab6-ChrisGharfine/actions/runs/39244506465/job/118033042952).
The [workflow summary screenshot](screenshots/workflow-success.jpg) shows the
successful verification of all three projects. These are GitHub Actions captures.

## Optional standalone Makefile exercise

From the repository root:

```console
cd makefile_greeting
make install
make test
make lint
make package
make clean
```

`app.py` prints `Hello, World!` when run with `python app.py`.
The Makefile targets perform these tasks:

| Target | Task |
| --- | --- |
| `install` | Install the pinned linting and packaging tools. |
| `test` | Discover and execute the greeting unit tests. |
| `lint` | Check source, tests, and packaging configuration with flake8. |
| `package` | Build a source archive and wheel in `dist`. |
| `clean` | Remove generated packages, metadata, and Python caches. |

Packaging uses `python -m build`, replacing the legacy direct `setup.py`
invocation while retaining the required source archive and wheel outputs.
The clean recipe uses Python so it also works on Windows without Unix commands.

## Optional combined PyBuilder and Makefile exercise

From the repository root:

```console
cd my_python_project
python -m pip install -r requirements.txt
make all
```

| Target | Task |
| --- | --- |
| `install_deps` | Install the pinned PyBuilder version. |
| `clean` | Run `pyb clean` to remove generated build output. |
| `test` | Run the three greeting tests through PyBuilder. |
| `build` | Run `pyb publish` to test and create distribution packages. |
| `all` | Run dependency installation, cleanup, tests, and packaging in order. |

`build` uses `publish` because that PyBuilder task produces the source archive
and wheel. PyBuilder generates its packaging configuration in `target`.
The Makefile gives repeatable names to the longer build commands and enforces
the order of the complete workflow, including when Make is invoked with `-j`.
Both Makefiles accept `PYTHON`; the combined one also accepts `PYB` overrides.

## Automated checks

The GitHub Actions workflow runs on pushes to `main`, pull requests, and manual
dispatch. It checks the calculator with both runners, runs every Makefile
target, verifies cleanup preserves source files, and builds all three projects
with Python 3.12.

Make reduces repetitive typing, keeps commands consistent between computers,
and provides a convenient entry point for automated checks. PyBuilder adds
dependency management, test execution, and packaging through its task graph.

Generated environments, caches, and distributions are ignored by Git. The
repository contains the code and configuration needed to reproduce them.
