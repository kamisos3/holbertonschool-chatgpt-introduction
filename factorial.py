#!/usr/bin/python3
num = int(sys.argv[1])
if num < 0:
    raise ValueError("Number must be non-negative.")
    except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

    f = factorial(num)
    print(f)
