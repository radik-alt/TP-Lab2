from model import taskOne as One, taskTwo as Two, taskThree as Three


def main():
    number = int(input())
    match number:
        case 1:
            return One.main()
        case 2:
            pass
        case 3:
            pass

main()