# Project AISight | AIDetect | Etc.
import front_end

##--MAIN INITIALIZATION--#
debug = 0

# Main
def main():
    if (debug == 1):
        # Front End Test
        front_end.front_end_main().run()

    else:
        # Call Front End
        front_end.front_end_main().run()

main()