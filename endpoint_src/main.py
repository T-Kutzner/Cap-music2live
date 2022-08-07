from present_function import main_function
import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/home")
def show_album_data():
   data = main_function()
   print(data) 
   

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)