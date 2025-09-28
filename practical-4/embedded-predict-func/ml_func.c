#include <stdlib.h>
#include <stdio.h>

float linear_regression_prediction(float *features, float *thetas, int n_params)
{
    float y_pred;

    if (features == NULL || thetas == NULL || n_params <= 0) {
        fprintf(stderr, "linear_regression_prediction: bad argument\n");
        exit(1);
    }
    y_pred = *thetas++;     /* bias is the first element */
    for (; n_params > 0; n_params--)
        y_pred += *features++ * *thetas++;
    return y_pred;
}

float exp_approx(float x, int n_term)
{
    int i;
    float approx, power, fact;

    approx = power = fact = 1;
    for (i = 0; i < n_term; i++) {
        power *= x;
        fact *= i+1;
        approx += power / fact;
    }
    return approx;
}

float sigmoid(float x)
{
    return (1 / (1 + exp_approx(-x, 10)));
}

float logistic_regression(float *features, float *thetas, int n_params)
{
    float x;

    if (features == NULL || thetas == NULL || n_params <= 0) {
        fprintf(stderr, "logistic_regression: bad argument\n");
        exit(1);
    }
    x = *thetas++;
    for (; n_params > 0; n_params--)
        x += *features++ * *thetas++;
    return sigmoid(x);
}
