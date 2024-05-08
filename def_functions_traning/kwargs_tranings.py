def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modify = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modify = True

    return old_dict, is_modify


product = {"id": 1, "name": "Laptop", "price": 999.99}
structure = modify_dict(old_dict=product, name="Laptop")

print(structure)
print(type(structure))