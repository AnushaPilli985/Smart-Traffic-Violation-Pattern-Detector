import pickle
from pickle import dump
data={
    "name":"hello",
    "age":23,
    "branch":"cse"
}
with open("data.pickel","wb") as file:
    pickle.dump(data.file)