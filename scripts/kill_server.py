import psutil
import os
import signal
import sys


def kill_gunicorn():
    print("Attempting to kill gunicorn processes...")
    killed_count = 0

    current_pid = os.getpid()

    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            # Check for gunicorn in name or cmdline
            name = proc.info["name"]
            cmdline = proc.info["cmdline"] or []

            # Avoid killing self or other tools
            if proc.info["pid"] == current_pid:
                continue

            is_gunicorn = "gunicorn" in name or any("gunicorn" in arg for arg in cmdline)
            is_openalgo = any("openalgo" in arg for arg in cmdline) or any(
                "app:app" in arg for arg in cmdline
            )

            if is_gunicorn and is_openalgo:
                print(f"Killing PID {proc.info['pid']}: {cmdline}")
                proc.kill()
                killed_count += 1

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if killed_count > 0:
        print(f"Successfully killed {killed_count} process(es). Server should be down.")
    else:
        print("No matching gunicorn processes found (or access denied).")


if __name__ == "__main__":
    kill_gunicorn()
