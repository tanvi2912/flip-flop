J = 0
K = 0

# Initialize the flip flop output and state
output = 0
state = 0

# Define the flip flop function
def jk_flip_flop(J, K, state):
    if J == 1 and K == 1:
        # Toggle the flip flop state
        if state == 0:
            state = 1
        else:
            state = 0
    elif J == 1:
        # Set the flip flop state to 1
        state = 1
    elif K == 1:
        # Set the flip flop state to 0
        state = 0
    # Output the flip flop state
    return state

# Test the flip flop function with various inputs
output = jk_flip_flop(0, 0, output)
print("Output: ", output)  # Output: 0

output = jk_flip_flop(1, 0, output)
print("Output: ", output)  # Output: 1

output = jk_flip_flop(0, 1, output)
print("Output: ", output)  # Output: 0

output = jk_flip_flop(1, 1, output)
print("Output: ", output)  # Output: 1

output = jk_flip_flop(1, 1, output)
print("Output: ", output)  # Output: 0