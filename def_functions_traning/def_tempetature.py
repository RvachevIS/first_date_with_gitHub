COMFORTABLE_TEMPERATURE = 25


def get_diff_from_comfortable_temperature(*, temperature: int) -> int:
    return COMFORTABLE_TEMPERATURE - temperature


if __name__ == '__main__':
    print(
        get_diff_from_comfortable_temperature(temperature=20))