import math
import urx
import logging
import time


def nextChar(pose):
    pose[0]+=3
    rob.movej(convertToRad(pose), acc=a, vel=v)
    return pose

def downLine(x, y, pose,rob, comeback, backPos):
    # pose[1]-=x
    # pose[2]+=y
    # rob.movej(convertToRad(pose), acc=a, vel=v)
    poseinmm = rob.getl()
    poseinmm[2]-=0.04
    rob.movel(poseinmm, acc=a, vel=v)

    if comeback:
        pose[0]+=3
        rob.movej(convertToRad(pose), acc=a, vel=v)
        rob.movej(convertToRad(backPos), acc=a, vel=v)
        pose = backPos
    return pose

def rightLine(pose,rob, comeback, backPos):
    # pose[1]+=0.1
    # pose[2]+=5
    # rob.movel(convertToRad(pose), acc=a, vel=v)
    poseinmm = rob.getl()
    poseinmm[1]-=0.02
    pose= convertToDegree(rob.getj())
    rob.movel(poseinmm, acc=a, vel=v)
    if comeback:
        pose[0]+=3
        rob.movej(convertToRad(pose), acc=a, vel=v)
        rob.movel(backPos, acc=a, vel=v)
        pose = backPos
    return pose

def leftLine(pose,rob, comeback, backPos):
    pose[1]+=0.1
    pose[2]-=5
    rob.movej(convertToRad(pose), acc=a, vel=v)
    if comeback:
        pose[0]+=3
        rob.movej(convertToRad(pose), acc=a, vel=v)
        rob.movej(convertToRad(backPos), acc=a, vel=v)
        pose = backPos
    return pose    

def midDownDiag(x, y, pose,rob, comeback, backPos):
    pose[1]-=x
    pose[2]+=y
    rob.movej(convertToRad(pose), acc=a, vel=v)
    if comeback:
        pose[0]+=3
        rob.movej(convertToRad(pose), acc=a, vel=v)
        rob.movej(convertToRad(backPos), acc=a, vel=v)
        pose = backPos
    return pose

def midUpDiag(pose,rob, comeback, backPos):
    pose[1]+=5
    pose[2]-=5
    rob.movej(convertToRad(pose), acc=a, vel=v)
    if comeback:
        pose[0]+=3
        rob.movej(convertToRad(pose), acc=a, vel=v)
        rob.movej(convertToRad(backPos), acc=a, vel=v)
        pose = backPos
    return pose    

def downDiag(pose,rob, comeback, backPos):
    pose[1]-=10
    pose[2]+=10
    rob.movej(convertToRad(pose), acc=a, vel=v)
    if comeback:
        pose[0]+=3
        rob.movej(convertToRad(pose), acc=a, vel=v)
        rob.movej(convertToRad(backPos), acc=a, vel=v)
        pose = backPos
    return pose

def upDiag(pose,rob, comeback, backPos):
    pose[1]+=10
    pose[2]-=10
    rob.movej(convertToRad(pose), acc=a, vel=v)
    if comeback:
        pose[0]+=3
        rob.movej(convertToRad(pose), acc=a, vel=v)
        pose = rob.movej(convertToRad(backPos), acc=a, vel=v)
        pose = pose = backPos
    return pose    


def convertToRad(pos):
    pos = [x*((math.pi)/float(180)) for x in pos ]
    return pos

def convertToDegree(pos):
    pos = [x*(float(180)/(math.pi)) for x in pos ]
    return pos    

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARN)

    rob = urx.Robot("192.168.43.107")
    #rob = urx.Robot("localhost")
    rob.set_tcp((0,0,0,0,0,0))
    rob.set_payload(0.5, (0,0,0))
    try:
        l = 0.05
        v = 1
        a = 0.3
        po = rob.getl()
        print "po::::", po
        # po = convertToDegree(po)
        # print "po converted to degree:", po

        pose = rob.getj()
        print("robot tcp is at: ", pose)
        # print("absolute move in base coordinate ")
        pose = convertToDegree(pose)
        print "converted to degree:", pose

        # rob.movej(convertToRad((93.10,-163.73, 81.47, -196.21, -2.84, 175.99)), a, v)

        # posPrev = pose[:]
        # postPrevTofindNew = po[:]

        # pose = downLine(10, 9, pose, rob, False, posPrev)
        # pose = rightLine(po, rob, False, posPrev)
        # po[1]+=0.02 
        # rob.movel(po, acc=a, vel=v)

