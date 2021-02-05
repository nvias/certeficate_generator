from webPage.web_page import run

if __name__ == "__main__":
    f = open("config", "r")
    conf = f.readlines()
    f.close()
    conf = [item.strip() for item in conf]
    run(conf[1])
