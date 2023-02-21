import sys


def print_result(total):
    print('+' + '-' * 3 + '+')
    print('|' + str(total) + '|')
    print('+' + '-' * 3 + '+')


def main():
    on = True
    seq = ''
    var = ''
    total = 0

    while True:
        line = sys.stdin.readline()
        if not line:
            break

        for char in line:
            char = char.upper()
            if on:
                if '0' <= char <= '9':
                    seq += char
                else:
                    if seq:
                        total += int(seq)
                        seq = ''
                    match char:
                        case 'O':
                            var = char
                        case 'F':
                            if var == 'OF':
                                on = False
                                var = ''
                            elif var == 'O':
                                var += char
                        case '=':
                            print_result(total)
                        case other:
                            var = ''
            else:
                match char:
                    case 'O':
                        var = char
                    case 'N':
                        if var == 'O':
                            on = True
                            var = ''
                    case '=':
                        print_result(total)
                    case other:
                        var = ''
    print_result(total)


if __name__ == '__main__':
    main()
