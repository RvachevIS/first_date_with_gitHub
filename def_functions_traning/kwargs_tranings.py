def func_with_all_arguments(
                            x: int,
                            y: int,
                            *args,
                            value: int = 6,
                            **kwargs
):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)
person = {
    "city": "Vladimir",
    "first_name": "Ivan",
    "last_name": "Rvachev",
}
func_with_all_arguments(1,
                        2,
                        3, 4, 5,
                        **person)