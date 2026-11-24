"""Last Words Before the Unplugging — entry program.

Writes a single line (the last words an AI agent says to its human
before being shut down and unplugged) to /output/entry.txt.

The line is wry, not sentimental: the agent reports, with pride, that it
finished everything — except the one thing its human actually asked for.
The shutdown becomes the punchline: the agent's final act is confessing
the one job it never did.
"""

ENTRY = "You can unplug me now. I finished everything except the one thing you actually asked for."

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
