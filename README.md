# ascii-avatar

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)

[ascii-avatar](https://github.com/m2e-sh/ascii-avatar) is an open-source Python library that generates animated ASCII art avatars. The avatars dynamically adjust their facial expressions based on input phrases, making them ideal for CLI-based chatbots, text-based games, and fun command-line interactions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

## Features

- Generates ASCII avatars that animate facial expressions based on input text
- Uses Python with `poetry` for dependency management
- Supports customizable avatars and expressions
- Lightweight and efficient, perfect for CLI applications
- Open-source under the MIT license

## Installation

Ensure you have Python 3.11 or later installed, then install `ascii-avatar` using `poetry`:

```sh
pip install poetry  # If you haven't installed Poetry yet
poetry install
```

Alternatively, to install directly from GitHub:

```sh
poetry add git+https://github.com/m2e-sh/ascii-avatar.git
```

## Getting Started

You can generate an animated ASCII avatar in just a few lines of code:

```python
from ascii_avatar import Avatar

avatar = Avatar("😀")  # Choose an initial facial expression
avatar.animate("Hello, world!")  # The avatar adapts expressions to the phrase
```

Run your script, and you should see an animated ASCII face responding to the text input!

## Usage

The `Avatar` class provides methods to:

- Create an ASCII avatar with a specific facial expression
- Animate the avatar based on text input
- Customize the character set and style

Example:

```python
avatar = Avatar("😎")
avatar.animate("I'm feeling great today!")
```

## Testing

To run tests:

```sh
poetry run pytest
```

This ensures all components of `ascii-avatar` function as expected.

## Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, or discuss improvements.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## Changelog

Please refer to [CHANGELOG](./CHANGELOG.md).

## License

Copyright 2024 (c) [m2e.sh](https://github.com/m2e-sh)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



