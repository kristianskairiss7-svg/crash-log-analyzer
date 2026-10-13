import sys
import re

def analyze_crash_log(log_text):
    print("=" * 50)
    print("🔍 ANALYZING CRASH LOG...")
    print("=" * 50)
    
    # Check for Out of Memory
    if "OutOfMemoryError" in log_text:
        print(" [!] CRITICAL: Out of Memory Error detected!")
        print("   -> Fix: Allocate more RAM in your launcher (e.g., -Xmx4G or -Xmx6G).\n")
    
    # Check for Missing Dependencies / Mod Exceptions
    mod_load_fails = re.findall(r"Mod ID: '([^']+)'", log_text)
    if mod_load_fails:
        print(f" [!] Missing or Failed Mods Detected: {set(mod_load_fails)}")
        print("   -> Fix: Check if required dependency mods are installed in your mods folder.\n")
        
    # Find the core 'Caused by' line (where Java actually crashed)
    caused_by = re.findall(r"Caused by:\s+(.*)", log_text)
    if caused_by:
        print(" [!] Root Exception Found:")
        print(f"   -> {caused_by[0]}")
        print()
    else:
        print(" [i] No explicit 'Caused by' statement found. Check top lines for raw exit codes.\n")
        
    print("=" * 50)
    print("Analysis complete.")

if __name__ == "__main__":
    # If a file path is provided in arguments, read it. Otherwise, prompt user input.
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], "r", encoding="utf-8") as f:
                content = f.read()
            analyze_crash_log(content)
        except FileNotFoundError:
            print(f"Error: File '{sys.argv[1]}' not found.")
    else:
        print("Paste your crash log text below (Type 'END' on a new line when finished):")
        lines = []
        while True:
            try:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            except EOFError:
                break
        full_log = "\n".join(lines)
        analyze_crash_log(full_log)