# *************************************888
        # writing R
        # pose = downLine(10, 9, pose, rob, True, posPrev)
        # drawing right line
        poseinmm = rob.getl()
        poseinmm[1]-=0.04
        rob.movel(poseinmm, acc=a, vel=v)
        # # pose = rightLine(pose, rob, False, posPrev)
        # # drawring down line
        # poseinmm = rob.getl()
        # poseinmm[2]-=0.02
        # rob.movel(poseinmm, acc=a, vel=v)
        # # pose = downLine(5, 4.5, pose, rob, False, posPrev)
        # # drawing left line
        # poseinmm = rob.getl()
        # poseinmm[1]+=0.02
        # rob.movel(poseinmm, acc=a, vel=v)
        # # pose = leftLine(pose, rob, False, posPrev)
        # # drawing midDownDiag
        # poseinmm = rob.getl()
        # poseinmm[1]-=0.02
        # poseinmm[2]-=0.02
        # rob.movel(poseinmm, acc=a, vel=v)
        # pose = midDownDiag(5, 10, pose, rob, False, posPrev)

        # # pose = nextChar(postPrevTofindNew)
        # pose = rob.getj()
        # pose = convertToDegree(pose)
        # pose[0]+=3
        # rob.movej(convertToRad(pose), acc=a, vel=v)
        # postPrevTofindNew[1]-=0.04
        # rob.movel(postPrevTofindNew, acc=a, vel=v)        

# ****************************
        # writing E
        # pose = rob.getj()
        # pose = convertToDegree(pose)
        # posPrev = pose[:]
        # poseMM = rob.getl()
        # posPrevTofindNew = poseMM[:]

        # pose = downLine(10, 9, pose, rob, False, posPrev)
        # # drawing right line
        # # poseinmm = rob.getl()
        # # poseinmm[1]-=0.02
        # # rob.movel(poseinmm, acc=a, vel=v)
        # posPrev = rob.getl()
        # posPrev[2]+=0.02
        # pose = rightLine(pose, rob, True, posPrev)
        # # pose = rightLine(pose, rob, False, posPrev)
        # posPrev = rob.getl()
        # posPrev[2]+=0.02
        # rightLine(pose, rob, True, posPrev)
        # # pose = downLine(5, 4.5, pose, rob, False, posPrev)
        # # drawing left line
        # posPrev = rob.getl()
        # posPrev[2]+=0.02
        # rightLine(pose, rob, False, posPrev)
        
        # # pose = nextChar(postPrevTofindNew)
        # pose = rob.getj()
        # pose = convertToDegree(pose)
        # pose[0]+=3
        # rob.movej(convertToRad(pose), acc=a, vel=v)
        # postPrevTofindNew[1]-=0.04
        # rob.movel(postPrevTofindNew, acc=a, vel=v)        

       


# ***********************************************

        # print "update pose", pose

        # rob.movej(convertToRad(pose), acc=a, vel=v)

        # pose[2] -= 1
        # print "pos after", pose
        # pose = convertToRad(pos)
        # rob.movej(pose, acc=a, vel=v)

        # rob.movej((0.01,-28.62,6.22,-77.69,-2.41,-12.96), acc=a, vel=v)
        # rob.movej(pose, acc=a, vel=v)
        # print("relative move in base coordinate ")
        # rob.translate((0, 0, -l), acc=a, vel=v)
        # print("relative move back and forth in tool coordinate")
        # rob.translate_tool((0, 0, -l), acc=a, vel=v)
        # rob.translate_tool((0, 0, l), acc=a, vel=v)
    finally:
        rob.close()

