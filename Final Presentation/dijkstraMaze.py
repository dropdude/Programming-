from pyamaze import maze,agent,COLOR,textLabel
import time
def dijkstra(m,*h,start=None):
    if start is None:
        start=(m.rows,m.cols)

    hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in m.grid}
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        if currCell==m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal]
            



if __name__=='__main__':
    m=maze(5,5)
    m.CreateMaze(1,1,loopPercent=40)

    h6=agent(m,2,3,color=COLOR.red)

    h6.cost=100

    path,c=dijkstra(m,h6,start=(5,5))
    textLabel(m,'Total Cost',c)

    # a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
    a=agent(m,5,5,color=COLOR.cyan,filled=True,footprints=True)
    m.tracePath({a:path})

    tic = time.perf_counter()
    m.run()
    toc = time.perf_counter()

    print(f"Solved the small maze with Uniform Search in {toc - tic:0.4f} seconds")

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

    # path,c=dijstra(myMaze,h1,h2,h2,h3,h4,h5)
    path,c=dijkstra(myMaze,h1,h2,h3,h4,h5,start=(10,15))
    textLabel(myMaze,'Total Cost',c)

    # a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
    a=agent(myMaze,10,15,color=COLOR.cyan,filled=True,footprints=True)
    myMaze.tracePath({a:path})

    tic = time.perf_counter()
    myMaze.run()
    toc = time.perf_counter()

    print(f"Solved the large maze with Uniform Search in {toc - tic:0.4f} seconds")

    