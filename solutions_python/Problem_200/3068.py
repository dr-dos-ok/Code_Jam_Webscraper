import logging

# Package-wide logging configuration
logging.basicConfig(format='%(levelname)s: %(module)s(%(lineno)s): %(message)s', level=logging.WARNING)
LOG = logging.getLogger()

num_cases = int(input())
LOG.info('Number of cases %d', num_cases)

# 111110
# 099999


def is_tidy(string):
    LOG.info('Evaluating %s', string)
    if len(string) == 1:
        return True
    for i in range(len(string) - 1):
        LOG.debug("%s %s", string[i+1], string[i])
        if string[i+1] < string[i]:
            return False
    return True


for case in range(1, num_cases + 1):
    number = int(input())
    LOG.info('Case #%d: Problem: %d', case, number)

    while True:
        if is_tidy(str(number)):
            break
        else:
            number = number - 1

    print("Case #{}: {}".format(case, number))
