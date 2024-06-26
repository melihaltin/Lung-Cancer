from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    data_source : str
    local_data_file : Path
    unzip_dir : Path
    
    
    

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict  
    


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_file: Path
    transformed_data_file: Path
    
    
@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    train_data: Path
    
    

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    target_column: str