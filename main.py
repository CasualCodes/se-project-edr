# Project AISight | AIDetect | Etc.
import front_end

##--MAIN INITIALIZATION--#
debug = 1

# Main
def main():
    if (debug == 1):
        front_end.front_end_main().run()
    else:
        print("Hello World!")

main()