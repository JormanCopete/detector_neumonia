
import unittest
import UI_main
import Backend
import Inference

class TestUtils(unittest.TestCase):
    def test_prediction_validate_normal(self):
        imageArray, img2show = Backend.read_jpg_file('E:\\Especalizacion IA\\DPIA\\images\\NORMAL2-IM-0826-0001.jpeg')
        predictionLabel, predictionProba, predictionHeatmap = Inference.predict(imageArray)
        self.assertEqual(predictionLabel, "normal")
        self.assertGreaterEqual(predictionProba,51)
        self.assertNotEqual(predictionLabel, "bacteriana")

    def test_prediction_validate_bacteriana(self):
        imageArray, img2show = Backend.read_jpg_file('E:\\Especalizacion IA\\DPIA\\images\\person364_bacteria_1659.jpeg')
        predictionLabel, predictionProba, predictionHeatmap = Inference.predict(imageArray)
        self.assertEqual(predictionLabel, "bacteriana")
        self.assertGreaterEqual(predictionProba,51)
        self.assertNotEqual(predictionLabel, "viral")
        
    def test_prediction_validate_viral(self):
        imageArray, img2show = Backend.read_jpg_file('E:\\Especalizacion IA\\DPIA\\images\\person1323_virus_2283.jpeg')
        predictionLabel, predictionProba, predictionHeatmap = Inference.predict(imageArray)
        self.assertEqual(predictionLabel, "viral")
        self.assertGreaterEqual(predictionProba,51)
        self.assertNotEqual(predictionLabel, "normal")
               

#python -m unittest testmain.py