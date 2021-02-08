import pygame
import sys
from pygame.locals import *
import random

pygame.init()

# Tạo cửa sổ
DISPLAYSURF = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('All Forward Yugi!')
DISPLAYSURF.fill((0, 0, 0))

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Thêm card vào


font = pygame.font.SysFont('consolas', 30)
deck = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS',
        '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
        '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
        '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD']

print(deck)

random.shuffle(deck)


def draw(n):
    hand = []
    for i in range(n):
        hand.append(deck.pop())
    return hand


hand = draw(10)

hand.sort()


def show_hand(hand_card):
    for (i, card) in enumerate(hand_card):
        hand_card[i] = pygame.transform.scale(pygame.image.load(f'PNG\\{card}.png'), (96, 140))
    return hand_card


hand_card = show_hand(hand)
print(hand_card)

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for (i, card) in enumerate(hand_card):
        DISPLAYSURF.blit(card, pygame.Rect(30 + i * 30, 20, 0, 0))
    pygame.display.flip()
