# AI App Compiler Backend

## Overview

The backend serves as the core engine of the AI App Compiler system. It is responsible for transforming natural language application requirements into structured, validated and executable application specifications through a compiler inspired pipeline.

Built using FastAPI and Python, the backend orchestrates every stage of the generation process including intent analysis, architecture planning, UI generation, API generation, database schema creation, authentication generation, validation, repair and runtime execution.

This backend was developed as part of an AI Engineer Internship project focused on system design, reliability, execution awareness and controlled software generation.

---

## Project Objective

The objective of the backend is to convert user requirements into complete software specifications through a deterministic multi stage workflow.

The system emphasizes:

Reliability

Structured outputs

Validation before execution

Automatic recovery from inconsistencies

Execution verification

Performance evaluation

Instead of generating application specifications through a single request, every stage performs a dedicated responsibility before passing information to the next stage.

---

## Backend Architecture

```text
User Prompt
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
Schema Validation
     │
     ▼
Consistency Validation
     │
     ▼
Repair Engine
     │
     ▼
SQLite Runtime Execution
     │
     ▼
Summary Generation
     │
     ▼
Final Response
```

---

## Detailed Pipeline Architecture

```text
┌───────────────────────────────────────────┐
│              USER REQUEST                 │
│                                           │
│ Build a CRM with login and analytics      │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│            INTENT EXTRACTION              │
│                                           │
│ Detect application category               │
│ Detect entities                           │
│ Detect requested features                 │
│ Preserve original requirement             │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│         ARCHITECTURE GENERATION           │
│                                           │
│ Select frontend stack                     │
│ Select backend stack                      │
│ Select database stack                     │
│ Create architecture blueprint             │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│              UI GENERATION                │
│                                           │
│ Generate pages                            │
│ Generate components                       │
│ Generate dashboards                       │
│ Generate forms                            │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│              API GENERATION               │
│                                           │
│ Generate endpoints                        │
│ Generate routes                           │
│ Generate request methods                  │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│           DATABASE GENERATION             │
│                                           │
│ Generate tables                           │
│ Generate columns                          │
│ Generate schema structure                 │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│        AUTHENTICATION GENERATION          │
│                                           │
│ Generate roles                            │
│ Generate permissions                      │
│ Generate access rules                     │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│            SCHEMA VALIDATION              │
│                                           │
│ Verify required sections                  │
│ Verify completeness                       │
│ Verify structural integrity               │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│         CONSISTENCY VALIDATION            │
│                                           │
│ Verify UI and API mapping                 │
│ Verify API and Database mapping           │
│ Verify Login and Auth mapping             │
│ Verify dependency relationships           │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│              REPAIR ENGINE                │
│                                           │
│ Detect missing components                 │
│ Repair invalid structures                 │
│ Restore missing endpoints                 │
│ Restore missing tables                    │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│            SQLITE EXECUTION               │
│                                           │
│ Generate SQL                              │
│ Execute schema                            │
│ Verify successful creation                │
│ Collect execution results                 │
└───────────────────────────────────────────┘
                     │
                     ▼

┌───────────────────────────────────────────┐
│             FINAL RESPONSE                │
│                                           │
│ Human readable summary                    │
│ Structured JSON output                    │
│ Validation results                        │
│ Runtime execution report                  │
└───────────────────────────────────────────┘
```

---

## Project Structure

```text
backend

stages
│
├── intent.py
├── architecture.py
├── ui_generator.py
├── api_generator.py
├── db_generator.py
├── auth_generator.py
├── summary_generator.py
└── text_summary.py

validators
│
├── schema_validator.py
└── consistency_validator.py

repair
│
└── repair_engine.py

runtime
│
└── simulator.py

evaluation
│
├── dataset.json
└── metrics.py

compiler.py

main.py
```

---

## Core Components

### Intent Extraction

The intent extraction stage analyzes user requirements and identifies:

Application category

Requested features

Core entities

Functional modules

Original requirement context

Supported application categories include:

CRM

Hospital Management

Ecommerce

Food Delivery

General Business Applications

---

### Architecture Generation

This stage creates the overall application architecture.

Current architecture selection includes:

React frontend

FastAPI backend

SQLite database

The generated architecture acts as the blueprint for all subsequent stages.

