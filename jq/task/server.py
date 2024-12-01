import subprocess

def main():
    filter = input('filter: ')
    print("[i] filter :", filter)
    if len(filter) >= 9:
        print("Filter is too long")
    elif ";" in filter or "|" in filter or "&" in filter:
        print("Filter contains invalid character")
    else:
        command = "jq '{}' test.json".format(filter)
        ret = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        print(ret.stdout)
        print(ret.stderr)

if __name__ == '__main__':
    main()