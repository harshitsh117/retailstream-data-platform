from src.data_access.data_loader import DataLoader


def main():

    customers = DataLoader.load_customers()
    products = DataLoader.load_products()
    orders = DataLoader.load_orders()
    order_items = DataLoader.load_order_items()

    print(f"Customers   : {len(customers)}")
    print(f"Products    : {len(products)}")
    print(f"Orders      : {len(orders)}")
    print(f"Order Items : {len(order_items)}")


if __name__ == "__main__":
    main()