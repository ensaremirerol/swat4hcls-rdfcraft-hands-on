# RDFCraft Tutorial for SWAT4HCLS 2025

This repo contains hands-on materials and instructions for the RDFCraft tutorial
at SWAT4HCLS 2025.

## Tutorial Overview

The hands-on session, we will walk you through the process of cleaning,
transforming the data and mapping it to RDF. We will use
[OpenRefine](https://openrefine.org/) for data cleaning and
[RDFCraft](https://github.com/MaastrichtU-IDS/RDFCraft) for mapping the data to
RDF.

## Prerequisites

- Java 8 or higher (for both OpenRefine and RDFCraft)

> [!NOTE]
>
> RDFCraft can be run without Java, but it won't be able to generate RDF files.
> You can still generate YARRRML and RML files and use them with other tools

## Software Installation

### OpenRefine

Please follow the instructions on the
[OpenRefine website](https://openrefine.org/download.html)

### RDFCraft

You can download the latest version of RDFCraft from the
[releases](https://github.com/MaastrichtU-IDS/RDFCraft/releases) page.

- For Windows, you can download the `.exe` file and run it.
- For macOS, you can download the `.dmg` file, open it and drag the app to the
  Applications folder. Then you can run the app from the Applications folder.

> [!IMPORTANT] On macOS, because app is not notarized by Apple, you need to run
> following command to bypass the gatekeeper:
>
> ```bash
> xattr -rd com.apple.quarantine </path/to/RDFCraft.app>
> ```
>
> More information about gatekeeper can be found
> [here](https://support.apple.com/en-us/HT202491).

## Folders in this Repository

- [raw_data](/raw_data) - Contains the raw data files that will be used in the
  tutorial.

- [cleaned_data](/cleaned_data) - Contains the cleaned data files that will be

- [openrefine_actions](/openrefine_actions) - Contains the OpenRefine actions
  that will be used in the tutorial. You can use these actions to quickly apply
  the transformations we will be doing in the tutorial.

- [rdf_craft_mappings](/rdf_craft_mappings) - Contains the RDFCraft mappings
  that will be used in the tutorial. You can use these mappings to quickly
  replicate the RDF mappings we will be doing in the tutorial.

- [rdf](/rdf) - Contains the RDF files that will be generated in the tutorial.s

## Data Files

We have two example datasets for this tutorial, both in CSV format and related
to Health Care:

- [Administrative Cases](/raw_data/administrative_cases.csv) - A dataset
  containing administrative cases in a hospital.

- [Prescriptions](/raw_data/prescriptions.csv) - A dataset containing
  prescriptions made by doctors.

## Outline of the Tutorial

- Initial planning and understanding of the data

- Data Cleaning with OpenRefine using the
  [Administrative Cases dataset](/raw_data/administrative_cases.csv)

- Mapping the cleaned data to RDF using RDFCraft

- Data Cleaning with OpenRefine using the
  [Prescriptions dataset](/raw_data/prescriptions.csv)

- Mapping the cleaned data to RDF using RDFCraft

- Allowing participants to practice cleaning and mapping the provided datasets
  or other datasets of their choice independently.
