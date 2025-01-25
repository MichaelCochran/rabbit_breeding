# Design Document

## 1. Considerations

#### 1.1 Assumptions
No specific assumptions were provided.

#### 1.2 Constraints
No specific constraints were provided.

#### 1.3 System Environment
The software will initially be released for PC and Mac users. The latest version of Python is recommended to ensure proper functionality. There is no need for internet or network connectivity at this time. Plans to expand to mobile devices in the future have been mentioned.

## 2. Architecture

#### 2.1 Overview
The software architecture comprises several key components, including the User Interface, Application Logic, Data Access Layer, and Database. The User Interface facilitates user interaction, while the Application Logic handles core functionalities such as data processing and business logic. The Data Access Layer acts as an intermediary between the Application Logic and the Database, facilitating data exchange.

#### 2.2 Component Diagrams
Component diagrams were provided illustrating the key components of the software architecture, including the User Interface, Application Logic, Data Access Layer, and Database.

### Component Diagram: Application Logic

| AnimalBreedingSystem                                      |
|___________________________________________________________|
| + run(): void                                             |
| + startBreedingProcess(): void                            |
| + validateInput(input: string): boolean                   |
| + processBreedingRecord(record: BreedingRecord): void     |
|___________________________________________________________|

| BreedingRecord                                            |
|___________________________________________________________|
| - parent1: Animal                                         |
| - parent2: Animal                                         |
| - matingDate: Date                                        |
| - offspring: List                                         |
|___________________________________________________________|

### Component Diagram: Data Access Layer

| BreedingRecordRepository                                  |
|___________________________________________________________|
| + save(record: BreedingRecord): void                      |
| + findById(id: string): BreedingRecord                    |
| + findAll(): List                                         |
|___________________________________________________________|

#### 2.3 Class Diagrams
Class diagrams were provided for the Application Logic and Data Access Layer components, illustrating the structure and relationships of classes within each component.

#### 2.4 Sequence Diagrams
A sequence diagram was provided for the "Recording a Breeding Event" use case, depicting the interactions between the User Interface, Application Logic, and Data Access Layer components.

#### 2.5 Deployment Diagrams
A deployment diagram was provided illustrating the deployment architecture of the system, including PC/Mac users and the SQLite3 database.

## 3 User Interface Design
No user interface mock-ups or templates were included at this time.

## 4 Appendices and References

#### 4.1 Definitions and Abbreviations
- **GUI**: Graphical User Interface
- **CLI**: Command-Line Interface
- **DAL**: Data Access Layer
- **DBMS**: Database Management System

#### 4.2 References
No specific references were utilized in the creation of this design document.
