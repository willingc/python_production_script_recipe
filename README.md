About
=====

This project demonstrates a collection of best practices for production-ready
Python scripts. It includes an example of a script that *isn't* ready for
production.

Running Tests
=============

    pip install -e .
    tox

Guidelines
==========

* If you run shell commands (e.g. `subprocess.call`), especially ssh,
  consider using a raw shell or a wrapper like
  [fabric](http://www.fabfile.org/) instead of pure Python. Don't obfuscate
  bash with Python, and don't rebuild a wheel that's already built.
* Avoid dependencies on non-core libraries. When this guide was written,
  the Python community often did things like remove versions from pypi that
  made it expensive to manage dependencies in production. If you ended up with
  a dep chain it was likely you were better off building the feature into your
  application.
* Include a module-level docstring that explains why the script _exists_.
  Scripts tend to rot in production because nobody is sure why they're there
  or if they're safe to remove. A docstring at the top helps reduce that
  uncertainty, especially if it's collected by a tool like
  [sphinx](http://sphinx-doc.org/).
* Always protect against import side effects. Someday, someone will import
  from your script in prod.
* Only import from your script in interactive shells (when you're doing a
  one-off) or in tests. Code that's needed in other scripts or in your
  application should live elsewhere.
* Don't check for coverage in the script conditional:

  ```python
  if __name__ == '__main__':  # pragma: no cover
  ```

  Because of that, don't put any logic in the conditional, just call functions.
  This makes it easy to write tests and get meaningful coverage reports.
* Your script should be understandable from its output on the _system_
  shell (e.g. bash), like a linux command.

  * No reading code.
  * No digging through the db.
  * No `pdb` tracing.

* Use the core `logging` library (not `print`). Scripts with uninformative
  output are painful to maintain, and informative output is easy with
  `logging`.

  * Log on successes, not just on failures!
  * Log at least to the console. Logging to files and db optional.
  * Use the logging levels. Check official docs of your version to figure out
    which level to use for your output.
  * Timestamp output, always!

* Use the core `argparse` library (not `optparse` or `sys.argv`). Bad
  argument handling can be destructive, and good argument handling is easy with
  `argparse`.

  * Watch out for dashes becoming underscores.
  * Include a help string for the script:

    ```python
    parser = argparse.ArgumentParser(description='help string')
    ```

  * Include a help string for every argument:

    ```python
    parser.add_argument('blah', help='help string')
    ```
