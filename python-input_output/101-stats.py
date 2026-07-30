#!/usr/bin/python3
"""Log parsing script that computes metrics from stdin."""
import sys

total_size = 0
status_counts = {}
valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0


def print_stats():
    """Print accumulated statistics."""
    print("File size: {:d}".format(total_size))
    for code in sorted(status_counts):
        print("{:d}: {:d}".format(code, status_counts[code]))


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        # Independently parse size (last token) and status code (second-to-last)
        if len(parts) >= 2:
            # Process size
            try:
                size = int(parts[-1])
                total_size += size
            except ValueError:
                size = None

            # Process status code (unrelated to size)
            if len(parts) >= 2:
                try:
                    code = int(parts[-2])
                    if code in valid_codes:
                        status_counts[code] = status_counts.get(code, 0) + 1
                except ValueError:
                    pass

        if line_count % 10 == 0:
            print_stats()
    # Final summary after all lines
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
