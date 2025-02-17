---
theme: default
marp: true
paginate: true
style: |
---

# RDFCraft: Hands-on Session

<!--
_paginate: skip
-->

### Ensar Emir EROL – Maastricht University

---

# Agenda

1. Tools to be used
2. Resources to be used
3. Dataset Introduction
4. Ontology Introduction
5. How to clean and prepare datasets for RDF mapping
6. What are URIs and how to create them
7. Planning for RDF mapping
8. 🚀 Cleaning and mapping example datasets 🚀

---

# Tools to Be Used

In this session, we will use the following tools:

1. [OpenRefine](https://openrefine.org/)
2. [RDFCraft](https://github.com/MaastrichtU-IDS/RDFCraft)

Both OpenRefine and RDFCraft depend on Java, so make sure you have Java
installed on your machine.

---

# Resources to Be Used

You can find all resources in the following repository: **TBD** _(Add your
repository link once available.)_

---

# Dataset Introduction

We have two example datasets related to healthcare, both in CSV format and
conceptually connected.

1. **Administrative Cases** – A simple dataset containing administrative cases
   in a hospital. This dataset has the following columns:

   ```csv
   row_id,patient_id,diagnosis_code,created_at,org_code,org_name
   ```

2. **Prescriptions** – A dataset containing hospital prescriptions. It has the
   following columns:

```csv
row_id,patient_id,medication_atc_code,diagnosis_code,creation_date,times_a_day,dosage
```

---

# Ontology Introduction

We will use really small part of
[Swiss Personalized Health Network (SPHN) Ontology](https://www.biomedit.ch/rdf/sphn-ontology/sphn/2023/2#)
for this session.

---

# How to clean and prepare datasets for RDF Mapping

<!--
The first challenge is that data from databases are not directly aligned with the ontology to be used.
Even if the data is in 4NF or 5NF, the values stored might not be standardized, which is crucial in RDF.
Therefore, we must clean and prepare the data for RDF mapping.
-->

**This is the most important part of the any mapping process.**

Even if you have the cleanest data in the world, it will **unlikely** to have
the structure that allows you to directly map it to **RDF**.

It depends on the **data** and the **ontology** you are using but in general,
you need to:

- **Standardize** the values
- **Normalize** the data according to the ontology

---

# Data Cleaning: Standardize the Values

- **Standardize** the values: Ensure that columns holding specific data (e.g.,
  dates, units) are consistent and follow a known standard.

For example, if you have a column of dates, make sure all dates follow ISO 8601
format (the default for RDF).

If you have a column for units (e.g., mg, ml), map them to a recognized system
to maintain consistency.

---

# Data Cleaning: Normalize the data

- **Normalize** the data according to the ontology: Ensure that your dataset’s
  structure aligns with the ontology.

For instance, if one column’s values need to be split into two different
entities in the ontology, separate them into two columns. Example:

10 mg should be split into:

`10 mg` -> `10` and `mg`

---

# What are URIs and how to create them

**URI** stands for **Uniform Resource Identifier**. It is a string of characters
that unambiguously identifies a particular resource.

In your mappings, you will need to create URI patterns to generate unique URIs
for entities in your dataset.

**Each entity in your dataset should have a unique URI.**

---

# How to create URI patterns

You can create URI patterns by referencing columns in your dataset. For example,
to create a URI for a prescription, you can use the row_id column:

```uri
http://example.org/prescription/$(row_id)
```

You can also use the same column in different URI patterns. For example, to
represent the dosage of a prescription, you might use:

```uri
http://example.org/prescription/$(row_id)/dosage
```

---

# Planning for RDF Mapping

Before starting the RDF mapping, another important step is to plan which classes
and properties from the ontology you will use.

**This is important to not get lost while mapping the data.**

We will use the following two main concepts from the SPHN Ontology:

- `sphn:AdministrativeCase`
- `sphn:DrugPrescription`

---

# 🚀 Cleaning and Mapping example datasets 🚀

Finally, we will demonstrate how to clean and map both datasets to RDF using
OpenRefine and RDFCraft.

Feel free to follow along!
