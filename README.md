# Takao

Takao is a dark theme for the
[Sphinx documentation generator](https://www.sphinx-doc.org).

I created it mainly for my own projects. Feel free to try it and open an issue
if you have any problems.

## Demo

For a demo of the theme, see https://columns-ui-sdk.readthedocs.io.

## Licence

Takao uses the MIT licence.

Distributions of Takao include the [Inter font](https://github.com/rsms/inter),
which
[uses the SIL Open Font Licence](https://github.com/rsms/inter/blob/master/LICENSE.txt).

## Installation

1. Install the Python package:

   ```shell
   pip install takao
   ```

2. Update `html_theme` in your Sphinx project configuration:

   ```python
   html_theme = "takao"
   ```

3. Create a clean documentation build in your Sphinx project directory:

   ```shell
   make clean
   make html
   ```

## Development

Development of Takao requires Python 3.11, [uv](https://docs.astral.sh/uv/) and
Node.js 18.

### Set up

1. Install Python dependencies:

   ```shell
   uv sync
   ```

2. Install Node.js dependencies:

   ```shell
   npm install
   ```

### Build a wheel

```shell
uv run scripts/build.py
```

### Build the docs

```shell
uv run scripts/build_docs.py
```

### Run visual regression tests

Requires [Podman](https://podman.io/getting-started/installation).

```shell
uv run scripts/run_e2e_tests.py
```

#### Update changed snapshots

```shell
uv run scripts/run_e2e_tests_update_snapshots.py
```
