from collections import deque

# packet stream
packets = [
    "S Mary", "P Dee", "P Dee", "E Eileen", "E Mike", "E Joe", "P Dee",
    "E Vicky", "E George", "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
    "P Dee", "S Bill", "S Chase", "E Price", "P Dee", "E Sue"
]

# empty queues for each priority
premium_queue = deque()
standard_queue = deque()
economy_queue = deque()

# parse packets and send to correct que
for packet in packets:
    priority, name = packet.split(maxsplit=1)
    if priority == 'P':
        premium_queue.append(packet)
    elif priority == 'S':
        standard_queue.append(packet)
    elif priority == 'E':
        economy_queue.append(packet)

# Weighted Fair Queue function
def weighted_fair_queue(premium, standard, economy):
    while premium or standard or economy:
        for _ in range(3):
            if premium:
                print(premium.popleft())
        for _ in range(2):
            if standard:
                print(standard.popleft())
        for _ in range(1):
            if economy:
                print(economy.popleft())

# WFQ process
print("Weighted Fair Queue order:")
weighted_fair_queue(premium_queue, standard_queue, economy_queue)