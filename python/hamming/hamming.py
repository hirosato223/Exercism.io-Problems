def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be same length!")
    hammingDistance = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hammingDistance += 1
    return hammingDistance
