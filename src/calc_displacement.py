import pandas as pd
import numpy as np

num = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']
suite = ['s', 'c', 'h']

def create_allcards():
    allcards = []
    for s in suite:
        for n in num:
            allcards.append(n+s)
    return allcards

def create_original_pos(cards):
    return {cards[v]:(v+1) for v in range(len(cards))}

def calc_mean_disp(card_found, original_pos, num_of_trials):
    mean_disps = []
    n_cards = len(original_pos)
    for n in range(num_of_trials):
        sum = 0
        for i in range(1, n_cards+1):
            displacement = abs( i - original_pos[card_found[n*n_cards + (i-1)]] )
            sum += displacement
        mean_disps.append(sum/n_cards)
    return mean_disps


if __name__ == "__main__":
    cards = create_allcards()

    original_pos = create_original_pos(cards)
    print(original_pos)

    plastic_df = pd.read_csv('../data/plastic_deck_50_trials.csv')
    plastic_df['card_found'] = plastic_df['card_found'].str.lower()
    plastics_found = plastic_df['card_found'] #list

    paper_df = pd.read_csv('../data/paper_deck_50_trials.csv')
    paper_df['card_found'] = paper_df['card_found'].str.lower()
    papers_found = paper_df['card_found'] #list

    num_of_trials = 50

    plastic_mean_disp = calc_mean_disp(plastics_found, original_pos, num_of_trials)
    paper_mean_disp = calc_mean_disp(papers_found, original_pos, num_of_trials)

    df = pd.DataFrame({'plastic':plastic_mean_disp, 'paper':paper_mean_disp})
    df.to_csv('../data/mean_displacements.csv')