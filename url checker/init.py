from robobrowser import RoboBrowser

def main():
    browser = RoboBrowser(history=True)
    browser.open("localhost:8000")
    

if __name__ == "__main__":
    main()


