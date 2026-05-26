# AI App Compiler



## Overview

AI App Compiler is a software generation system that transforms natural language application requirements into validated and executable application specifications.

The project approaches software generation as a compiler problem instead of a simple prompt engineering task. Rather than generating everything through a single response, the system processes user requirements through multiple controlled stages. Each stage performs a specific responsibility before passing information to the next stage.

A user can enter a requirement such as:

Build a CRM with login, contacts, leads, analytics and role based access

The system analyzes the request and generates a structured application configuration containing user interface definitions, API endpoints, database schemas, authentication rules, validation reports and runtime execution results.

The project was developed to demonstrate reliability, execution awareness, validation, repair mechanisms and system level engineering principles.

---
## Internship Project Context

This project was developed as part of an AI Engineer Internship technical assessment focused on system design, reliability, validation and execution awareness.

The objective of the assignment was to design and implement a compiler inspired software generation system capable of transforming natural language requirements into structured and executable application specifications.

Unlike traditional prompt based generation systems, the assignment required a modular architecture consisting of multiple stages including intent extraction, architecture planning, schema generation, validation, repair and runtime verification.

The project was designed to demonstrate practical AI engineering skills including:

System architecture design

Structured generation pipelines

Validation and consistency checking

Automatic error detection and repair

Runtime execution and verification

Evaluation framework development

Performance and reliability measurement

The implementation emphasizes engineering discipline, predictable outputs and execution awareness rather than relying solely on direct language model responses.

This repository represents the complete solution submitted for the AI Engineer Internship assignment.
---

## Project Objective

The objective of this project is to convert natural language requirements into structured software specifications through a compiler inspired workflow.

The system focuses on:

Reliable generation

Predictable outputs

Validation before execution

Automatic recovery from errors

Runtime verification

Performance evaluation

Every generated component is validated and verified before execution.

---

## Architecture Overview

```text
User Requirement
        │
        ▼
Intent Extraction
        │
        ▼
Architecture Generation
        │
        ▼
UI Generation
        │
        ▼
API Generation
        │
        ▼
Database Generation
        │
        ▼
Authentication Generation
        │
        ▼
Validation Engine
        │
        ▼
Consistency Verification
        │
        ▼
Repair Engine
        │
        ▼
Runtime Execution
        │
        ▼
Application Summary
        │
        ▼
Final JSON Output
```

---

## Detailed System Architecture

```text
┌───────────────────────────────────────────┐
│           USER REQUIREMENT INPUT          │
│                                           │
│ Build a CRM with login and analytics      │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│            INTENT EXTRACTION              │
│                                           │
│ Identify application category             │
│ Detect requested features                 │
│ Extract entities and modules              │
│ Preserve original requirement             │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│         ARCHITECTURE GENERATION           │
│                                           │
│ Select frontend technology                │
│ Select backend technology                 │
│ Select database technology                │
│ Create application structure              │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│              UI GENERATION                │
│                                           │
│ Create pages                              │
│ Create dashboards                         │
│ Create forms                              │
│ Create visual components                  │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│              API GENERATION               │
│                                           │
│ Generate endpoints                        │
│ Generate request methods                  │
│ Generate route definitions                │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│           DATABASE GENERATION             │
│                                           │
│ Create tables                             │
│ Create columns                            │
│ Create entity structures                  │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│        AUTHENTICATION GENERATION          │
│                                           │
│ Create user roles                         │
│ Create permission rules                   │
│ Create access control model               │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│            VALIDATION ENGINE              │
│                                           │
│ Verify required sections                  │
│ Verify schema completeness                │
│ Verify structural integrity               │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│         CONSISTENCY VALIDATION            │
│                                           │
│ Verify UI to API mapping                  │
│ Verify API to Database mapping            │
│ Verify Login to Auth mapping              │
│ Verify dependency relationships           │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│              REPAIR ENGINE                │
│                                           │
│ Detect missing components                 │
│ Repair incomplete schemas                 │
│ Restore missing endpoints                 │
│ Restore missing tables                    │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│            SQLITE EXECUTION               │
│                                           │
│ Generate SQL statements                   │
│ Execute schema creation                   │
│ Verify successful execution               │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│               FINAL OUTPUT                │
│                                           │
│ Human readable summary                    │
│ Structured JSON configuration             │
│ Validation results                        │
│ Runtime execution report                  │
└───────────────────────────────────────────┘
```

