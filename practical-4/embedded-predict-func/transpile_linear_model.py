import os
import joblib
from sklearn.linear_model import LinearRegression

def load_model(filename: str) -> LinearRegression | None:
    if (os.path.exists(filename) and os.path.isfile(filename)):
        return joblib.load(filename)
    return None

def generate_predict_fun(model: LinearRegression, filename: str) -> None:
    bias = model.intercept_
    n_features = len(model.coef_)
    with open(filename, 'w') as f:
        f.write("#include <stdio.h>\n")
        f.write("#include <stdlib.h>\n\n")
        f.write("float predict(float *features, int n_features)\n")
        f.write("{\n")
        f.write("\tfloat y_pred;\n\n")
        f.write(f"\tif (features == NULL || n_features != {n_features})\n")
        f.write("\t\texit(1);\n");
        f.write(f"\ty_pred = {bias};\n")
        for c in model.coef_:
            f.write(f"\ty_pred += *features++ * {c};\n")
        f.write("\treturn y_pred;\n")
        f.write("}\n")

def generate_main_fun(X: list[float], filename: str) -> None:
    n_features = len(X)
    with open(filename, 'a') as f:
        f.write("\nint main(void)\n")
        f.write("{\n")
        f.write(f"\tfloat X[] = {{ {', '.join(str(x) for x in X)} }};\n")
        f.write(f'\tprintf("y_pred is: %f\\n", predict(X, {n_features}));\n')
        f.write(f"\treturn 0;\n")
        f.write("}\n")

if __name__ == "__main__":
    model = load_model("../../models/regression.joblib")
    filename = "linear_model_predict.c"
    generate_predict_fun(model, filename)
    generate_main_fun([120, 3, 0], filename)
    print(f"gcc {filename} -o {filename[:-2]}")

