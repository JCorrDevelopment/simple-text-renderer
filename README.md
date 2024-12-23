# Weavely

## Current status

Project is in the early stages of development, so code may see significant changes. Even though the project base 
functionality seems to be working, there are still many features are missing and proper testing is not yet implemented.
Be aware that the project is not yet read for production use.

## Description

Weavely Document Writer is a Python library designed for developers who need flexible and dynamic generation of plain 
text documents. Unlike existing solutions that often limit customization, Weavely empowers developers to create 
text-based reports, documents, or any arbitrary content with full control over formatting and rendering. 
Using a simple block-based approach, Weavely enables the creation of documents that are both well-structured and easy 
to customize, addressing the frustrations of dealing with rigid and complex libraries. Whether you're generating 
reports or formatting content for textual representation, Weavely offers a straightforward solution that adapts to your 
needs without endless configuration.

## Requirements:

- Python 3.13 or higher
- [rye](https://rye.astral.sh/) for managing most of the activities in the project.


## Documentation

You can find the documentation here: https://jcorrdevelopment.github.io/Weavely/weavely.html

Documentation is generated using `pdoc` tool and is hosted as a GitHub page.

Alternatively, you can find the documentation locally under `docs` directory. To sync the documentation state with the
latest changes, you can run the following command:

```shell
rye run docs
```

Alternatively, you can run documentation server locally by running the following command:

```shell
rye run docs:pdoc-server
```

## Installation

Ensure your project meets the minimal requirements. At the moment, project still in the early stages of development,
so it is not yet available on PyPi. To install the project, you can clone the repository and install it using `pip`
by referencing git repository:

```shell
pip install git+https://github.com/JCorrDevelopment/Weavely.git
```

## Contributing

Weavely is an open-source project, so any contributions are welcome. Provide your feedback, bug reports and feature
requests in the [Issues](https://github.com/JCorrDevelopment/Weavely/issues) section. If you want to contribute to the
project, you need to follow simple steps:

a. Follow the [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for your commits.
b. Ensure that your code is linted and formatted according to the project's standards. (Use `rye run pre-commit` to
   check your code before committing)

## Ideas for development

[ ] - Support for Weavely general template language for customizable document rendering
[ ] - Paragraph type combined by several composite parts
[ ] - Container block
[ ] - Chained formatter to combine several existing formatters into a single object