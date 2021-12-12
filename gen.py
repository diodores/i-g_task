import data


def flat_generator(nested_list):
    for _ in sum(nested_list, []):
        yield _


for item in flat_generator(data.nested_list):
    print(item)
