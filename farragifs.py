from PIL import Image
from PIL import ImageSequence
import os

def getFramesCount(gifPath):
    openGif = Image.open(gifPath)
    print("gif frames = " + str(openGif.n_frames))

def printAllFrames(gifPath,folderName):
    openGif = Image.open(gifPath)
    os.mkdir(f'{folderName}')
    initNumber = 0
    for frame in ImageSequence.Iterator(openGif):
        initNumber += 1
        frame.save(f'{folderName}/{str(initNumber)}.png',format = "png", lossless = True)

def printSomeFrames(gifPath, howManyFrames,folderName):
    openGif = Image.open(gifPath)
    framesCount = str(openGif.n_frames)
    
    if str(howManyFrames) > framesCount:
        print(f"the number of frames that you entered {howManyFrames} is greater than frames in gif {framesCount}")
        print('the number of frames that you enter must be equal or smaller than the frames in gif')
    else:
        os.mkdir(f'{folderName}')
        for i in range(howManyFrames):
            openGif.seek(openGif.n_frames // howManyFrames * i)
            openGif.save(f"{folderName}"'/{}.png'.format(i+1))






