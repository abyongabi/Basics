import random

ls = [
    "May the coming year bring you joy, prosperity, and countless opportunities for personal and professional growth.",
    "Wishing you a year filled with love, laughter, and memorable moments with your loved ones.",
    "May you achieve all your goals and aspirations in the upcoming year, turning your dreams into reality.",
    "Here's to a year of good health, both physically and mentally, allowing you to thrive in every aspect of your life.",
    "May the new year bring you peace and tranquility, providing a serene backdrop for your journey ahead.",
    "Wishing you success in all your endeavors, with each challenge turning into a stepping stone toward greatness.",
    "Here's to a chapter of new beginnings, filled with exciting adventures and positive transformations.",
    "Wishing you strength in existing relationships and the opportunity to build new ones, fostering connections that last a lifetime.",
    "May you find moments of reflection and self-discovery in the upcoming year, leading to a deeper understanding of yourself and your purpose.",
    "Wishing you a year of resilience and perseverance, enabling you to overcome any obstacles and emerge stronger than ever before."
]

name = input("What is your name? ")
print(f"Dear {name},")
print(ls[random.randint(0, len(ls) - 1)])
