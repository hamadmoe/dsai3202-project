from predict import run_prediction

def run_batch_pipeline():
    print("Starting batch prediction pipeline...")
    
    run_prediction()
    
    print("Batch pipeline complete.")

if __name__ == "__main__":
    run_batch_pipeline()