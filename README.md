# Minecraft Crash Log Analyzer

A lightweight Python command-line utility designed to parse chaotic Java and Minecraft crash logs, isolate root exceptions (`Caused by`), and instantly detect common issues like `OutOfMemoryError` or missing mod dependencies.

## Features
- **Out of Memory Detection:** Flags JVM memory exhaustion and recommends RAM allocation fixes.
- **Missing Mod Identification:** Scans logs for failed mod loads and missing dependencies.
- **Root Exception Isolation:** Extracts the exact `Caused by` line where Java crashed.

## Usage

Run the script directly in your terminal:

```bash
python main.py
