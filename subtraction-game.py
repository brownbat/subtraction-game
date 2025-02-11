import random
import time
import sys

def subtraction_game():
    num_digits = 1
    rounds = []
    correct_streak = 0

    while True:
        num1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        num2 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        if num1 < num2:
            num1, num2 = num2, num1

        print(", ".join(str(r["time"]) for r in rounds))  # Print historical times
        print()
        print("Subtract:")
        print(num1)
        print(num2)

        start_time = time.time()
        while True:
            try:
                sys.stdout.flush()
                user_input = input("> ")
                user_answer = int(user_input.strip())
                if user_answer == num1 - num2:
                    break
                else:
                    print("Incorrect!")
                    correct_streak = 0  # Reset streak on incorrect answer
            except ValueError:
                print("Please enter a valid integer.")
            except OSError as e:
                print(f"I/O error occurred: {e}")
                return

        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)
        rounds.append({"values": (num1, num2), "time": elapsed_time})

        # Adjust threshold to (num_digits + 1)² seconds
        if elapsed_time < (num_digits + 1) ** 2:
            correct_streak += 1
        else:
            correct_streak = 0

        if correct_streak >= 3:
            num_digits += 1
            correct_streak = 0  # Reset streak for new difficulty level

        print("\033c", end="")  # Clears the terminal screen

if __name__ == "__main__":
    subtraction_game()
