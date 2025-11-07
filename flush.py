import subprocess

def flush_dns():
    try:
        # macOS DNS flush
        cmd = ["sudo", "killall", "-HUP", "mDNSResponder"]

        print("ENTER PWD:")
        subprocess.run(cmd, check=True)
        print("FLUSED")

    except subprocess.CalledProcessError:
        print("REJECTED.")
    except Exception as e:
        print("ERROR:", e)


if __name__ == "__main__":
    flush_dns()
