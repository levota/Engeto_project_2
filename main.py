from Pomocne_funkce import hra

ODDELOVAC = 47 * "-"

def hlavni():
    print("Hi there!")
    print(ODDELOVAC)
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print(ODDELOVAC)
    hra()

if __name__ == "__main__":
    hlavni()