---

## Core Components

### Intent Extraction

This stage analyzes the user requirement and identifies the type of application being requested.

Supported categories include CRM systems, ecommerce platforms, hospital management systems and general business applications.

The extracted information becomes the foundation for all subsequent stages.

### Architecture Generation

The architecture generator creates the overall system structure.

The current implementation generates:

React frontend

FastAPI backend

SQLite database

This stage acts as the blueprint for the remainder of the pipeline.

### UI Generation

The UI generator creates application pages and interface elements based on the detected application type.

Examples include dashboards, login screens, contact management pages, appointment modules and analytics views.

### API Generation

The API generator creates endpoint definitions required by the application.

Generated endpoints are aligned with the entities discovered during intent extraction.

### Database Generation

The database generator creates tables and column structures for each application category.

Generated tables are later executed inside the runtime environment for verification.

### Authentication Generation

Authentication generation creates user roles and permission structures required for access control.

Roles are linked to generated pages and application modules.

### Validation Engine

The validation engine verifies that every required section exists before execution begins.

It checks completeness, structure and configuration integrity.

### Consistency Validation

Consistency validation verifies relationships between generated layers.

Examples include:

Pages requiring matching APIs

APIs requiring matching database tables

Login functionality requiring authentication rules

Dependencies requiring valid references

### Repair Engine

The repair engine automatically fixes incomplete or inconsistent configurations.

Instead of regenerating the entire application specification, only missing sections are repaired.

This improves reliability and reduces unnecessary regeneration.

### Runtime Execution

The final configuration is executed against an SQLite runtime environment.

Generated tables are created and verified to ensure the produced specification is executable.

---

## Evaluation Framework

The project includes a benchmark dataset containing multiple categories of prompts.

The evaluation framework measures:

Generation success rate

Runtime execution success

Average latency

Ambiguous prompt detection

Contradiction detection

Repair effectiveness

System stability

The benchmark dataset contains business applications, healthcare systems, ecommerce platforms, educational solutions, logistics systems and intentionally difficult prompts designed to test reliability.

---

## Frontend

The frontend is developed using React and Vite.

Users can:

Enter application requirements

Generate configurations

View application summaries

Inspect structured JSON output

Review validation results

Check runtime execution status

Switch between summary and JSON modes

---

## Backend

The backend is implemented using FastAPI.

Responsibilities include:

Pipeline orchestration

Stage execution

Validation

Repair operations

Runtime verification

Metrics collection

Response generation

---

## Technology Stack

Frontend

React

Vite

Axios

Backend

FastAPI

Python

Runtime

SQLite

Evaluation

Custom benchmark framework

Metrics engine

Version Control

Git

GitHub

---

## Future Enhancements

Future versions of the project may include:

Dynamic frontend generation

Advanced relationship modeling

Visual workflow generation

Role aware interface generation

Automatic API documentation

Application export functionality

Cloud execution environments

Multiple database engines

Advanced validation strategies

---
## Quick Navigation

Frontend Documentation

[Open Frontend Guide](./frontend/README.md)

Backend Documentation

[Open Backend Guide](./backend/README.md)

---

## Conclusion

AI App Compiler demonstrates how software generation can be approached through structured engineering principles rather than direct text generation.

By combining staged generation, validation, consistency verification, automatic repair and runtime execution, the system produces reliable and executable application specifications while maintaining transparency throughout the generation process.

The project emphasizes control, predictability and verification, making it closer to a compiler workflow than a traditional prompt driven application generator.


# Deployment

## Production Environment

### Frontend

The React frontend is deployed on Railway and provides the user interface for entering application requirements and viewing compiler outputs.

URL

https://ai-app-compiler-production.up.railway.app

### Backend API

The FastAPI backend hosts the compiler pipeline, validation engine, repair system and runtime execution layer.

URL

https://ai-app-compiler-api-production.up.railway.app

### Interactive API Documentation

Swagger documentation is automatically generated by FastAPI.

URL

https://ai-app-compiler-api-production.up.railway.app/docs

### Source Code Repository

GitHub

https://github.com/adithyabvds/AI-App-Compiler
