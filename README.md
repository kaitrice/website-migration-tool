# Website Migration Tool

[![GitHub Issues](https://img.shields.io/github/issues/kaitrice/website-migration-tool)](https://github.com/kaitrice/website-migration-tool/issues) 
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kaitrice/website-migration-tool.svg)](https://github.com/kaitrice/website-migration-tool/pulls)
[![Pylint Status](https://img.shields.io/github/actions/workflow/status/kaitrice/website-migration-tool/pylint.yml?label=Pylint)](https://github.com/kaitrice/website-migration-tool/actions/workflows/pylint.yml)
[![Pytest Status](https://img.shields.io/github/actions/workflow/status/kaitrice/website-migration-tool/pytest.yml?label=Unit%20Test)](https://github.com/kaitrice/website-migration-tool/actions/workflows/pytest.yml)
[![License](https://img.shields.io/badge/license-MIT-white.svg)](/LICENSE)

Help migrate content from any website.

## Dependencies

- [Validators](https://github.com/python-validators/validators)

## Run Locally

Clone the project

```bash
  git clone https://github.com/kaitrice/website-migration-tool
```

Go to the project directory

```bash
  cd website-migration-tool
```

Install dependencies

```bash
  py -m pip install -r requirements.txt
```

Run command line tool

```bash
  make dev
```


## Running Tests

To run tests, run the following command

```bash
  make test
```

## Deployment

To deploy this project run

```bash
  make deploy MSG=""
```

## Roadmap

1. **Site Access**
    - URL Input
    - Authentication Handling
    - Sitemap Detection

1. **Content Extraction**
    - Pages / Posts
    - Products / Categories
    - Media Assets (images, videos, files)
    - Metadata (titles, descriptions, links)
    - Custom Selectors / Rules

1. **Content Transformation & Structuring**
    - Normalize Data (JSON, CSV, Markdown)
    - Map Fields to New Site Schema
    - Merge / Deduplicate Content
    - Tag & Categorize

1. **Review & Analysis**
    - Visual Content Audit
    - Sitemap Generation

1. **Export & Migration Prep**
    - JSON Exports
    - Media Downloads
    - Version Snapshots

1. **Multi-Site & Reuse Capabilities**
    - Compare Old vs New Site
    - Process Multiple Websites

## Used By

This project is used by the following companies:

- Coming soon...
