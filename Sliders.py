import cv2

def Track_Check(x):
	pass

class Sliders:
	def __init__(self, image_path, slider_type = "HSV", image_scale = 1, 
					num_blur_passes = 1, blur_filter_size = (3, 3)):
		'''
		image_path: The image path
		
		slider_type: The type of sliders that you want to use. The available 
		options are HSV, BGR, LAB, Canny, Binary

		image_scale: The scale by which you wish to resize the image. 
		Values smaller than 1 will reduce the image size while values larger
		than 1 will increase the image size
		
		num_blur_passes: The number of times the image should be blurred
		
		blur_filter_size: The size of the blurring filter
		'''
		self.image_path = image_path
		self.slider_type = slider_type.upper()
		self.image_scale = image_scale
		self.num_blur_passes = num_blur_passes
		self.blur_filter_size = blur_filter_size

		if self.slider_type not in ["HSV", "BGR", "LAB", "CANNY", "BINARY"]:
			raise ValueError("The slider type is not valid. The following slider types are valid: HSV, BGR, LAB, CANNY, BINARY")
	
	def Blur_Image(self, image):
		'''
		Blur the images with the specified blurring filter size.
		'''
		for i in range(self.num_blur_passes):
			image = cv2.GaussianBlur(image, self.blur_filter_size, 0)

		return image

	def Load_Image(self):
		'''
		Load the image and resize it with the given scale value
		'''
		image = cv2.imread(self.image_path)
		R, C, Z = image.shape
		image = cv2.resize(image, (int(C*self.image_scale), int(R*self.image_scale)))

		return image

	def Start_Slider_Display(self):	
		'''
		This function starts the appropriate slider display depending
		on the value provided in the slider_type variable
		'''
		self.original_image = self.Load_Image()
		image = self.Blur_Image(self.original_image)

		if self.slider_type == "HSV":
			self.HSV_Slider(image)

		elif self.slider_type == "BGR":
			self.RGB_Slider(image)

		elif self.slider_type == "LAB":
			self.LAB_Slider(image)

		elif self.slider_type == "CANNY":
			self.Canny_Edge_Slider(image)

		elif self.slider_type == "BINARY":
			self.Binary_Slider(image)

	def HSV_Slider(self, image):
		'''
		This is where the HSV sliders are started
		'''
		hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		
		cv2.namedWindow("Sliders")
		
		cv2.createTrackbar("High-H", "Sliders", 255, 255, Track_Check)
		cv2.createTrackbar("High-S", "Sliders", 255, 255, Track_Check)
		cv2.createTrackbar("High-V", "Sliders", 255, 255, Track_Check)
		
		cv2.createTrackbar("Low-H", "Sliders", 0, 255, Track_Check)
		cv2.createTrackbar("Low-S", "Sliders", 0, 255, Track_Check)
		cv2.createTrackbar("Low-V", "Sliders", 0, 255, Track_Check)

		while True:
			high_H = cv2.getTrackbarPos("High-H", "Sliders")
			high_S = cv2.getTrackbarPos("High-S", "Sliders")
			high_V = cv2.getTrackbarPos("High-V", "Sliders")

			low_H = cv2.getTrackbarPos("Low-H", "Sliders")
			low_S = cv2.getTrackbarPos("Low-S", "Sliders")
			low_V = cv2.getTrackbarPos("Low-V", "Sliders")

			low = (low_H, low_S, low_V)
			high = (high_H, high_S, high_V)

			mask = cv2.inRange(hsv_image, low, high)

			segmented = cv2.bitwise_and(self.original_image, self.original_image, mask=mask)

			cv2.imshow("Original", self.original_image)
			cv2.imshow("Mask", mask)
			cv2.imshow("Segmented", segmented)

			k = cv2.waitKey(30)
			if k == ord("q"):
				break
		
		cv2.destroyAllWindows()


	def RGB_Slider(self, image):
		'''
		This is where the RGB sliders are started
		'''
		cv2.namedWindow("Sliders")
		
		cv2.createTrackbar("High-B", "Sliders", 255, 255, Track_Check)
		cv2.createTrackbar("High-G", "Sliders", 255, 255, Track_Check)
		cv2.createTrackbar("High-R", "Sliders", 255, 255, Track_Check)
		
		cv2.createTrackbar("Low-B", "Sliders", 0, 255, Track_Check)
		cv2.createTrackbar("Low-G", "Sliders", 0, 255, Track_Check)
		cv2.createTrackbar("Low-R", "Sliders", 0, 255, Track_Check)

		while True:
			high_B = cv2.getTrackbarPos("High-B", "Sliders")
			high_G = cv2.getTrackbarPos("High-G", "Sliders")
			high_R = cv2.getTrackbarPos("High-G", "Sliders")

			low_B = cv2.getTrackbarPos("Low-B", "Sliders")
			low_G = cv2.getTrackbarPos("Low-G", "Sliders")
			low_R = cv2.getTrackbarPos("Low-R", "Sliders")

			low = (low_B, low_G, low_R)
			high = (high_B, high_G, high_R)

			mask = cv2.inRange(image, low, high)

			segmented = cv2.bitwise_and(self.original_image, self.original_image, mask=mask)

			cv2.imshow("Original", self.original_image)
			cv2.imshow("Mask", mask)
			cv2.imshow("Segmented", segmented)

			k = cv2.waitKey(30)
			if k == ord("q"):
				break
		
		cv2.destroyAllWindows()

	def LAB_Slider(self, image):
		'''
		This is where the LAB sliders are started
		'''
		lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		
		cv2.namedWindow("Sliders")
		
		cv2.createTrackbar("High-L", "Sliders", 255, 255, Track_Check)
		cv2.createTrackbar("High-A", "Sliders", 255, 255, Track_Check)
		cv2.createTrackbar("High-B", "Sliders", 255, 255, Track_Check)
		
		cv2.createTrackbar("Low-L", "Sliders", 0, 255, Track_Check)
		cv2.createTrackbar("Low-A", "Sliders", 0, 255, Track_Check)
		cv2.createTrackbar("Low-B", "Sliders", 0, 255, Track_Check)

		while True:
			high_L = cv2.getTrackbarPos("High-L", "Sliders")
			high_A = cv2.getTrackbarPos("High-A", "Sliders")
			high_B = cv2.getTrackbarPos("High-B", "Sliders")

			low_L = cv2.getTrackbarPos("Low-L", "Sliders")
			low_A = cv2.getTrackbarPos("Low-A", "Sliders")
			low_B = cv2.getTrackbarPos("Low-B", "Sliders")

			low = (low_L, low_A, low_B)
			high = (high_L, high_A, high_B)

			mask = cv2.inRange(lab_image, low, high)

			segmented = cv2.bitwise_and(self.original_image, self.original_image, mask=mask)

			cv2.imshow("Original", self.original_image)
			cv2.imshow("Mask", mask)
			cv2.imshow("Segmented", segmented)

			k = cv2.waitKey(30)
			if k == ord("q"):
				break
		
		cv2.destroyAllWindows()

	def Canny_Edge_Slider(self, image):
		'''
		This is where the Canny sliders are started
		'''
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		
		cv2.namedWindow("Sliders")
		
		cv2.createTrackbar("Thresh 1", "Sliders", 255, 255, Track_Check)
		cv2.createTrackbar("Thresh 2", "Sliders", 255, 255, Track_Check)

		while True:
			thresh_1 = cv2.getTrackbarPos("Thresh 1", "Sliders")
			thresh_2 = cv2.getTrackbarPos("Thresh 2", "Sliders")

			mask = cv2.Canny(gray, thresh_1, thresh_2)

			cv2.imshow("Original", self.original_image)
			cv2.imshow("Edge Mask", mask)

			k = cv2.waitKey(30)
			if k == ord("q"):
				break
		
		cv2.destroyAllWindows()

	def Binary_Slider(self, image):
		'''
		This is where the Binary sliders are started
		'''
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		
		cv2.namedWindow("Sliders")
		
		cv2.createTrackbar("Thresh", "Sliders", 255, 255, Track_Check)

		while True:
			thresh = cv2.getTrackbarPos("Thresh", "Sliders")

			ret, mask= cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)

			segmented = cv2.bitwise_and(self.original_image, self.original_image, mask=mask)

			cv2.imshow("Original", self.original_image)
			cv2.imshow("Mask", mask)
			cv2.imshow("Segmented", segmented)


			k = cv2.waitKey(30)
			if k == ord("q"):
				break
		
		cv2.destroyAllWindows()