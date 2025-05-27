def HandleException() -> None:
    """
    Testing exception handling in Python.
    """
    try:
        print('A')
        val = 1 / 0  # This will raise a ZeroDivisionError
        print(val)
        print('B') # not printed due to the exception

    except ZeroDivisionError as e:
        # raise e # This will raise the exception again, but it is caught by the same except block.
        # code will move to finally block after this, and print m
        # since the forced exception is caught and not handled it will throw error.
        # output A M error.
        print('C')
    except Exception as e:
        print('D') # not printed due to the specific exception above.
    finally:
        print('E') # This will always be printed regardless of the exception.

if __name__ == "__main__":
    HandleException()