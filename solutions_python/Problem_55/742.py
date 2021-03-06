import sys

class RollerCoaster:
    '''Represents a theme park roller coaster'''

    def __init__(self, rides_per_day, number_of_seats):
        self.rides_per_day = rides_per_day
        self.number_of_seats = number_of_seats

    def calculate_profit(self, groups):
        profit = 0

        for i in range(self.rides_per_day):

            number_of_people = 0
            for i, group_size in enumerate(groups):

                if number_of_people + group_size <= self.number_of_seats:
                    number_of_people += group_size
                else:
                    break
            
            profit += number_of_people
            groups = groups[i:] + groups[:i]  # Updates the queue for the next ride 

        return profit


def main():
    if len(sys.argv) > 1:
        input_filename = sys.argv[1]

        input_file = open(input_filename)
        output_file = open(input_filename.replace('.in', '.out'), 'w')

        case_number = 0
        for i, line in enumerate(input_file):
            if i == 0:
                number_of_inputs = int(line)
            else:
                case_number += 1
                R, k, N = map(int, line.split())
                groups = map(int, input_file.next().split())

                roller_coaster = RollerCoaster(R, k)
                profit = roller_coaster.calculate_profit(groups)

                output_file.write('Case #{0}: {1}\n'.format(case_number, profit))

        input_file.close()
        output_file.close()


if __name__ == '__main__':
    main()
