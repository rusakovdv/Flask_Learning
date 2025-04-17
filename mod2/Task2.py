import sys


def get_mean_size():
    lines = sys.stdin.readlines()[1:]
    total_size = 0
    file_count = 0

    for line in lines:
        parts = line.split()
        if len(parts) >= 5:
            try:
                size = int(parts[4])
                total_size += size
                file_count += 1
            except ValueError:
                continue

    if file_count == 0:
        return "No files found or couldn't determine sizes"

    mean_size = total_size / file_count
    return f"Mean file size: {mean_size:.2f} bytes"


if __name__ == '__main__':
    print(get_mean_size())