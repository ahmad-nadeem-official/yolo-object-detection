'''
main function to run the YOLO model
'''

def detection(path, confidence, model):
  print("welcome to obejct detection by YOLO")
  model = YOLO(model)
  result = model(source=path, show=True, conf=confidence, save=True)
  return result