def linear_search_product(product_list, target_product):
    indices = []

    # Iterate through the product_list and check each product
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)

    return indices

# Example usage:
products = ["Apple", "Banana", "Apple", "Orange", "Apple", "Grapes"]
target = "Apple"
result = linear_search_product(products, target)
if result:
    print(f"The product '{target}' was found at indices: {result}")
else:
    print(f"The product '{target}' was not found in the list.")
