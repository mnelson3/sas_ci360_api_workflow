# Security Policy

## Supported Versions

This repository holds a retained historical/archived reference implementation of a Python client for the SAS Customer Intelligence 360 Workflow API (workflow processes, tasks, approvals, assignments, and attachments). It has been superseded by `sas-ci360-sol-workflow` and is no longer actively developed. Only the code currently deployed on each environment branch is supported — there is no long-term support for older commits.

| Branch | Environment | Status |
|---|---|---|
| `main` | Production | Supported |
| `staging` | Staging | Supported |
| `develop` | Development | Supported |

## Reporting a Vulnerability

This repository doesn't have a public issue tracker, so please don't report security concerns that way. Use one of:

- GitHub's [private vulnerability reporting](https://github.com/mnelson3/sas_ci360_api_workflow-archived/security/advisories/new) (enabled on this repo), or
- Email **support@nelsongrey.com**

Either way, include:

- A description of the vulnerability and its potential impact
- Steps to reproduce, or a proof of concept if available
- Any relevant logs, request/response samples, or affected endpoints

You should get an acknowledgement within a few business days.

## Automated Dependency Scanning

Dependabot alerts and security updates, native GitHub secret scanning (with push protection), and code scanning (CodeQL) are all enabled on this repository. Avoid committing credentials or secrets regardless — credentials are supplied by the consuming application via environment variables / a secrets manager, never committed to source.
