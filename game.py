import argparse
import secrets
import hashlib


def create_parser():
    """Parse command line options"""
    parser = argparse.ArgumentParser()
    parser.add_argument('options', nargs='+', type=str)
    return parser.parse_args()


class HashMap:
    def generate(self):
        """Generate secret key and hmac"""
        self.secret_key = secrets.randbits(1024)
        byte_string = bytes(str(self.secret_key), 'utf-8')
        hash_string = hashlib.sha3_256(byte_string)
        secret_hmac = hash_string.hexdigest()  # by hmac-sha3
        print("HMAC: ", secret_hmac)
        return self.secret_key

    def print_key(self):
        print("key: ", self.secret_key)
        print('https://emn178.github.io/online-tools/sha3_256.html')


class Menu:
    """Includes console menu from which the user can choose some case"""

    def __init__(self, list_of_opt):
        self.list_of_opt = list_of_opt

    def print_menu(self):
        """Displays a menu in the console."""
        key = 0
        for item in self.list_of_opt:
            key += 1
            print(key, ":", item)
        print("0 : exit")

    def select_move(self):
        """Allows the user to select one of the menu case"""
        number = int(input("Enter selected number: "))
        if number <= 0 or number > len(self.list_of_opt):
            raise SystemExit
        return number


class Winner:
    """Calculates winner of the game. print_winner method print information about round."""

    def __init__(self, user_move, computer_move):
        self.user_move = user_move
        self.computer_move = computer_move + 1

    def get_result(self, list_of_opt):
        """Return who won"""
        if self.user_move == self.computer_move:
            return -1

        if self.user_move > len(list_of_opt) // 2 + 1:
            if self.computer_move > self.user_move or self.computer_move <= self.user_move + len(
                    list_of_opt) // 2 - len(list_of_opt):
                res = self.user_move
            else:
                res = self.computer_move
        else:
            if self.user_move < self.computer_move <= self.user_move + len(list_of_opt) // 2:
                res = self.user_move
            else:
                res = self.computer_move

        return res

    def print_winner(self, res):
        """Print who won the game"""
        print("User:", self.user_move)
        print("Computer:", self.computer_move)
        if res == -1:
            print("Draw")
        elif res == self.computer_move:
            print("Won computer")
        elif res == self.user_move:
            print("Won user!")


def main():
    try:
        list_of_opt = create_parser().options
        if len(list_of_opt) % 2 == 0:
            raise Exception
        menu = Menu(list_of_opt)
        menu.print_menu()  # Initialize menu
        hashing = HashMap()
        int_key = hashing.generate()
        winner = Winner(menu.select_move(), int(int_key % len(list_of_opt)))
        res = winner.get_result(list_of_opt)
        hashing.print_key()
        winner.print_winner(res)
    except SystemExit:
        pass
    except Exception:
        print("Program doesn`t take {} arguments".format(len(list_of_opt)))


if __name__ == '__main__':
    main()
