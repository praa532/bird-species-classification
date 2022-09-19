from os.path import join, exists
from os import listdir, makedirs
from shutil import move
import random


species = [
   "001.Black_footed_Albatross",
"002.Laysan_Albatross",
"003.Sooty_Albatross",
"004.Groove_billed_Ani",
"005.Crested_Auklet",
"006.Least_Auklet",
"007.Parakeet_Auklet",
"008.Rhinoceros_Auklet",
"009.Brewer_Blackbird",
"010.Red_winged_Blackbird",
"011.Rusty_Blackbird",
"012.Yellow_headed_Blackbird",
"013.Bobolink",
"014.Indigo_Bunting",
"015.Lazuli_Bunting",
"016.Painted_Bunting",
"017.Cardinal",
"018.Spotted_Catbird",
"019.Gray_Catbird",
"020.Yellow_breasted_Chat",
]

train_dir = "C:\\Project\\Train data"
validation_dir = "C:\\Project\\test"   



def create_validation():
    """Validation data sepration from augmented training images.
    Number of images chosen for validation depends upon the
    number of images present in the directory. If less than 100,
    then 10 images are moved into validation folder. Similarly,
    two if conditions for cases with less than 110 and greater
    than 150. Images are selected using random sampling.
    """
    
    
    
    
    train_imgs="C:\\Project\\Train"
    
    for bird_specie in species: 
        train_imgs_path = join(train_dir, bird_specie)
        validation_img_path= join(validation_dir, bird_specie) 
        
        if not exists(join(validation_dir, bird_specie)): 
            makedirs(join(validation_dir, bird_specie))
        
        train_imgs = listdir(train_imgs_path)
        number = len(train_imgs)  # number of images in each category
        
        
        if number < 78:
            validation_separation = random.sample(train_imgs, 6)
            for img_file in validation_separation:
                move(join(train_imgs_path, img_file),
                    join(validation_img_path, img_file))

        elif 78 <= number <= 85:
                validation_separation = random.sample(train_imgs, 8)
                for img_file in validation_separation:
                    move(join(train_imgs_path, img_file),
                         join(validation_img_path, img_file))

        elif number > 85:
            validation_separation = random.sample(train_imgs, 9)
            for img_file in validation_separation:
                move(join(train_imgs_path, img_file),
                         join(validation_img_path, img_file))
       
        


if __name__ == "__main__":
            
    create_validation() 
