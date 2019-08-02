import pyfpgrowth

def extract_frequent_patterns(fpat, thres):
    """
    Args:
        fpat: File pointer to file containing frequent
            patterns.
        thres: Threshold to use in FPgrowth algo.

    Returns:
        All frequent patterns found using FPgrowth
    """

    all_patterns_lines = [line.strip().split(';') for line in fpat.readlines()]
    all_patterns = []

    for item_list in all_patterns_lines:
        pattern = []
        for item in item_list:
            pattern.append(item.replace(' ', '_'))
        all_patterns.append(pattern)

    return pyfpgrowth.find_frequent_patterns(all_patterns, thres)

if __name__ == '__main__':
    print(extract_frequent_patterns(open('../dataset/sample_patterns.txt', 'r'), 0.1))
