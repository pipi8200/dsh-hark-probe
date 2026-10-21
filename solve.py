def prime_square_sum(n: int) -> int:
    if n < 2:
        return 0
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(range(i * i, n + 1, i)))
    return sum(i * i for i in range(n + 1) if sieve[i])


if __name__ == "__main__":
    print(prime_square_sum(1_000_000))
