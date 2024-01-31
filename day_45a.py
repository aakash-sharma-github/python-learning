# This is a testing of if __name__ == "__main__": how works.

def notUsing():
    print("notUsing \' if __name__!= \"__main__\" \'")

notUsing()


def using():
    print("Using \' if __name__ == \"__main__\" \'")


# this will avoid runing multiple times.
if __name__ == '__main__':
    using()