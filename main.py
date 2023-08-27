
from src.components import data_ingestion
from src.components import data_transformation
from src.components import model_trainer


if __name__=="__main__":
    obj =  data_ingestion.DataIngestion()
    train_path,test_path= obj.initiate_data_ingestion()
    DT = data_transformation.DataTransformation()
    train_arr,test_arr,preprocessor= DT.initiate_data_transformation(train_path,test_path)
    MT= model_trainer.ModelTrainer()
    print(MT.initiate_model_trainer(train_arr,test_arr))
