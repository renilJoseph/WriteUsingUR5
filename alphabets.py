import math
import urx
import logging
import time

def nextChar(initPosInMM, a, v):
    initPosInMM[1]-=0.03 
    poseAngle = convertToDegree(rob.getj())
    poseAngle[0]+=2
    rob.movej(convertToRad(poseAngle), acc=a, vel=v)
    rob.movel(initialPosInMM, a, v)
    return pose

def drawLine(valx, valy, valz, rob, a, v, comeback, backPos):
    poseinmm = rob.getl()
    poseinmm[0]+=valx
    poseinmm[1]+=valy
    poseinmm[2]+=valz
    rob.movel(poseinmm, acc=a, vel=v)

    if comeback:
        poseAngle = convertToDegree(rob.getj())
        poseAngle[0]+=2
        rob.movej(convertToRad(poseAngle), acc=a, vel=v)
        rob.movel(backPos, acc=a, vel=v)
    return pose #return current position after changing in degree

def convertToRad(pos):
    pos = [x*((math.pi)/float(180)) for x in pos ]
    return pos

def convertToDegree(pos):
    pos = [x*(float(180)/(math.pi)) for x in pos ]
    return pos    

def drawA(rob,a, v):
        # drawing A
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        finalPos[2]-=0.2
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, 0.2, 0, rob, a, v, False, None)
        drawLine(0, -0.2, -0.2, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)  

def drawB(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, -0.2, rob, a, v, False, finalPos)
        drawLine(0, 0.2, 0, rob, a, v, False, None)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, -0.2, rob, a, v, False, finalPos)
        drawLine(0, 0.2, 0, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)

def drawC(rob,a, v):      
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        nextChar(initialPosInMM, a, v)   

def drawD(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, 0.4, rob, a, v, False, finalPos)
        drawLine(0, 0.2, 0, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)

def drawE(rob,a, v):       
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, False, finalPos)
        finalPos[2]-=0.2
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        finalPos[2]+=0.2
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        nextChar(initialPosInMM, a, v)   

def drawF(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        finalPos[2]-=0.2
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        finalPos[2]+=0.2
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        nextChar(initialPosInMM, a, v)

def drawG(rob,a, v):      
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, 0, -0.4, rob, a, v, False, backPos)
        drawLine(0, 0, +0.2, rob, a, v, False, backPos)
        drawLine(0, 0.2, 0, rob, a, v, False, backPos)
        nextChar(initialPosInMM, a, v)   

def drawH(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        finalPos[2]-=0.2
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, -0.2, rob, a, v, False, finalPos)
        drawLine(0, 0, -0.4, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)

def drawI(rob,a, v):       
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        finalPos[1]-=0.1
        drawLine(0, 0, 0, rob, a, v, True, finalPos)
        drawLine(0, 0, -0.4, rob, a, v, False, backPos)
        nextChar(initialPosInMM, a, v)   

def drawJ(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        finalPos[1]-=0.2
        drawLine(0, -0.4, 0, rob, a, v, True, finalPos)
        drawLine(0, 0, -0.4, rob, a, v, False, None)
        drawLine(0, 0.2, 0, rob, a, v, False, finalPos)
        nextChar(initialPosInMM, a, v)

def drawK(rob,a, v):       
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        finalPos[1]-=0.2
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, -0.2, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0.2, rob, a, v, False, backPos)
        nextChar(initialPosInMM, a, v)   

def drawL(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)

def drawM(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, -0.2, rob, a, v, False, backPos)
        drawLine(0, -0.2, 0.2, rob, a, v, False, backPos)
        drawLine(0, 0, -0.4, rob, a, v, False, backPos)
        nextChar(initialPosInMM, a, v)   

def drawN(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.4, -0.4, rob, a, v, False, None)
        drawLine(0, 0, 0.4, rob, a, v, False, finalPos)
        nextChar(initialPosInMM, a, v)

def drawO(rob,a, v):      
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        drawLine(0, 0, 0.4, rob, a, v, False, backPos)
        drawLine(0, 0.2, 0, rob, a, v, False, backPos)
        nextChar(initialPosInMM, a, v)   

def drawP(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, -0.2, rob, a, v, False, finalPos)
        drawLine(0, 0.2, 0, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)

def drawQ(rob,a, v):   
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        drawLine(0, 0, 0.4, rob, a, v, False, backPos)
        finalPos[1]-=0.2
        finalPos[2]-=0.2
        drawLine(0, 0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, -0.3, -0.3, rob, a, v, False, finalPos)
        nextChar(initialPosInMM, a, v)   

def drawR(rob,a, v):     
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        drawLine(0, 0, -0.2, rob, a, v, False, backPos)
        drawLine(0, 0.2, 0, rob, a, v, False, backPos)
        drawLine(0, -0.2, -0.2, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)   

def drawS(rob,a, v):      
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.2, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        drawLine(0, 0, -0.2, rob, a, v, False, backPos)
        drawLine(0, 0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)   

def drawT(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        finalPos[1]-=0.2
        drawLine(0, -0.4, 0, rob, a, v, True, finalPos)
        drawLine(0, 0, -0.4, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)

def drawU(rob,a, v):      
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        drawLine(0, 0, 0.4, rob, a, v, False, backPos)
        nextChar(initialPosInMM, a, v)   

def drawV(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, -0.4, -0.4, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0.4, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)

def drawW(rob,a, v):     
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, -0.4, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0.2, rob, a, v, False, backPos)
        drawLine(0, -0.2, -0.2, rob, a, v, False, backPos)
        drawLine(0, -0.4, 0.4, rob, a, v, False, backPos)
        nextChar(initialPosInMM, a, v)   

def drawX(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        finalPos[2]-=0.4
        drawLine(0, -0.4, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.4, 0.4, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)

def drawY(rob,a, v):
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        finalPos[2]-=0.4
        drawLine(0, -0.2, -0.2, rob, a, v, False, finalPos)
        drawLine(0, 0, -0.2, rob, a, v, False, None)
        drawLine(0, 0, 0.2, rob, a, v, False, None)
        drawLine(0, -0.2, 0.2, rob, a, v, False, None)
        nextChar(initialPosInMM, a, v)

def drawZ(rob,a, v):
        # drawing A
        initlPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initlPosInMM[:]
        drawLine(0, -0.4, 0, rob, a, v, False, finalPos)
        drawLine(0, 0.4, -0.4, rob, a, v, False, None)
        drawLine(0, -0.4, 0, rob, a, v, True, finalPos)
        nextChar(initialPosInMM, a, v)

def draw_(rob,a, v):
        # drawing A
        initlPosInMM = rob.getl()
        nextChar(initialPosInMM, a, v)
