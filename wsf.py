import __help__
import argparse
import update
import sys

# --- func excutble ---
def wsf() -> None:
    import main

    # -- display menu help --
    if "-h" in sys.argv or "--help" in sys.argv:
        __help__.__help__()
        sys.exit()

    # --- Main Modes ---
    parser = argparse.ArgumentParser(description="wsf", add_help=False)
    parser.add_argument("-u", action="store_true", help="Updata Program")
    parser.add_argument("-a", action="store_true", help="Assmble File")
    parser.add_argument("-w", action="store_true", help="Write Scritpt File")
    
    parser.add_argument("-t", type=str, help="Select Type File")
    parser.add_argument("-s", type=str, help="Save File Path")
    parser.add_argument("-n", type=str, help="Name file")

    arg = parser.parse_args()

    # --- install or updata path ---
    if arg.u:
        update.check()
        sys.exit()

    # --- Assmble file ---
    if arg.a:

        # --- write file ---
        if arg.w:
            write = True
        else:
            write = False  

        import main
        main.Assmble(arg.n, arg.t, arg.s, write)

# ---- main ----
if __name__ == "__main__":
    wsf()