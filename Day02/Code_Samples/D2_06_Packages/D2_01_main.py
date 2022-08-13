"""
 - With __init__.py having all components that can be used in other modules
    their import is easier than writing e.g.:
    from purchase.cart import add_to_cart
"""
import purchase


def main():
    purchase.add_to_cart('James', 'Cart1', 'TV')
    purchase.do_payment('James', 500)


if __name__ == "__main__":
    main()
