import os
import time
import sys
import random

# Define different "currents" in the river — each with unique words and speeds
currents = [
    {"words": ["flow", "dream", "motion", "whisper", "echo", "drift", "calm"], "speed": 0.03},
    {"words": ["ripple", "wave", "spark", "glide", "stream", "softly"], "speed": 0.04},
    {"words": ["peace", "breeze", "shine", "quiet", "silk"], "speed": 0.05},
]

# Prepare the river strings (repeated to make them long enough)
for c in currents:
    river = " ".join(c["words"]) + " "
    c["river"] = river * 10
    c["offset"] = random.randint(0, len(c["river"]))  # random starting point

width = os.get_terminal_size().columns
last_update = [0.0 for _ in currents]

def get_wrapped_slice(s, start, length):
    """Return a string slice that wraps around seamlessly."""
    end = start + length
    if end <= len(s):
        return s[start:end]
    else:
        return s[start:] + s[:end - len(s)]

try:
    while True:
        sys.stdout.write("\033[H")  # Move cursor to top

        current_time = time.time()
        for idx, c in enumerate(currents):
            if current_time - last_update[idx] >= c["speed"]:
                c["offset"] = (c["offset"] + 1) % len(c["river"])
                last_update[idx] = current_time

            line = get_wrapped_slice(c["river"], c["offset"], width)
            sys.stdout.write(line + "\n")

        sys.stdout.flush()
        time.sleep(0.01)

except KeyboardInterrupt:
    print("\nRiver stopped.")
