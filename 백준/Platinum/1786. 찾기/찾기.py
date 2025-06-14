def compute_prefix_array(pattern):
    lps = [0] * len(pattern)
    match_len = 0

    for idx in range(1, len(pattern)):
        while match_len > 0 and pattern[idx] != pattern[match_len]:
            match_len = lps[match_len - 1]
        if pattern[idx] == pattern[match_len]:
            match_len += 1
            lps[idx] = match_len
    return lps


def search_pattern(text, keyword, prefix):
    positions = []
    match_idx = 0
    total_matches = 0

    for i in range(len(text)):
        while match_idx > 0 and text[i] != keyword[match_idx]:
            match_idx = prefix[match_idx - 1]

        if text[i] == keyword[match_idx]:
            if match_idx == len(keyword) - 1:
                total_matches += 1
                positions.append(i - len(keyword) + 2)
                match_idx = prefix[match_idx]
            else:
                match_idx += 1

    return total_matches, positions


# 입력
text_input = input()
pattern_input = input()

# 전처리 및 탐색
prefix_table = compute_prefix_array(pattern_input)
match_count, indices = search_pattern(text_input, pattern_input, prefix_table)

# 출력
print(match_count)
print(*indices)
