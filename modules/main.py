# import shopping.more_shopping.shopping_cart
# importing specific functions from package
# from shopping.more_shopping.shopping_cart import buy
from utility import divide,multiply

# importing whole package
from shopping.more_shopping import shopping_cart

# __name__ specifies the file name, __main__ is the file which will run when we run play
#  good way to check which file is loaded and run
if __name__=='__main__':
    print(shopping_cart.buy('apple'))
    print("divide(5,2)",divide(5,2))
    print("multiply(5,2)",multiply(5,2))

    print("__name__",__name__)