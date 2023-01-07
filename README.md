# Jarvis - A System Information CLI

A command line interface (CLI) to display information about your system's configuration, such as:

- What is the OS configuration?
- How much RAM does the system have?
- What are the system's CPU specs?
- How much free space is available on the system's disk?
- What processes are currently running on the system?
- What network ports are in use?

## Installation

To install the 'Jarvis' package and make the CLI command available to use, run the following command in the terminal:

```bash
pip install .
```

## Usage
To use the 'Jarvis' CLI, run the jarvis command followed by a subcommand:

```bash
jarvis <subcommand>
```

where <subcommand> is one of the following:


- os: Display information about the operating system.
- ram: Display information about the system's RAM.
- cpu: Display information about the system's CPU.
- disk: Display information about the system's disk.
- processes: Display a list of processes currently running on the system.
- ports: Display a list of network ports in use.


## Updating the package
If you make any changes to the 'Jarvis' package and want to update the installed version, simply run the pip install . command again. This will overwrite the previous version with the new one.

## Uninstalling the package
To uninstall the 'Jarvis' package and remove the CLI command, run the following command in the terminal:

Copy code
```bash
pip uninstall jarvis
```

This will remove the package and its dependencies from your system.

## Contributing
We welcome contributions to the 'Jarvis' project! If you have an idea for a new feature or have found a bug, please open an issue or submit a pull request.