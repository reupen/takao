# Takao

Takao is a dark theme for the
[Sphinx documentation generator](https://www.sphinx-doc.org).

I created it mainly for my own projects. Feel free to try it and open an issue
if you have any problems.

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

Development of Takao requires Python 3.11, [Poetry](https://python-poetry.org)
and Node.js 18.

### Building a wheel

1. Install Python dependencies:

   ```shell
   poetry install
   ```

2. Install Node.js dependencies:

   ```shell
   npm install
   ```

3. Build static assets:

   ```shell
   npm run build
   ```

4. Build the wheel :
   ```shell
   poetry build
   ```
