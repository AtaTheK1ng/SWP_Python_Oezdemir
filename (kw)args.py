
def myFunction(parameter_1, parameter_2, *args, **kwargs):
    print(f"Parameter 1: {parameter_1}")
    print(f"Parameter 2: {parameter_2}")
    if args:
        for arg in args:
            print(f"Args: {arg}")
    if kwargs:
        for key, value in kwargs.items():
            print(f"Kwargs: {key} - {value}")

def main():
    args = (100, 200, 300)
    kwargs = {'extra': 'info'}
    myFunction('A', *args, **kwargs)

if __name__ == "__main__":
    main()