# C/C++ Project Template

## Overview
A template repository for C/C++ projects with CMake and Conan. A GitHub Action 
workflow is provided with the on `workflow_dispatch` event. This event has three input
parameters which are `project_lang`, `project_type`, and `project_namespace`.
`project_lang` is the language the project will be generated in. As the name of this
template repo might suggest, the only available options are C and C++. For
`project_type`, one can choose from Executable, Static Library, Shared Library, or
Interface Library. The last  parameter, `project_namespace`, is optional and defaults 
to the name of the GitHub repository name. 

## Template Parameters: `project_type`
`project_type` determines how the project will be generated. The supported types are
Executable, and Library.

### Project Types: Executable
#### Rust Executable Project File Tree
```text
.
├── src/
│   └── main.rs
├── tests/
│   ├── 
│   └── 
├── .clippy.toml
├── .gitignore
├── build.rs
├── Cargo.toml
├── Cargo.lock
├── LICENSE
└── README.md
```


### Project Types: Library
#### Rust Project File Tree
```text
.
├── src/
│   └── lib.rs
├── tests/
│   ├── 
│   └── 
├── .clippy.toml
├── .gitignore
├── build.rs
├── Cargo.toml
├── Cargo.lock
├── LICENSE
└── README.md
```