---

### UI Generation

The UI generator creates application pages and interface elements according to the identified application type.

Examples include:

Login pages

Dashboards

Analytics screens

Contact management views

Appointment management screens

Product catalog interfaces

---

### API Generation

The API generator creates endpoint definitions required by the generated application.

Examples include:

POST login

GET contacts

POST contacts

GET products

POST orders

The generated endpoints remain aligned with application entities and business functionality.

---

### Database Generation

The database generator creates database structures required by the generated application.

Generated elements include:

Tables

Columns

Entity structures

Relationships

Generated schemas are later verified through runtime execution.

---

### Authentication Generation

Authentication generation creates:

Roles

Permissions

Access control definitions

Authorization structures

Roles are mapped to application functionality and generated interfaces.

---

### Summary Generation

The summary generator creates a concise overview of the generated application.

The generated report contains:

Application type

Features

Pages

API endpoints

Database tables

Architecture information

Runtime status

Validation status

---

## Validation System

The validation layer ensures generated specifications remain reliable and complete.

### Schema Validation

Verifies:

Intent exists

Architecture exists

UI exists

API exists

Database exists

Authentication exists

Completeness of generated configuration

Structural correctness

---

### Consistency Validation

Verifies:

Pages reference valid APIs

APIs reference valid database structures

Authentication exists when login functionality is present

Dependencies remain consistent across all layers

Cross layer relationships remain valid

---

## Ambiguity Handling

The backend detects vague requirements before generation begins.

Examples include:

Build something

Create an app

Make software

Such requests trigger clarification responses rather than generating unreliable outputs.

---

## Contradiction Detection

The backend detects logically impossible requirements.

Examples include:

Payment system without customers

CRM without users

Hospital management system without patients

Conflicting specifications are rejected before execution.

---

## Repair Engine

The repair engine automatically fixes incomplete configurations.

Capabilities include:

Restoring missing tables

Restoring missing endpoints

Restoring missing entities

Repairing invalid relationships

Updating incomplete specifications

The system repairs only the affected sections rather than regenerating the entire application.

---

## Runtime Execution

Runtime execution verifies generated specifications through SQLite execution.

Execution flow:

Generate schema

Create SQLite database

Create tables

Execute SQL

Verify creation

Collect results

Execution confirms that generated configurations are structurally valid and executable.

---

## Evaluation Framework

The backend includes a benchmark framework for measuring system reliability.

Metrics include:

Total test count

Successful generations

Success rate

Average latency

Ambiguous prompt detection

Contradiction detection

Repair frequency

Execution success rate

The benchmark dataset contains standard, ambiguous, contradictory and multi domain application requests.

---

## API Endpoint

### Compile Application

Request:

```http
POST /compile
```

Example Request:

```json
{
  "prompt": "Build a CRM with login, contacts and analytics"
}
```

Response:

```json
{
  "intent": {},
  "architecture": {},
  "ui": {},
  "api": {},
  "database": {},
  "auth": {},
  "validation": {},
  "runtime": {}
}
```

---

## Technology Stack

Backend Framework

FastAPI

Programming Language

Python

Runtime Engine

SQLite

Validation System

Custom Validation Framework

Evaluation System

Benchmark Dataset

Metrics Engine

Version Control

Git

GitHub

---

## Future Enhancements

Potential future improvements include:

Dynamic code generation

Advanced schema relationships

Multi database support

Cloud runtime execution

Role aware UI generation

Automatic API documentation

Visual workflow generation

Advanced validation strategies

Application export functionality

Container based deployment

---

## Internship Project Context

This backend was developed as part of an AI Engineer Internship technical assessment.

The project was designed to demonstrate practical AI engineering concepts including structured generation pipelines, validation systems, automatic repair mechanisms, execution awareness and reliability focused software generation.

The implementation prioritizes engineering discipline, predictability and verifiable outputs rather than direct single step generation.

---

## Conclusion

The AI App Compiler Backend demonstrates a compiler inspired approach to software generation through staged processing, validation, repair and runtime verification.

By combining intent extraction, architecture planning, schema generation, consistency validation, automatic repair and SQLite execution, the backend produces reliable and executable application specifications while maintaining transparency throughout the generation process.