import requests
import os
import sys

URL = os.getenv("GREEN_API_URL")
INPUT_FILE = "src/sum.py"

if not URL:
    print("❌ GREEN_API_URL not set in environment.")
    sys.exit(1)

def convert_to_green_code():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            code = f.read()

        response = requests.post(URL, json={"code": code})
        response.raise_for_status()

        optimized_code = response.json().get("optimized_code", "")
        if not optimized_code:
            print("❌ No optimized code returned.")
            sys.exit(1)

        with open(INPUT_FILE, "w", encoding="utf-8") as f:
            f.write(optimized_code)

        print(f"✅ Optimized code written to {INPUT_FILE}")

    except Exception as e:
        print(f"❌ Error during optimization: {e}")
        sys.exit(1)

if __name__ == "__main__":
    convert_to_green_code()
