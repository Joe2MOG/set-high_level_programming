#!/usr/bin/python3
"""N queens puzzle solver"""
import sys


def solve(board, row, n, results):
    if row == n:
        results.append(board[:])
        return
    for col in range(n):
        if safe(board, row, col):
            board.append([row, col])
            solve(board, row + 1, n, results)
            board.pop()


def safe(board, row, col):
    for r, c in board:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve([], 0, N, solutions)
    for sol in solutions:
        print(sol)
