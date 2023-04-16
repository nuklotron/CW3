import utils


def main():
    data = utils.load_data()
    data = utils.last_operations(data)
    data = utils.final_result(data)

    for row in data:
        print(row)


if __name__ == "__main__":
    main()
