import os
import joblib
from sklearn.linear_model import LinearRegression

def generate_predict_fun(n_params: int, filename: str) -> None:
    with open(filename, 'w') as f:
        f.write("#include <stdio.h>\n")
        f.write("#include <stdlib.h>\n\n")
        f.write("int simple_tree(float *features, int n_features)\n")
        f.write("{\n")
        f.write("\tint res;\n\n")
        f.write("\tif (features == NULL || n_features < 1)\n")
        f.write("\t\texit(1);\n")
        f.write("\tres = 1;\n")
        for _ in range(n_params):
            f.write(f"\tres = res && *features++ > 0;\n")
        f.write("\treturn res;\n")
        f.write("}\n")

def generate_main_fun(X: list[float], filename: str) -> None:
    n_features = len(X)
    with open(filename, 'a') as f:
        f.write("\nint main(void)\n")
        f.write("{\n")
        f.write(f"\tfloat X[] = {{ {', '.join(str(x) for x in X)} }};\n")
        f.write(f'\tprintf("res is: %d\\n", simple_tree(X, {n_features}));\n')
        f.write(f"\treturn 0;\n")
        f.write("}\n")

if __name__ == "__main__":
    filename = "simple_tree.c"
    array = [120, 3, 0]
    generate_predict_fun(len(array), filename)
    generate_main_fun(array, filename)
    print(f"gcc {filename} -o {filename[:-2]}")

