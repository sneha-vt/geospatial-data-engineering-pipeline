import os
import subprocess
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "src")
LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

log_file = os.path.join(
    LOG_DIR,
    f"pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)

steps = [
    ("Load raw data", "load_data.py"),
    ("Create geospatial data", "create_geodata.py"),
    ("Validate data", "validate_data.py"),
    ("Load data into PostGIS", "load_to_postgis.py"),
]


def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


print("=" * 60)
print("GEOSPATIAL DATA ENGINEERING PIPELINE")
print("=" * 60)

write_log("Pipeline started")

for number, (description, script) in enumerate(steps, start=1):

    print(f"\n[{number}/{len(steps)}] {description}...")
    write_log(f"Started: {description}")

    script_path = os.path.join(SRC_DIR, script)

    try:
        result = subprocess.run(
            [sys.executable, script_path],
            cwd=BASE_DIR,
            capture_output=True,
            text=True
        )

        if result.stdout:
            print(result.stdout)

        if result.returncode != 0:
            print(f"❌ FAILED: {description}")
            print(result.stderr)

            write_log(f"FAILED: {description}")
            write_log(result.stderr)

            sys.exit(result.returncode)

        print(f"✅ SUCCESS: {description}")
        write_log(f"SUCCESS: {description}")

    except Exception as error:
        print(f"❌ ERROR: {error}")
        write_log(f"ERROR: {error}")
        sys.exit(1)

print("\n" + "=" * 60)
print("✅ PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)

write_log("Pipeline completed successfully")
print(f"\nLog file: {log_file}")