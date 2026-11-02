# translation_checker

> **Pre-release:** An experimental Python source inspection tool. The API,
> output format, and detection behavior may change before a stable release.

`translation_checker` finds direct `translate(...)` calls in Python source
code and prints their line numbers. It parses the source into an abstract
syntax tree (AST) without executing the inspected code.

The current implementation detects calls only. It does not validate
translations or check whether translation keys exist.

## Requirements

- The examples below were verified with **Python 3.15**. A minimum supported
  version and compatibility with other Python versions have not yet been
  established.
- Only the Python standard library is used; no third-party dependencies are
  required.

## Quick Start

Clone the repository and open its directory:

```shell
git clone https://github.com/Nagisns/translation_checker.git
cd translation_checker
```

Start Python from this directory, then run:

```python
from checker import check_translations

source = 'message = translate("welcome")\nprint(message)\n'
check_translations(source)
```

Output:

```text
Line 1: translate detected.
```

The `translate` function does not need to be defined for inspection, because
the supplied source is parsed rather than executed. Calls appearing only
inside comments or string literals are not reported.

To inspect a UTF-8 Python file, replace `example.py` with the path to your
file and run the following from the repository directory:

```python
from pathlib import Path
from checker import check_translations

source = Path("example.py").read_text(encoding="utf-8")
check_translations(source)
```

There is currently no command-line interface or installable package
configuration. Running `python checker.py` alone does not scan any files.

## Function Behavior

`check_translations(source: Optional[str]) -> None`

| Input | Behavior |
|---|---|
| Valid Python source containing a direct `translate(...)` call | Prints `Line N: translate detected.` for each matching call. Line numbers start at 1. |
| Valid source with no matching calls, including an empty string | Produces no detection output. |
| `None` | Logs the warning `Source code is not set.` and returns. |
| Invalid Python syntax | Raises `SyntaxError`; the function does not catch it. |

Results are printed to standard output; the function returns `None` on
normal completion. Output is not explicitly sorted by line number.

## Current Limitations

- Detection matches the literal function name `translate`. Attribute calls
  such as `i18n.translate(...)` and aliases such as `tr(...)` are not matched.
- Names are not resolved against imports or scopes. An unrelated function
  named `translate` is also reported.
- Translation quality, key existence, argument validity, and untranslated
  strings are not checked.
- File discovery, directory scanning, structured results, and automated
  fixes are not implemented.

## Feedback

For bugs or feature requests, open an
[issue](https://github.com/Nagisns/translation_checker/issues). Include your
Python version, a minimal source example, and the expected and actual output.

## License

[MIT License](LICENSE).
