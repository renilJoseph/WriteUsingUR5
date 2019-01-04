import math
import urx
import logging
import time

def nextChar(initPosInMM, a, v):
    initPosInMM[1]-=0.03 
    poseAngle = convertToDegree(rob.getj())
    poseAngle[0]+=2
    rob.movej(convertToRad(poseAngle), acc=a, vel=v)
    rob.movel(initPosInMM, a, v)
    return rob.getl()

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
    return rob.getl() #return current position after changing in degree

def convertToRad(pos):
    pos = [x*((math.pi)/float(180)) for x in pos ]
    return pos

def convertToDegree(pos):
    pos = [x*(float(180)/(math.pi)) for x in pos ]
    return pos    

def drawA(rob,a, v):
        # drawing A
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        finalPos[2]-=0.2
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, 0.2, 0, rob, a, v, False, None)
        drawLine(0, -0.2, -0.2, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)  

def drawB(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, -0.2, rob, a, v, False, finalPos)
        drawLine(0, 0.2, 0, rob, a, v, False, None)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, -0.2, rob, a, v, False, finalPos)
        drawLine(0, 0.2, 0, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)

def drawC(rob,a, v):      
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        nextChar(initPosInMM, a, v)   

def drawD(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, 0.4, rob, a, v, False, finalPos)
        drawLine(0, 0.2, 0, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)

def drawE(rob,a, v):       
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, False, finalPos)
        finalPos[2]-=0.2
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        finalPos[2]+=0.2
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        nextChar(initPosInMM, a, v)   

def drawF(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        finalPos[2]-=0.2
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        finalPos[2]+=0.2
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        nextChar(initPosInMM, a, v)

def drawG(rob,a, v):      
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, -0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, 0, -0.4, rob, a, v, False, backPos)
        drawLine(0, 0, +0.2, rob, a, v, False, backPos)
        drawLine(0, 0.2, 0, rob, a, v, False, backPos)
        nextChar(initPosInMM, a, v)   

def drawH(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        finalPos[2]-=0.2
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, -0.2, rob, a, v, False, finalPos)
        drawLine(0, 0, -0.4, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)

def drawI(rob,a, v):       
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        finalPos[1]-=0.1
        drawLine(0, 0, 0, rob, a, v, True, finalPos)
        drawLine(0, 0, -0.4, rob, a, v, False, backPos)
        nextChar(initPosInMM, a, v)   

def drawJ(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        finalPos[1]-=0.2
        drawLine(0, -0.4, 0, rob, a, v, True, finalPos)
        drawLine(0, 0, -0.4, rob, a, v, False, None)
        drawLine(0, 0.2, 0, rob, a, v, False, finalPos)
        nextChar(initPosInMM, a, v)

def drawK(rob,a, v):       
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        finalPos[1]-=0.2
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, -0.2, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0.2, rob, a, v, False, backPos)
        nextChar(initPosInMM, a, v)   

def drawL(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)

def drawM(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, -0.2, rob, a, v, False, backPos)
        drawLine(0, -0.2, 0.2, rob, a, v, False, backPos)
        drawLine(0, 0, -0.4, rob, a, v, False, backPos)
        nextChar(initPosInMM, a, v)   

def drawN(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.4, -0.4, rob, a, v, False, None)
        drawLine(0, 0, 0.4, rob, a, v, False, finalPos)
        nextChar(initPosInMM, a, v)

def drawO(rob,a, v):      
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        drawLine(0, 0, 0.4, rob, a, v, False, backPos)
        drawLine(0, 0.2, 0, rob, a, v, False, backPos)
        nextChar(initPosInMM, a, v)   

def drawP(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        drawLine(0, 0, -0.2, rob, a, v, False, finalPos)
        drawLine(0, 0.2, 0, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)

def drawQ(rob,a, v):   
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        drawLine(0, 0, 0.4, rob, a, v, False, backPos)
        finalPos[1]-=0.2
        finalPos[2]-=0.2
        drawLine(0, 0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, -0.3, -0.3, rob, a, v, False, finalPos)
        nextChar(initPosInMM, a, v)   

def drawR(rob,a, v):     
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        drawLine(0, 0, -0.2, rob, a, v, False, backPos)
        drawLine(0, 0.2, 0, rob, a, v, False, backPos)
        drawLine(0, -0.2, -0.2, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)   

def drawS(rob,a, v):      
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.2, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        drawLine(0, 0, -0.2, rob, a, v, False, backPos)
        drawLine(0, 0.2, 0, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)   

def drawT(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        finalPos[1]-=0.2
        drawLine(0, -0.4, 0, rob, a, v, True, finalPos)
        drawLine(0, 0, -0.4, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)

def drawU(rob,a, v):      
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, 0, -0.4, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0, rob, a, v, False, backPos)
        drawLine(0, 0, 0.4, rob, a, v, False, backPos)
        nextChar(initPosInMM, a, v)   

def drawV(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, -0.4, -0.4, rob, a, v, False, finalPos)
        drawLine(0, -0.2, 0.4, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)

def drawW(rob,a, v):     
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, -0.4, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.2, 0.2, rob, a, v, False, backPos)
        drawLine(0, -0.2, -0.2, rob, a, v, False, backPos)
        drawLine(0, -0.4, 0.4, rob, a, v, False, backPos)
        nextChar(initPosInMM, a, v)   

def drawX(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        finalPos[2]-=0.4
        drawLine(0, -0.4, -0.4, rob, a, v, True, finalPos)
        drawLine(0, -0.4, 0.4, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)

def drawY(rob,a, v):
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        finalPos[2]-=0.4
        drawLine(0, -0.2, -0.2, rob, a, v, False, finalPos)
        drawLine(0, 0, -0.2, rob, a, v, False, None)
        drawLine(0, 0, 0.2, rob, a, v, False, None)
        drawLine(0, -0.2, 0.2, rob, a, v, False, None)
        nextChar(initPosInMM, a, v)

def drawZ(rob,a, v):
        # drawing A
        initPosInMM = rob.getl()
        initPoseInDeg = convertToDegree(rob.getj())
        backPos = initPoseInDeg[:]
        finalPos = initPosInMM[:]
        drawLine(0, -0.4, 0, rob, a, v, False, finalPos)
        drawLine(0, 0.4, -0.4, rob, a, v, False, None)
        drawLine(0, -0.4, 0, rob, a, v, True, finalPos)
        nextChar(initPosInMM, a, v)

def draw_(rob,a, v):
        # drawing A
        initPosInMM = rob.getl()
        nextChar(initPosInMM, a, v)
