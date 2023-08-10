def cost_delivery(quantity, *args, discount=0):
    if quantity <= 0:
        return 0

    first_item_cost = 5
    additional_item_cost = 2

    total_cost = first_item_cost + (quantity - 1) * additional_item_cost

    if discount > 0 and discount <= 1:
        total_cost *= (1 - discount)

    return total_cost
