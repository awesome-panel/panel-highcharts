"""Module of Invoke tasks regarding CODE QUALITY to be invoked from the command line. Try

invoke --list

from the command line for a list of all available commands.
"""

from invoke import task


@task
def bandit(command):
    """Runs Bandit the security linter from PyCQA."""
    print(
        """
Running Bandit the Python Security Linter
to identify common security issues in Python code
=================================================
"""
    )
    command.run("bandit -r ./", echo=True)


@task
def black(command):
    """Runs black (autoformatter) on all .py files recursively"""
    print(
        """
Running Black the Python code formatter
=======================================
"""
    )
    command.run("black .", echo=True)


@task
def isort(command):
    """Runs isort (import sorter) on all .py files recursively"""
    print(
        """
Running isort the Python code import sorter
===========================================
"""
    )
    command.run("isort .", echo=True)


@task
def pytest(
    command,
    test_files="tests",
    integrationtest=False,
    test_results="test_results",
    open_results=True,
):
    """Runs pytest to identify failing tests

    Arguments:
        command {[type]} -- Invoke command object

    Keyword Arguments:
        root_dir {str} -- The directory from which to run the tests
        test_files {str} -- A space separated list of folders and files to test. (default: {'tests})
        integrationtest {bool} -- If True tests marked integrationtest or functionaltest will be
            run. Otherwise not. (default: {False})
        test_results {string} -- If not None test reports will be generated in the test_results
            folder
        open_results {bool} -- If True test reports in the 'test_results' folder will be opened in
            a browser

    # Print running pytest
    """
    print(
        """
Running pytest the test framework
=================================
"""
    )
    # Build the command_string
    command_string = f"pytest {test_files} --doctest-modules --cov=panel_highcharts"
    if not integrationtest:
        command_string += ' -m "not functionaltest and not integrationtest"'
    if test_results:
        # command_string += f" --junitxml={test_results}/test-results-api.xml"
        command_string += f" --cov-report html:{test_results}/cov_html"

    # Run the command_string
    command.run(command_string, echo=True)

    # Open the test coverage report in a browser
    if test_results and open_results:
        command.run("start test_results/cov_html/index.html")


@task()
def pylint(command, files="setup.py tasks panel_highcharts tests"):
    """Runs pylint (linter) on all .py files recursively to identify coding errors

    Arguments:
        command {[type]} -- [description]
        files {string} -- A space separated list of files and folders to lint
    """
    # https://stackoverflow.com/questions/22241435/pylint-discard-cached-file-state
    # from astroid import MANAGER
    # MANAGER.astroid_cache.clear()
    print(
        """
Running pylint.
Pylint looks for programming errors, helps enforcing a coding standard,
sniffs for code smells and offers simple refactoring suggestions.
=======================================================================
"""
    )
    command_string = f"pylint {files}"
    command.run(command_string, echo=True)


@task
def mypy(command, files="setup.py tasks panel_highcharts tests"):
    """Runs mypy (static type checker) on all .py files recursively

    Arguments:
        command {[type]} -- [description]
        files {string} -- A space separated list of files and folders to lint
    """
    print(
        """
Running mypy for identifying python type errors
===============================================
"""
    )
    command_string = f"mypy {files}"
    command.run(command_string, echo=True)


@task
def autoflake(command):
    """Runs autoflake to remove unused imports on all .py files recursively

    Arguments:
        command {[type]} -- [description]
    """
    print(
        """
Running autoflake to remove unused imports on all .py files recursively
=======================================================================
"""
    )
    # command.run("RUN rm -rf .mypy_cache/; exit 0")
    command.run(
        "autoflake --imports=pytest,pandas,numpy,plotly,dash,urllib3 --in-place --recursive .",
        echo=True,
    )


@task(
    pre=[isort, autoflake, black, pylint, mypy, pytest],
    aliases=["pre_commit", "test"],
    name="all",
)
def _all(command):  # pylint: disable=unused-argument
    """Runs isort, autoflake, black, pylint, mypy and pytest

    Arguments:
        command {[type]} -- [description]
    """
    # If we get to this point all tests listed in 'pre' have passed
    # unless we have run the task with the --warn flag
    if not command.config.run.warn:
        print(
            """
All Tests Passed Successfully
=============================
"""
        )
