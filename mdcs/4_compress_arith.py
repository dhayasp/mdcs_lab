def get_unique_char(message):
    unique_char = []
    for character in message:
        unique = True
        for e in unique_char:
            if e == character:
                unique = False
                break
        if unique:
            unique_char.append(character)
    return unique_char


def get_frequency(message, unique_char):
    frequency = {}
    for character in unique_char:
        char_freq = 0
        for e in message:
            if character == e:
                char_freq += 1
        frequency[character] = char_freq
    return frequency


def get_occurring_probability(message, frequency):
    probability = {}
    message_length = len(message)
    for key, value in frequency.items():
        probability[key] = value / message_length
    return probability


def get_cumulative_sum(lower_bound, upper_bound, probability_ls):
    cumulative_sum = [lower_bound]
    diff = upper_bound - lower_bound
    char_lower_bound = lower_bound
    for probability in probability_ls:
        char_upper_bound = char_lower_bound + (diff * probability)
        cumulative_sum.append(char_upper_bound)
        char_lower_bound = char_upper_bound
    return cumulative_sum


def associate_key_with_interval(cumulative_sum, unique_char):
    interval = {}
    for i in range(len(cumulative_sum) - 1):
        interval[unique_char[i]] = [cumulative_sum[i], cumulative_sum[i + 1]]
    return interval


def get_tag(probability, unique_char, message):
    probability_ls = [probability[key] for key in unique_char]
    cumulative_sum = get_cumulative_sum(0.0, 1.0, probability_ls)
    print('Cumulative sum for interval [0, 1): ', cumulative_sum)
    interval_dict = associate_key_with_interval(cumulative_sum, unique_char)
    tag = 0.0
    for character in message:
        char_interval = interval_dict.get(character)
        char_lower_bound = char_interval[0]
        char_upper_bound = char_interval[1]
        tag = (char_lower_bound + char_upper_bound) / 2.0
        cumulative_sum = get_cumulative_sum(
            char_lower_bound, char_upper_bound, probability_ls)
        interval_dict = associate_key_with_interval(
            cumulative_sum, unique_char)
    return tag


def concatenate_char(ls):
    return ''.join(ls)


def arithmetic_encoding(message):
    unique_char = get_unique_char(message)
    print('Unique char in the message:', unique_char)
    frequency = get_frequency(message, unique_char)
    print('Frequency of each unique character:', frequency)
    probability = get_occurring_probability(message, frequency)
    print('Occurring probability of each unique character:', probability)
    tag = get_tag(probability, unique_char, message)
    return tag, probability


def arithmetic_decoding(probability, message_length, tag):
    probability_ls = list(probability.values())
    unique_char = list(probability.keys())
    cumulative_sum = get_cumulative_sum(0.0, 1.0, probability_ls)
    interval_dict = associate_key_with_interval(cumulative_sum, unique_char)
    message_char_ls = []
    current_lower_bound = 0.0
    current_upper_bound = 1.0
    for _ in range(message_length):
        for key, value in interval_dict.items():
            lower_bound, upper_bound = value
            if lower_bound < tag < upper_bound:
                message_char_ls.append(key)
                current_lower_bound = lower_bound
                current_upper_bound = upper_bound
                cumulative_sum = get_cumulative_sum(
                    current_lower_bound, current_upper_bound, probability_ls)
                interval_dict = associate_key_with_interval(
                    cumulative_sum, unique_char)
                break
    return concatenate_char(message_char_ls)


def run_arithmetic_coding():
    message = 'OpenGenus'
    message_len = len(message)
    print('The message is', message)
    print('The length of the message is', message_len)
    tag, probability = arithmetic_encoding(message)
    print('The tag for', message, 'is', tag)
    decoded_msg = arithmetic_decoding(probability, message_len, tag)
    print('Decoded message:', decoded_msg)


if __name__ == '__main__':
    run_arithmetic_coding()
