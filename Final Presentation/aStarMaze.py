from pyamaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue
import time
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)
def aStar(m):
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,(1,1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(5,5)
    m.CreateMaze(1,1,loopPercent=40)

    h6=agent(m,2,3,color=COLOR.red)

    h6.cost=100

    path=aStar(m)

    a=agent(m,footprints=True)
    m.tracePath({a:path})
    l=textLabel(m,'A Star Path Length',len(path)+1)

    tic = time.perf_counter()
    m.run()
    toc = time.perf_counter()

    print(f"Solved the small maze with a* in {toc - tic:0.4f} seconds")


    myMaze=maze(10,15)
    myMaze.CreateMaze(1,1,loopPercent=40)
    # myMaze.CreateMaze(loadMaze='dijkMaze.csv')

    h1=agent(myMaze,3,2,color=COLOR.red)
    h2=agent(myMaze,6,12,color=COLOR.red)
    h3=agent(myMaze,4,14,color=COLOR.red)
    h4=agent(myMaze,9,2,color=COLOR.red)
    h5=agent(myMaze,8,7,color=COLOR.red)

    h1.cost=100
    h2.cost=100
    h3.cost=100
    h4.cost=100
    h5.cost=100

    path=aStar(myMaze)

    a=agent(myMaze,footprints=True)
    myMaze.tracePath({a:path})
    l=textLabel(myMaze,'A Star Path Length',len(path)+1)

    tic = time.perf_counter()
    myMaze.run()
    toc = time.perf_counter()

    print(f"Solved the large maze with a* in {toc - tic:0.4f} seconds")