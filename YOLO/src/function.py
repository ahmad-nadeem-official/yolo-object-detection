'''
main function to run the YOLO model
'''

'''install ultralytics if not installed'''
# !pip install ultralytics

from ultralytics import YOLO

def detection(path, confidence, model):
  print("welcome to obejct detection by YOLO")
  model = YOLO(model)
  result = model(source=path, show=True, conf=confidence, save=True)
  return result

path = input("please enter the path of video :")
confidence = float(input("please enter the confidence value: "))
model = input("please enter the model :")
if model == "":
  model = "yolov8n.pt"


detection(path, confidence, model)