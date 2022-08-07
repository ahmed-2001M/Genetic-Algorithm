from algo import let_the_game_begin
import pickle 
import math 


def save(res):
    how = open('po.obj', 'wb') 
    pickle.dump(res, how)

if __name__ == '__main__':
    gen, res = let_the_game_begin(boardSize=6, populationSize=300, mutation_probability=0.2)
    print(gen)
    save(res)
    res.draw_chromosome()