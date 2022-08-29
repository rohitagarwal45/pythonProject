import random


# high = int(input("enter range "))
# user_no = int(input("enter the no to be guessed "))
#
# def range(high):
#
#     low = 1
#     count = 0
#     random_no = 0
#     while random_no != user_no:
#         random_no = random.randint(low, high)
#         print(f"randum no - {random_no}")
#         count = count + 1
#         if random_no < user_no:
#             low = random_no
#         else :
#             high = random_no
#
#     return count
#
# count1 = range(high)
# print(f"guess no is matched at {count1} times")

# Rock Papper Scissors game
def game():
    user = input("What's ur choise Rock (R) , Papper (P) and Scissors (S) \n").lower()
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer selection is {computer}")

    if user == computer:
        print("its a draw")
        exit()

    if logic1(user, computer):
        print('You win')
        exit()
    else:
        print('Computer wins')
        exit()


def logic1(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') \
        or (user == 's' and computer == 'p'):
        return True


game()
