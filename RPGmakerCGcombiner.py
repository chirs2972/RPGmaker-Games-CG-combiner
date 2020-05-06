import os, sys
import glob
import shutil
from PIL import Image

mode = 4

if not os.path.exists("Input3"): 
	mode=mode-1    #floder is exist or not
	os.mkdir("Input3")
	print("Input3 has created")
elif not os.listdir("Input3"):  
	mode=mode-1	#floder is empty or not
else:
    images4 = glob.glob("Input3/*.png")		#load pics in images3 list

if not os.path.exists("Input2"): 
	mode=mode-1
	os.mkdir("Input2")
	print("Input2 has created")
elif not os.listdir("Input2"):  
	mode=mode-1
else:
    images3 = glob.glob("Input2/*.png")


if not os.path.exists("Base"):
	os.mkdir("Base") 
	print("Base has created")
if not os.path.exists("Input1"): 
	os.mkdir("Input1")
	print("Input1 has created")
if not (os.listdir("Input1") or os.listdir("Base")):
	print("base and input1 folder must be not empty")
	os.system("pause")
	os._exit(0)

print("Mode is "+str(mode))

def phase4(result2,images4,i,j,k):		#combine 4 pics
	for l in range(0,len(images4)):
		file = open(images4[l],'rb')
		im4 = Image.open(file)
		im4 = im4.convert('RGBA')
		resultpic = Image.alpha_composite(result2,im4)
		resultpic.save("Output/"+fname+"_"+str(i)+"_"+str(j)+"_"+str(k)+"_"+str(l)+".PNG")
		print("Output "+fname+"_"+str(i)+"_"+str(j)+"_"+str(k)+"_"+str(l)+".PNG")


def phase3(result,images3,i,j):			#combine 3 pics
	if (mode == 4) :
		for k in range(0,len(images3)):
			file = open(images3[k],'rb')
			im3 = Image.open(file)
			im3 = im3.convert('RGBA')
			resultpic = Image.alpha_composite(result,im3)
			phase4(resultpic,images4,i,j,k)
	else:
		for k in range(0,len(images3)):
			file = open(images3[k],'rb')
			im3 = Image.open(file)
			im3 = im3.convert('RGBA')
			resultpic = Image.alpha_composite(result,im3)
			resultpic.save("Output/"+fname+"_"+str(i)+"_"+str(j)+"_"+str(k)+".PNG")
			print("Output "+fname+"_"+str(i)+"_"+str(j)+"_"+str(k)+".PNG")


images1 = glob.glob("Base/*.png")
images2 = glob.glob("Input1/*.png")


for i in range(0,len(images1)):
	file = open(images1[i],'rb')
	fname ,fext = os.path.splitext(images1[i])  #split path and extension name
	fname = fname.split('\\',1)[1]  #split path and file name
	im1 = Image.open(file)
	resultpic = Image.new('RGBA',im1.size,(0,0,0,0))
	im1 = im1.convert('RGBA')
	for j in range(0,len(images2)):
		if(mode > 2) :
			file = open(images2[j],'rb')
			im2 = Image.open(file)
			im2 = im2.convert('RGBA')
			resultpic = Image.alpha_composite(im1,im2)
			phase3(resultpic,images3,i,j)
		else :
			file = open(images2[j],'rb')
			im2 = Image.open(file)
			im2 = im2.convert('RGBA')
			resultpic = Image.alpha_composite(im1,im2)
			resultpic.save("Output/"+fname+"_"+str(i)+"_"+str(j)+".PNG")
			print("Output "+fname+"_"+str(i)+"_"+str(j)+".PNG")