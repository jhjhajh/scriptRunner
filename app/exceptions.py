# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class NameEntryInvalid(Error):
    """Raised when entry name contains comma, which is the token to parse text file"""
    pass


class FileNotFound(Error):
    """File not found. ask user to delete or put file in the right path"""
    pass

class FileCannotRun(Error):
    """print command cannot be run. check data txt file to see if the command is what you want or the file is correct"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")