#import cv2
import numpy as np
import os
import pytesseract
from PIL import Image
from io import BytesIO
from flask import jsonify


# roi_per_img = {"/deep_learning_samples/10_jpg/img_1.jpg": (940, 1040),
#                "/deep_learning_samples/10_jpg/img_2.jpg": (940, 1040),
#                "/deep_learning_samples/10_jpg/img_3.jpg": (940, 1040),
#                "/deep_learning_samples/10_jpg/img_4.jpg": (940, 1040),
#                "/deep_learning_samples/10_jpg/img_5.jpg": (940, 1040),
#                "/deep_learning_samples/10_jpg/img_6.jpg": (940, 1040),
#                "/deep_learning_samples/10_jpg/img_7.jpg": (940, 1040),
#                "/deep_learning_samples/10_jpg/img_8.jpg": (940, 1040),
#                "/deep_learning_samples/10_jpg/img_9.jpg": (940, 1040),
#                "/deep_learning_samples/10_jpg/img_10.jpg": (940, 1040)
#                }


# def get_roi(image_path):

#     img = cv2.imread(image_path)
#     return img
#     x1, x2 = roi_per_img[image_path]
#     return img[x1:x2, :]



def cheque_micr_data(img):

      image = cv2.imread(img)
      cheque_data = pytesseract.image_to_string(image, lang='mcr')
      cheque_data = cheque_data.strip()
      micr_data = cheque_data.splitlines()[-1]
      micr_data = micr_data.split()
      micr_data.pop(3)
      routing_number = micr_data[0]
      routing_number = routing_number.strip('c')
      account_number = micr_data[1]
      account_number = account_number[:-1]
      cheque_number = micr_data[2]
      cheque_number = cheque_number[:-1]
      final_output = {"Routing Number":routing_number, "Account Number":account_number, "Cheque Number":cheque_number}
      # print((final_output))
      return final_output



def american_cheque_micr_data(img):

  image = cv2.imread(img)
  american_cheque_data = pytesseract.image_to_string(image, lang='mcr')
  american_cheque_data = american_cheque_data.strip()
  micr_data = american_cheque_data.splitlines()[-1]
  micr_data = micr_data.split()
  routing_number = micr_data[0]
  routing_number = routing_number.strip('c')
  account_number = micr_data[1]
  account_number = account_number.strip('a')
  cheque_number = micr_data[2]
  cheque_number = cheque_number[:-1]
  final_output = {"Routing Number":routing_number, "Account Number":account_number, "Cheque Number":cheque_number}
  return final_output


def bank_of_america_cheque(img):
  image = cv2.imread(img)
  b_american_cheque_data = pytesseract.image_to_string(image, lang='mcr')
  b_american_cheque_data = b_american_cheque_data.strip()
  micr_data = b_american_cheque_data.splitlines()[-1]
  micr_data = micr_data.split()
  routing_number = micr_data[0]
  routing_number = routing_number.strip('a')
  process_number = micr_data[1]
  processed_number = process_number.split('c')
  account_number = processed_number[0]
  cheque_number = processed_number[1]
  final_output = {"Routing Number":routing_number, "Account Number":account_number, "Cheque Number":cheque_number}
  return final_output



      
# # if __name__ == "__main__":

# #     img_dir = "deep_learning_samples/cheque_samples.jpeg"
# #     result = cheque_micr_data(img_dir)
# #     print(result)




