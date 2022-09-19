def prime(n):

    for i in range(2, n):
        if (n % i == 0):
            print(i, 'False')
            return False
        else:
            print(i, 'True')
            return True

if __name__ == '__main__':
    prime(13)