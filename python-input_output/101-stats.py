#!/usr/bin/python3
"""Log parsing script that computes metrics from stdin."""
import sys

total_size = 0
status_counts = {}
valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0

def print_stats():
    print("File size: {:d}".format(total_size))
    for code in sorted(status_counts):
        print("{:d}: {:d}".format(code, status_counts[code]))

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        # Correct minimum token count: IP - [date] "GET /path HTTP/1.1" code size → 8 tokens
        if len(parts) >= 8:
            try:
                size = int(parts[-1])
                code = int(parts[-2])
                total_size += size
                if code in valid_codes:
                    status_counts[code] = status_counts.get(code, 0) + 1
            except ValueError:
                pass
        if line_count % 10 == 0:
            print_stats()
    # Final summary after all lines (even if empty)
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
