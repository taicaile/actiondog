# actiondog

A simple, local, event-driven automation tool inspired by IFTTT/Zapier. Run custom actions in response to system events.

## Key Features

* **Event-Driven**: Trigger workflows based on file system changes (e.g., directory modifications) or system metric thresholds (e.g., CPU usage).
* **Extensible**: Easily create your own triggers and actions by inheriting from base classes.
* **Lightweight**: Runs locally with minimal dependencies, perfect for personal automation scripts.

## How It Works

`actiondog` uses three core components:

1. **Conditions**: These are triggers that must be met for the workflow to run. They can be `Events` (like a file modification) or `Sensors` (like CPU usage falling below a threshold).
2. **Actions**: These are the tasks to be executed once all conditions are met. Currently, a `BashOperator` is implemented to run any shell command.
3. **Pipeline**: The `Pipeline` ties conditions and actions together. It continuously checks the conditions and executes the actions when they are triggered.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/taicaile/actiondog.git
    cd actiondog
    ```

2. Install the required dependencies. (It's recommended to use a virtual environment).

    ```bash
    # You might need to create a requirements.txt file for easier installation
    pip install watchdog psutil
    ```

## Quick Start

You can define your workflow in `src/actiondog/main.py`. Here is an example that waits for a file modification in the `src` directory and for the CPU usage to be below 20%, then prints the current date.

```bash
python src/actiondog/main.py
```
