# SAS Customer Intelligence 360

## SAS 360 API WORKFLOW LIBRARY

> **Status: superseded.** This library has been replaced by [`sas-ci360-sol-workflow`](https://github.com/mnelson3/sas-ci360-sol-workflow) — the same Workflow API, rebuilt with mockable unit tests, typed exceptions, and safer configuration defaults. This repo is kept for historical reference; start new work in `sas-ci360-sol-workflow` instead. This repo's final implementation is frozen at the `archive/superseded` branch.

### Overview

The Workflow API enables you to access and manage workflow resources such as workflow processes, workflow tasks, approvals, assignments, and attachments in SAS Customer Intelligence 360. Workflows enable an organization to automate processes and save time. Automated workflows are used to manage assignments and provide real-time visibility into project timelines. Workflows contain workflow tasks, which are assigned to contributors (users or groups) who complete the tasks.

For detailed information on REST API:<br>
https://support.sas.com/documentation/onlinedoc/ci/ci360-apis/marketingWorkflow/v1/redoc.html
<br><br>

### Table of Contents

This topic contains the following sections:

 - <a href="#prerequisites">Prerequisites</a>
 - <a href="#installation">Installation</a>
 - <a href="#getting-started">Getting Started</a>
 - <a href="#api-workflow-code">API Workflow Code</a>
 - <a href="#troubleshooting">Troubleshooting</a>
 - <a href="#contributing">Contributing</a>
 - <a href="#license">License</a>
 - <a href="#additional-resources">Additional Resources</a>
<br><br>

### Prerequisites

 * Required Python: >=3.6
 * Customer Intelligence 360 Tenant with Administrative Rights
 * SAS CI360 API Core Library:<br>
   https://github.com/mnelson3/sas_ci360_api_core
<br><br>

### Installation

To install the SAS CI360 API Workflow Library from a clone of this repository:
 1. `git clone https://github.com/mnelson3/sas_ci360_api_workflow.git`
 1. `cd sas_ci360_api_workflow`
 1. `pip install .`
<br><br>

### Getting Started

While this library is available for review, please note that it is considered a work in process and NOT considered "released for production".
<br><br>

### API Workflow Code

 1. Assignments - Contains operations for the workflow assignments.
 1. Attachments - Contains operations for the workflow attachments.
 1. Definitions - Returns a collection of workflow definitions based on the options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.workflow.definition.summary media type.
 1. Processes - Contains operations for the workflow processes.
 1. Root - Contains operations for this root resource.
 1. Tasks - Contains operations for the workflow tasks.
<br><br>

### Troubleshooting

For issues specific to sasci360apicore or sasci360apiworkflow try updating the libraries.

To update sasci360apicore:
 1. Pull the latest changes from a clone of the [SAS CI360 API Core Library](https://github.com/mnelson3/sas_ci360_api_core)
 1. Open a terminal window (Unix/macOS) or command prompt (Windows) in that clone
 1. Copy and paste the following line at the cursor<br>
    pip install --upgrade .
 1. Press "Enter"

To update sasci360apiworkflow:
 1. Pull the latest changes from a clone of this repository
 1. Open a terminal window (Unix/macOS) or command prompt (Windows) in that clone
 1. Copy and paste the following line at the cursor<br>
    pip install --upgrade .
 1. Press "Enter"
<br><br>

### Contributing

We welcome your contributions! Please read [CONTRIBUTING](CONTRIBUTING.md) for details on how to submit contributions to this project.
<br><br>

### License

This project is licensed under the [Nelson Grey LLC Community License 1.0](LICENSE).

- **Free for individuals, education, and research**: use, modify, and distribute this software for non-commercial purposes
- **Commercial evaluation**: evaluate the software for a possible commercial use, free of charge
- **Commercial production use**: requires a commercial license from Nelson Grey LLC
- **Automatic conversion**: on December 13, 2029, this automatically converts to the Apache License 2.0

For commercial licensing inquiries, contact support@nelsongrey.com.

### Additional Resources

For more information, see [REST APIs](https://go.documentation.sas.com/doc/en/cintcdc/production.a/cintapis/ch-rest-apis.htm).
<br><br>
