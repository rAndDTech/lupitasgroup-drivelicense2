from PIL import Image as PIL,ImageOps,ImageEnhance
from pdf417decoder import PDF417Decoder

class PDFDecoderLicense:

    def __init__(self,imageload):
        self.imageload=imageload
      

    def decode(self):
        image = PIL.open(self.imageload)
        #gray scale
        #new_image = ImageEnhance.Sharpness(image).enhance(1.5)
        #new_image.save("image_7.jpg")
        new_image = ImageOps.grayscale(image)
        new_image.save("image_2.jpg")
        # contraste
       
       
        decoder = PDF417Decoder(image)

        if (decoder.decode() > 0):
            decoded = decoder.barcode_data_index_to_string(0)
            print(decoded)
            return decoded
        else:
            return ""

if __name__ == "__main__":
    
    print(PDFDecoderLicense("org.jpeg").decode())