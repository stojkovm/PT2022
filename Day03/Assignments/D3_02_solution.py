def convert(fn_filename, ln_filename):
    with open(fn_filename, "r") as input1:
        with open(ln_filename, "r") as input2:
            with open("full_names.txt", "w") as output:
                for line1, line2 in zip(input1, input2):
                    output.write(
                        f"{line1.strip()} {line2.lower().capitalize()}")


if __name__ == "__main__":
    convert('first_names.txt', "last_names.txt")
