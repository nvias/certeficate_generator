from webPage.web_page import run
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-c','--config',help="Config file by read me")
    args = parser.parse_args()
    f = 0
    try:
        f = open(args.config, "r")
    except:
        print("Config file not found")
        raise
    conf = f.readlines()
    f.close()
    conf = [item.strip() for item in conf]
    run(conf[1])
