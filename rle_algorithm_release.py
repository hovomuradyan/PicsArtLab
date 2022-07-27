def compress_rle(content):
    compressed_content = ""
    start_symbol = ""
    symbols_length = 0
    if len(content) > 2:
        for i in range(len(content)):
            if i == 0:
                start_symbol = content[i]
                symbols_length += 1
            else:
                current_symbol = content[i]
                if current_symbol == start_symbol and not current_symbol.isnumeric():
                    symbols_length += 1
                else:
                    if symbols_length > 1:
                        compressed_content += start_symbol + str(symbols_length)
                    else:
                        compressed_content += start_symbol
                    symbols_length = 1
                    start_symbol = current_symbol
        if symbols_length > 1:
            compressed_content += start_symbol + str(symbols_length)
        else:
            compressed_content += start_symbol
    else:
        return "ERROR: content must have 2+ symbols"
    return compressed_content


def decompress_rle(compressed_content):
    decompressed_content = ""
    if len(compressed_content) > 2:
        for i in range(len(compressed_content)):
            if i != 0:
                if compressed_content[i].isnumeric() and not compressed_content[i - 1].isnumeric():
                    decompressed_content += compressed_content[i - 1] * (int(compressed_content[i]) - 1)
                else:
                    decompressed_content += compressed_content[i]
            else:
                decompressed_content += compressed_content[i]
    else:
        return "ERROR: content must have 2+ symbols"
    return decompressed_content


print(compress_rle("aaaabbbcc"))
print(decompress_rle("a4b3cc"))
