#!/usr/bin/env python
import avatargen
import sys
import random

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
CANVAS_SIZE = 400


def main():
    global CANVAS_SIZE
    block_size = int(CANVAS_SIZE / 6)

    block_count = int(random.randint(2,10))
    output = f"avatars/{random.randint(100000000,999999999)}{random.choice(chars)}.png"

    with avatargen.generate(size=CANVAS_SIZE,
                            block_size=block_size,
                            block_count=block_count) as avatar:
        avatar.save(output)


if __name__ == "__main__":
    for _ in range(int(input("Введите кол-во аватаров: "))):
        main()
    print("Проверьте папку avatars")
