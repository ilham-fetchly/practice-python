import time

print("Press ENTER to start the stopwatch")
print("and, press ENTER again to 'lap' the stopwatch")
print("Press CTRL+C to stop")

# infinite loop
while True:
    try:
        input()  # wait for Enter to start
        start_time = time.time()
        print("Stopwatch started...")

        # another loop to wait for the second Enter key press
        while True:
            try:
                input()
                end_time = time.time()
                lap_time = round(end_time - start_time, 2)
                print("Lap time:", lap_time, "seconds")
                start_time = end_time  # reset the start time

            except KeyboardInterrupt:
                print("Stopwatch stopped...")
                break

    except KeyboardInterrupt:
        print("Exiting...")
        break
