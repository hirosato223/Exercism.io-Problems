def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError("Requested length is larger than input string")
    output = []
    for idx in range(0, len(series)-length+1):
        chunk = series[idx:idx+length]
        output.append(chunk)
    return output
